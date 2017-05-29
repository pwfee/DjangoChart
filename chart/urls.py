from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from chart import views
urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^json/', views.file_json, name='json'),
    url(r'^show/', views.show_csv_item, name='show_csv'),
    url(r'^top/', TemplateView.as_view(template_name="top.html"),
                       name='top'),
    url(r'^nav/', TemplateView.as_view(template_name="nav.html"),
                       name='nav'),
]
