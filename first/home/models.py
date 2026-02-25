from django.db import models
from django.contrib.auth.models import User 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    no_telp = models.CharField(max_length=15, unique=True)
    alamat = models.TextField()

    def __str__(self):
        return f"{self.user.first_name} - {self.no_telp}"

class JastipItem(models.Model):
    KATEGORI_CHOICES = [
        ('Sarapan', 'Sarapan'),
        ('Makan Siang', 'Makan Siang'),
        ('Makan Malam', 'Makan Malam'),
    ]

    nama_makanan = models.CharField(max_length=200)
    toko = models.CharField(max_length=100)
    harga = models.DecimalField(max_digits=10, decimal_places=0)
    biaya_jastip = models.DecimalField(max_digits=10, decimal_places=0)
    gambar_url = models.URLField(blank=True)
    kategori = models.CharField(max_length=20, choices=KATEGORI_CHOICES, default='Makan Siang')
    status_open = models.BooleanField(default=True)
    deadline = models.DateTimeField()

    def __str__(self):
        return f"[{self.kategori}] {self.nama_makanan}"