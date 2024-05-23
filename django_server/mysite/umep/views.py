from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import subprocess
import os
import json
import warnings


def index(request):
    return render(request, 'umep/index.html')

@csrf_exempt  # Disable CSFR

def run_script(request):
    if request.method == 'POST':
        script_name = request.POST.get('script_name')
        script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scripts', script_name)
        # run the script, and give out an httpresponse text
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        return HttpResponse(f"Script Ran Succesfully. Go Back With Browser Back Button.", content_type="text/html")




# Leaflet Map View
def leaflet_map(request):
    return render(request, 'umep/leaflet_map.html')

# Polygon Processing View
def process_polygon(request):
    if request.method == 'POST':
        polygon_data = request.POST.get('polygon_data')

        polygon_output_path = '/home/user/Documents/django_server/data/polygon/polygon_data.geojson'

        # Write polygon data to defined output
        with open(polygon_output_path, 'w') as file:
            file.write(polygon_data)

        return HttpResponse(f"Polygon data saved successfully at {polygon_output_path}!")
    return redirect('leaflet_map')
