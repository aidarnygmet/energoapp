from django.urls import path
from . import views
from .views import save_data, save_kotel_status, update_kotel_status, save_kotel_info

urlpatterns = [
    path('', views.base, name='base'),
    path('save-data/', save_data, name='save_data'),
    path('save-kotel-status/', save_kotel_status, name='save_kotel_status'),
    path('update-kotel-status/<int:object_id>/', update_kotel_status, name='update_kotel_status'),
    path('save-kotel-info/', save_kotel_info, name='save_kotel_info'),
    path('demo/', views.demo, name='demo')
    # ... other URL patterns ...
]
