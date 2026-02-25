from django.urls import path
from . import views

app_name = 'sarapan'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/search-menu/', views.search_menu_api, name='search_menu_api'),
    path('api/update-session/', views.update_session_api, name='update_session_api'),
]