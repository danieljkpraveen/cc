from django.urls import path
from .views import index, eml_to_csv


urlpatterns = [
    path('', index, name='index'),
    path('eml_to_csv/', eml_to_csv, name='eml_to_csv'),
]
