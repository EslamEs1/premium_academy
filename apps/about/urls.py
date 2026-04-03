from django.urls import path

from apps.about import views

app_name = 'about'

urlpatterns = [
    path('about/', views.about_page, name='about'),
    path('how-it-works/', views.how_it_works_page, name='how_it_works'),
]
