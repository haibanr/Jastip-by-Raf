from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nama
    
    class Meta:
        verbose_name_plural = "Categories"

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories')
    nama = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.category.nama} - {self.nama}"

class Menu(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='menus')
    nama_menu = models.CharField(max_length=200)
    deskripsi = models.TextField()
    harga = models.PositiveIntegerField()
    gambar = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_best_seller = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama_menu