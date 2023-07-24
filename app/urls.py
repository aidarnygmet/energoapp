from django.urls import path
from . import views
from .views import save_data, save_kotel_status, update_kotel_status, save_kotel_info, graph_data, update_graph,kotel_graph_data
from app import consumer
urlpatterns = [
    path('', views.base, name='base'),
    path('save-data/', save_data, name='save_data'),
    path('save-kotel-status/', save_kotel_status, name='save_kotel_status'),
    path('update-kotel-status/<int:object_id>/', update_kotel_status, name='update_kotel_status'),
    path('save-kotel-info/', save_kotel_info, name='save_kotel_info'),
    path('graph-data/', graph_data, name='graph_data'),
    path('demo/', views.demo, name='demo'),
    path('update-graph/', update_graph, name='update_graph'),
    path('kotel-graph-data/', kotel_graph_data, name='kotel_graph_data'),
    # ... other URL patterns ...
]
