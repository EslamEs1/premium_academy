from django.urls import path

from apps.main import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('faq/', views.faq_page, name='faq'),
    path('privacy/', views.privacy_page, name='privacy'),
    path('terms/', views.terms_page, name='terms'),
]
