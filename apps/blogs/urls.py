from django.urls import path, re_path

from apps.blogs import views

app_name = 'blogs'

urlpatterns = [
    path('blog/', views.blog_list, name='list'),
    re_path(r'^blog/(?P<slug>[-\w]+)/$', views.blog_detail, name='detail'),
]
