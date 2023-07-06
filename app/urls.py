from django.urls import path
from . import views
from .views import save_data

urlpatterns = [
    path('', views.base, name='base'),
    path('save-data/', save_data, name='save_data')
    # ... other URL patterns ...
]
