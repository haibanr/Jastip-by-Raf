from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import UserProfile

def signup_view(request):
    if request.method == 'POST':
        nama = request.POST['nama']
        no_telp = request.POST['no_telp']
        alamat = request.POST['alamat']
        password = request.POST['password']

        if User.objects.filter(username=no_telp).exists():
            messages.error(request, 'Nomor telepon sudah terdaftar!')
            return redirect('home:signup')

        user = User.objects.create_user(
            username=no_telp, 
            password=password, 
            first_name=nama
        )
        UserProfile.objects.create(user=user, no_telp=no_telp, alamat=alamat)
        
        login(request, user)
        return redirect('home:index')
        
    return render(request, 'home/signup.html')

def login_view(request):
    if request.method == 'POST':
        no_telp = request.POST['no_telp']
        password = request.POST['password']
        
        user = authenticate(request, username=no_telp, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            messages.error(request, 'Nomor WA atau Password salah!')
            
    return render(request, 'home/login.html')

def logout_view(request):
    logout(request)
    return redirect('home:index')

def index(request):
    sekarang = datetime.now().hour
    
    kategori_data = [
        {
            'nama': 'Sarapan',
            'url': 'sarapan:index',
            'img': 'https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?q=80&w=500',
            'is_active': 6 <= sekarang < 11,
            'jam': '06:00 - 11:00'
        },
        {
            'nama': 'Makan Siang',
            'url': 'makan_siang:index',
            'img': 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=500',
            'is_active': 11 <= sekarang < 16,
            'jam': '11:00 - 16:00'
        },
        {
            'nama': 'Makan Malam',
            'url': 'makan_malam:index',
            'img': 'https://images.unsplash.com/photo-1514516348920-f5d92b8473c0?q=80&w=500',
            'is_active': 17 <= sekarang < 22,
            'jam': '17:00 - 22:00'
        },
    ]
    
    return render(request, 'home/index.html', {'kategori_list': kategori_data})