from django.urls import path, re_path

from apps.teacher import views

app_name = 'teacher'

urlpatterns = [
    path('teachers/', views.teacher_list, name='list'),
    path('teachers/join/', views.teacher_apply, name='apply'),
    re_path(r'^teachers/(?P<slug>[-\w]+)/$', views.teacher_detail, name='detail'),
]
