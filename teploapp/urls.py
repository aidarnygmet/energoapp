"""
URL configuration for teploapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app.views import save_data, save_kotel_status, update_kotel_status, save_kotel_info, graph_data,update_graph, kotel_graph_data
from app import consumer
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('save-data/', save_data, name='save-data'),
    path('save-kotel-status/', save_kotel_status, name='save_kotel_status'),
    path('update-kotel-status/<int:object_id>/', update_kotel_status, name='update_kotel_status'),
    path('save-kotel-info/', save_kotel_info, name='save_kotel_info'), 
    path('graph-data/', graph_data, name='graph_data'),
    path('update-graph/', update_graph, name='update_graph'),
    path('kotel-graph-data/', kotel_graph_data, name='kotel_graph_data'),
    # ... other URL patterns ...
]
urlpatterns += staticfiles_urlpatterns()

