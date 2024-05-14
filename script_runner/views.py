from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import subprocess
import os
import json

def index(request):
    # The template path is 'app_name/template_name.html'
    return render(request, 'script_runner/index.html')

@csrf_exempt  # Normally, ensure CSRF protection is enabled; it's exempted here for simplicity in POST handling
def run_script(request):
    if request.method == 'POST':
        script_name = request.POST.get('script_name')
        script_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scripts', script_name)

        if not os.path.isfile(script_path):
            return HttpResponse("Script does not exist.", status=404)

        try:
            result = subprocess.run(['python', script_path], capture_output=True, text=True, check=True)
            return HttpResponse(f"Output:<br>{result.stdout}<br>Error:<br>{result.stderr}", content_type="text/html")
        except subprocess.CalledProcessError as e:
            return HttpResponse(f"An error occurred: {e}", status=500)
    else:
        return HttpResponse("Invalid request", status=400)



# Leaflet Map View
def leaflet_map(request):
    return render(request, 'script_runner/leaflet_map.html')

# Polygon Processing View
def process_polygon(request):
    if request.method == 'POST':
        polygon_data = request.POST.get('polygon_data')

        # Define the path where you want to store the polygon data
        output_directory = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/polygon'
        output_filename = 'polygon_data.geojson'

        # Ensure the directory exists, if not, create it
        os.makedirs(output_directory, exist_ok=True)

        output_path = os.path.join(output_directory, output_filename)

        # Write the polygon data to the specified file
        with open(output_path, 'w') as file:
            file.write(polygon_data)

        return HttpResponse(f"Polygon data saved successfully at {output_path}!")
    return redirect('leaflet_map')

