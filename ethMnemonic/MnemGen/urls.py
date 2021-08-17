from django.conf.urls import url
from django.urls import path

from . import views
# Defines the various urls patterns used by the view and the app.
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('ethtomnem/', views.EthtoMnem, name='Eth_to_Mnem'),
    path('mnemtoeth/',views.MnemtoEth, name="Mnem_to_Eth"),
    path('mnemvalid/',views.MnemChecker, name="MnemValid")
]