from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('share/', views.share, name='share'),
    path('ethtomnem/', views.EthtoMnem, name='Eth_to_Mnem'),
    path('mnemtoeth/',views.MnemtoEth, name="Mnem_to_Eth"),
]