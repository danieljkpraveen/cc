from django.urls import path
from .views import (
    index,
    eml_to_csv,
    check_firewall_connection,
    connect_and_fetch_panos_version
)


urlpatterns = [
    path('', index, name='index'),
    path('eml_to_csv/', eml_to_csv, name='eml_to_csv'),
    path('check_firewall_connection/', check_firewall_connection,
         name='check_firewall_connection'),
    path('connect_and_fetch_panos_version/', connect_and_fetch_panos_version,
         name='connect_and_fetch_panos_version'),
]
