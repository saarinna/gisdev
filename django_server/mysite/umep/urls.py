from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('run-script/', views.run_script, name='run_script'),
    path('leaflet-map/', views.leaflet_map, name='leaflet_map'),
    path('process-polygon/', views.process_polygon, name='process_polygon'),
]
