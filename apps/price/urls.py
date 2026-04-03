from django.urls import path

from apps.price import views

app_name = 'price'

urlpatterns = [
    path('pricing/', views.pricing_page, name='pricing'),
]
