import os
import pickle
import pandas as pd
import requests
import time
import random
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings

from sklearn.metrics.pairwise import cosine_similarity
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

# --- CONFIGURATION ---
ML_PATH = os.path.join(settings.BASE_DIR, 'ml_assets')
ITS_COORDS = (-7.2823, 112.7944)
WEATHER_API_KEY = "05270066ca71558af95dcfe18cfc50aa"
SURABAYA_ID = "1625822"

geolocator = Nominatim(user_agent="jastip_its_final_v6")
LOCATION_CACHE = {}
WEATHER_CACHE = {'data': 'Clear', 'last_update': None}

# --- CORE HELPERS ---

def get_coords_accurate(merchant_name):
    area_name = str(merchant_name).split(',')[-1].strip() if ',' in str(merchant_name) else str(merchant_name)
    if area_name in LOCATION_CACHE:
        return LOCATION_CACHE[area_name]
    
    try:
        location = geolocator.geocode(f"{area_name}, Surabaya, Indonesia", timeout=5)
        time.sleep(1.1) 
        if location:
            coords = (location.latitude, location.longitude)
            LOCATION_CACHE[area_name] = coords
            return coords
    except:
        pass
    return ITS_COORDS

def get_real_weather():
    now = datetime.now()
    if WEATHER_CACHE['last_update'] and (now - WEATHER_CACHE['last_update']).seconds < 1800:
        return WEATHER_CACHE['data']

    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?id={SURABAYA_ID}&appid={WEATHER_API_KEY}"
        res = requests.get(url, timeout=3).json()
        status = res['weather'][0]['main']
        WEATHER_CACHE.update({'data': status, 'last_update': now})
        return status
    except:
        return "Rain" if 14 <= now.hour <= 18 else "Clear"

def load_ml_assets():
    try:
        assets = {}
        files = {
            'df': 'surabaya_menu_clean.pkl',
            'tfidf': 'tfidf_vectorizer.pkl',
            'matrix': 'tfidf_matrix.pkl'
        }
        for key, filename in files.items():
            with open(os.path.join(ML_PATH, filename), 'rb') as f:
                assets[key] = pickle.load(f)
        return assets['df'], assets['tfidf'], assets['matrix']
    except Exception as e:
        print(f"ML Assets Error: {e}")
        return None, None, None

# --- AI SCORING ENGINE ---

def get_smart_recommendations(request, num_results=8):
    df_sby, _, _ = load_ml_assets()
    if df_sby is None: return []

    weather = get_real_weather()
    hour = datetime.now().hour
    is_rush = (7 <= hour <= 9) or (16 <= hour <= 19)
    last_cat = request.session.get('last_category', 'Ayam & Bebek')
    
    df_sample = df_sby.sample(min(len(df_sby), 20)).copy()
    results = []

    for _, row in df_sample.iterrows():
        m_coords = get_coords_accurate(row.get('merchant_name'))
        dist = geodesic(ITS_COORDS, m_coords).km
        
        # Traffic & Scoring Logic
        traffic = "Macet Parah" if is_rush and dist > 3.0 else ("Padat" if is_rush else "Lancar")
        score = 0.5 if row.get('category') == last_cat else 0.0
        
        prod_lower = str(row['product']).lower()
        warm_keywords = ['soto', 'bakso', 'kuah', 'pedas', 'mie', 'hot', 'kopi']
        cold_keywords = ['es', 'juice', 'dingin', 'ice', 'fresh', 'boba']

        if weather in ['Rain', 'Clouds', 'Thunderstorm']:
            if any(x in prod_lower for x in warm_keywords):
                score += 1.0
                badge = "Nikmat saat Hujan 🌧️"
            else:
                badge = "Rekomendasi Spesial"
        else:
            if any(x in prod_lower for x in cold_keywords):
                score += 1.0
                badge = "Segar saat Gerah ☀️"
            else:
                badge = "Pilihan Favorit"

        results.append({
            'nama_menu': row['product'],
            'harga': int(row['price']),
            'jarak': round(dist, 1),
            'traffic': traffic,
            'weather_icon': "🌧️" if weather in ['Rain', 'Clouds'] else "☀️",
            'badge': badge,
            'gambar': f"https://placehold.co/400x300?text={str(row['product']).replace(' ', '+')}",
            'deskripsi': f"📍 {row.get('merchant_name')}",
            'score': score
        })

    return sorted(results, key=lambda x: x['score'], reverse=True)[:num_results]

# --- VIEW HANDLERS ---

def index(request):
    from .models import SubCategory, Menu
    subcategories = SubCategory.objects.all()
    active_sub = subcategories.first()
    menus = Menu.objects.filter(subcategory=active_sub, is_available=True) if active_sub else []
    
    return render(request, 'makan_malam/index.html', {
        'subcategories': subcategories,
        'active_sub': active_sub,
        'menus': menus,
        'recommendations': get_smart_recommendations(request),
        'history': request.session.get('purchase_history', [])[:5],
    })

def search_menu_api(request):
    query = request.GET.get('q', '').strip()
    df_sby, tfidf, tfidf_matrix = load_ml_assets()
    if df_sby is None: return JsonResponse({'results': [], 'category_name': "Error"})

    results = []
    is_rush = (7 <= datetime.now().hour <= 9) or (16 <= datetime.now().hour <= 19)

    if query:
        query_vec = tfidf.transform([query.lower()])
        sim = cosine_similarity(query_vec, tfidf_matrix).flatten()
        indices = sim.argsort()[-15:][::-1]
        
        for i in indices:
            if sim[i] > 0.1:
                row = df_sby.iloc[i]
                dist = geodesic(ITS_COORDS, get_coords_accurate(row.get('merchant_name'))).km
                results.append({
                    'nama_menu': row['product'],
                    'harga': int(row['price']),
                    'deskripsi': f"📍 {row.get('merchant_name')}",
                    'gambar': f"https://placehold.co/400x300?text={str(row['product']).replace(' ', '+')}",
                    'jarak': round(dist, 1),
                    'traffic': "Padat" if is_rush else "Lancar"
                })
        label = f"Hasil: {query}"
    else:
        df_random = df_sby.sample(n=min(len(df_sby), 12))
        for _, row in df_random.iterrows():
            dist = geodesic(ITS_COORDS, get_coords_accurate(row.get('merchant_name'))).km
            results.append({
                'nama_menu': row['product'],
                'harga': int(row['price']),
                'deskripsi': f"📍 {row.get('merchant_name')}",
                'gambar': f"https://placehold.co/400x300?text={str(row['product']).replace(' ', '+')}",
                'jarak': round(dist, 1),
                'traffic': "Lancar"
            })
        label = "Explore Menu"

    return JsonResponse({'results': results, 'category_name': label})

def update_session_api(request):
    name = request.GET.get('name')
    history = request.session.get('purchase_history', [])
    if name and name not in [h.get('nama') for h in history]:
        history.insert(0, {'nama': name, 'harga': request.GET.get('price', 0), 'tgl': datetime.now().strftime("%H:%M")})
    
    request.session['purchase_history'] = history[:5]
    request.session['last_category'] = request.GET.get('category', '')
    request.session.modified = True
    return JsonResponse({'status': 'ok'})