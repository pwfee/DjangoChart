from django.conf.urls import include, url
from django.contrib import admin
from chart import views
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^csv/', views.show_csv_item, name='show_csv'),

]
