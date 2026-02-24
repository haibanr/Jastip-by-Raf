# Jastip-by-Raf
AI-Powered Smart Food Delivery for ITS Surabaya. Built with Django, Scikit-Learn, and Real-Time Contextual Intelligence.


# 🛵 Jastip Raf: Hyper-Local Food AI Delivery
> **Smart Food Recommendation System with Real-Time Context Awareness**
<img width="1364" height="606" alt="home" src="https://github.com/user-attachments/assets/07783d3c-a7ff-47f8-be86-9142fa34d2c5" />


---

## 📝 Deskripsi Singkat
**Jastip Raf** adalah proyek platform *smart-delivery* berbasis web yang dirancang khusus untuk memfasilitasi jasa titip makanan di lingkungan **Kampus ITS Surabaya**. Berbeda dengan aplikasi jastip konvensional, Jastip Raf mengintegrasikan **Kecerdasan Buatan (AI)** untuk memberikan pengalaman pemesanan yang personal dan kontekstual.

Aplikasi ini mampu mendeteksi cuaca secara *real-time* dan menganalisis waktu pemesanan untuk memberikan rekomendasi menu yang paling sesuai secara otomatis. Dengan dukungan **TF-IDF Machine Learning** untuk pencarian menu yang akurat dan fitur **Traffic Intelligence** untuk memprediksi kepadatan jalan, Jastip Raf mengubah cara mahasiswa memesan makanan menjadi lebih cerdas dan efisien.

---

## 🚀 Fitur Unggulan

### 1. Smart AI Recommendation Engine (Weather & Time Aware)
Sistem menggunakan mesin skoring cerdas yang menganalisis kondisi cuaca melalui API. 
* **Hujan:** Otomatis mempromosikan menu hangat/berkuah.
* **Panas:** Menu segar dan dingin akan naik ke peringkat atas.

> **<img width="793" height="465" alt="ai_recommend" src="https://github.com/user-attachments/assets/d3eca031-d6ac-42d0-96c0-14d54dd13940" />**
>**[Contoh kasus: rekomendasi menu waktu malam hari]**

### 2. Intelligent Search dengan TF-IDF
Menggunakan algoritma **Cosine Similarity** dan **TF-IDF Vectorizer**. Sistem memahami konteks menu meskipun kata kuncinya tidak persis sama.

> **<img width="1215" height="605" alt="smart_search" src="https://github.com/user-attachments/assets/f5d93875-cbac-4e44-be59-bdbd3f0798a5" />**
> **<img width="1216" height="606" alt="smart_search2" src="https://github.com/user-attachments/assets/a52f8476-3c75-476f-bbbc-0f3d5cac9109" />**


### 3. Real-Time Traffic & Geolocation
Menghitung jarak presisi antara merchant dan titik antar (ITS) menggunakan library **Geopy** serta memberikan status kepadatan jalan secara dinamis.

> **<img width="656" height="578" alt="traffic_info" src="https://github.com/user-attachments/assets/4ab9d26c-00d3-4ae9-8c91-d941f5871507" />**
> **<img width="734" height="336" alt="traffic_info2" src="https://github.com/user-attachments/assets/3e7c758e-c897-44a2-bc81-eb30cc0670bd" />**

### 4. Seamless WhatsApp Integration
Mengonversi keranjang belanja menjadi format pesan teks profesional yang siap dikirim langsung ke kurir melalui WhatsApp.

> **<img width="627" height="170" alt="wa_format" src="https://github.com/user-attachments/assets/bef6896b-ac82-4c12-a66a-fae6a3df7d43" />**

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

