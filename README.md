# Jastip-by-Raf
AI-Powered Smart Food Delivery for ITS Surabaya. Built with Django, Scikit-Learn, and Real-Time Contextual Intelligence.


# 🛵 Jastip Raf: Hyper-Local Food AI Delivery
> **Smart Food Recommendation System with Real-Time Context Awareness**

---

## 📝 Deskripsi Singkat
**Jastip Raf** adalah platform *smart-delivery* berbasis web yang dirancang khusus untuk memfasilitasi jasa titip makanan di lingkungan **Kampus ITS Surabaya**. Berbeda dengan aplikasi jastip konvensional, Jastip Raf mengintegrasikan **Kecerdasan Buatan (AI)** untuk memberikan pengalaman pemesanan yang personal dan kontekstual.

Aplikasi ini mampu mendeteksi cuaca secara *real-time* dan menganalisis waktu pemesanan untuk memberikan rekomendasi menu yang paling sesuai secara otomatis. Dengan dukungan **TF-IDF Machine Learning** untuk pencarian menu yang akurat dan fitur **Traffic Intelligence** untuk memprediksi kepadatan jalan, Jastip Raf mengubah cara mahasiswa memesan makanan menjadi lebih cerdas dan efisien.

---

## 🚀 Fitur Unggulan

### 1. Smart AI Recommendation Engine (Weather & Time Aware)
Sistem menggunakan mesin skoring cerdas yang menganalisis kondisi cuaca melalui API. 
* **Hujan:** Otomatis mempromosikan menu hangat/berkuah.
* **Panas:** Menu segar dan dingin akan naik ke peringkat atas.

> **[ Masukkan GIF/Gambar Demo Rekomendasi AI di sini ]**

### 2. Intelligent Search dengan TF-IDF
Menggunakan algoritma **Cosine Similarity** dan **TF-IDF Vectorizer**. Sistem memahami konteks menu meskipun kata kuncinya tidak persis sama.

> **[ Masukkan GIF/Gambar Demo Search Bar di sini ]**

### 3. Real-Time Traffic & Geolocation
Menghitung jarak presisi antara merchant dan titik antar (ITS) menggunakan library **Geopy** serta memberikan status kepadatan jalan secara dinamis.

> **[ Masukkan Gambar Detail Jarak & Traffic di sini ]**

### 4. Seamless WhatsApp Integration
Mengonversi keranjang belanja menjadi format pesan teks profesional yang siap dikirim langsung ke kurir melalui WhatsApp.

> **[ Masukkan Gambar Hasil Format Pesan WhatsApp di sini ]**

---

## 🛠️ Tech Stack

| Komponen | Teknologi |
| :--- | :--- |
| **Backend** | Django (Python 3.x) |
| **Frontend** | Tailwind CSS, JavaScript (ES6+) |
| **Machine Learning** | Scikit-Learn (TF-IDF), Pandas |
| **Geospatial** | Geopy (Nominatim API) |
| **API** | OpenWeatherMap API |

---

## 🏗️ Cara Menjalankan Project

1. **Clone Repository**
   ```bash
   git clone [https://github.com/username/jastip-raf.git](https://github.com/username/jastip-raf.git)
