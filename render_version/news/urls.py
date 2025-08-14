from django.urls import path, re_path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.news_list, name='list'),
    re_path(r'^(?P<slug>[-\w]+)/$', views.news_detail, name='detail'),
]
