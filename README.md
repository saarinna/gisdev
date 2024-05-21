# GIS Development Project

This repository contains an application made to integrate QGIS with Django, utilizing the UMEP (Urban Multi-scale Environmental Predictor) QGIS plugin for spatial analysis and environmental modeling. The focus of the application is to estimate the mean radiant temperature (Tmrt) in complex urban environments using the SOLWEIG (SOlar and LongWave Environmental Irradiance Geometry) model.

The application is build with Django, which is a high-level web framework for building web applications using the Python programming language. This application runs on a local server, but technically it should be possible to transfer the framework in to a web server. QGIS and its processing tools and plugins are used in the majority of scripts to run spatial analysis and environmental modeling. The Urban Multi-scale Environmental Predictor (UMEP) is a climate service modeling tool, available as a plugin for QGIS.

Read more about [UMEP](https://umep-docs.readthedocs.io/en/latest/index.html).

Read more about the SOLWEIG model on [UMEP Docs](https://umep-docs.readthedocs.io/en/latest/OtherManuals/SOLWEIG.html).

# Installation Guide

## Prerequisites
- A Linux based operating system

### 1. Install QGIS
1. **Download and Install QGIS:**
   - Go to [QGIS website](https://www.qgis.org/en/site/forusers/download.html) to install QGIS.

2. **Launch QGIS and Install UMEP Plugins:**
   - Open QGIS.
   - Go to **Plugins** > **Manage and Install Plugins**.
   - Search for "UMEP" and install both the **UMEP** and **UMEP Processing** plugins.

3. **Restart QGIS:**
   - Ignore any warnings that may appear upon launching QGIS.

4. **Close QGIS:**

### 2. Set Up Conda Environment

1. **Install Anaconda:**
   - Download and install Anaconda from [Anaconda website](https://docs.anaconda.com/free/anaconda/install/index.html).

2. **Import the Conda Environment:**
   - Download the `qgis311.yml` file from the project repository.
   - Open a terminal in the directory containing the `qgis311.yml` file.
   - Run the following command to create the environment:
     ```bash
     conda env create -f qgis311.yml
     ```

3. **Activate the Conda Environment:**
   - Activate the environment with:
     ```bash
     conda activate qgis311
     ```

4. **Open QGIS from Conda:**
   - Launch QGIS from the terminal by typing:
     ```bash
     qgis
     ```
5. **Set the Processing paths???**

### 3. Set Up the Project Files

1. **Download the Project Files:**
   - Download the `mysite` folder from the project repository.
   - Place it in the `Documents` directory on your local machine, so the path looks like: `/home/user/Documents/django_server`.




# Scripts and Leaflet Map

The application has scripts that use PyQGIS, UMEP processing plugin, and different Python libraries. The scripts have input and output paths that need to be modified. There is also an interactive map, where the user can draw a polygon, that will be used to crop the study area.

**Leaflet Map**

The map can be used to easily define the desired study area. After submitting the polygon, it will be used as input for cropping input data.
  - Output:
     - polygon_data.geojson


**crop.py**
 
The script takes the user defined polygon, reprojects it, and crops the digital elevation model and digital surface model.
   - Input:
      - DSM_Helsinki.tif
	   - DEM_Helsinki.tif
	   - polygon_data.geojson
	 	   - The user drawn polygon.
   - Output:
            - croppedsm.tif
	    - croppedem.tif


**skyviewfactor.py**

The script creates skyviewfactor TIF files, shadowmats, wall heights, and wall aspects for input into the SOLWEIG analysis.
   - Input:
      - croppedsm.tif
      - croppedem.tif
   - Output:
      - skyviewfactor.tif
	   - svf.zip
	   - shadowmats.npz
	   - wallAspect.tif
	   - wallHeight.tif

**solweig.py**

The script runs the SOLWEIG analysis, using the outputs from the previous scripts as input.
   - Input:
      - croppedsm.tif
	   - croppedem.tif
      - skyviewfactor.tif
	   - svf.zip
	   - shadowmats.npz
	   - wallAspect.tif
	   - wallHeight.tif
   - Output:
      - Tmrt_average.tif

**view_image.py**

The script uses Python Library Pillow to read in the tif file. Python library matplotlib is used to display the Tmrt_average.tif, created in the SOLWEIG analysis.

   - Input:
      - Tmrt_average.tif

The following parameters can be changed by the user:
   - vmin
   - vmax
      - These parameters define the range of the values displayed. It is recommended to keep vmin at 10 or less.
   - cmap
      - The colormap can be set to the users preference. See: [available colormaps in matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html).
 
# Input Data

**DEM_Helsinki.tif**

The digital elevation model (DEM) represents the grounds surface elevation.

- Resolution: 1 meters
- Format: GeoTiff
- Coordinate system: EPSG:3879 - ETRS89 / GK25FIN
- Elevation model of the City of Helsinki
   - https://hri.fi/data/en_GB/dataset/helsingin-korkeusmalli  

 
 **DSM_Helsinki.tif**

The digital surface model (DSM) represents the grounds surface elevation and height of buildings.

- Resolution: 1 meters
- Format: GeoTiff
- Coordinate system: EPSG:3879 - ETRS89 / GK25FIN
  - Derived from the Elevation model of the City of Helsinki, using UMEP digital surface model generator.
 
**weather_umep.txt**

 Weather data retrieved from the global the Coopernicus programme and Climate Data Store. Used in SOLWEIG analysis.

# How To Use

Before the application can be used, the scripts file paths need to be modified.

In `/home/user/Documents/django_server/scripts` all four scripts need to be modified.
The `/home/user/Documents/django_server/umep/views.py` file needs to be modified.
The files include filepaths `/home/user/Documents/django_server/...` where the `user` needs to be changed to match your local machines username.

1. **Open terminal in the Project Directory:**
   - Open a terminal in the root of the Django project, where `manage.py` is located.

2. **Activate the Conda Environment:**
   - Activate the Conda environment by running:
     ```bash
     conda activate qgis311
     ```
3. **Run the Django Server:**
   - Start the Django development server with:
     ```bash
     python manage.py runserver
     ```
4. **Access the Application:**
   - Open your browser and go to [http://127.0.0.1:8000/umep/](http://127.0.0.1:8000/umep/) to access the application.

5. Click on Select Area for SOLWEIG

- A map view will open.
- Use the drawing tools on the left hand side to draw a single polygon representing the area where the anaylsis will be run.
- Once the polygon has been drawn, press Submit Polygon.
- A message will appear, telling that the polygon was saved succesfully.
- Use browsers back button to get back to the main page.

6. Click on Crop Data

- Wait for the script to finish.
- A message will appear, telling that the script has been ran succesfully.
- Use browsers back button to get back to the main page.

7. Click on Create Skyviewfactors and Wall Aspect and Ratio

- Wait for the script to finish.
- A message will appear, telling that the script has been ran succesfully.
- Use browsers back button to get back to the main page.

8. Click on Run SOLWEIG

- Wait for the script to finish.
- A message will appear, telling that the script has been ran succesfully.
- Use browsers back button to get back to the main page.

9. Click on View Result

- A new window will open with a png image of the result.

The tif files of the SOLWEIG output can be retrieved from django_server - data - output -solweig - Tmrt_average.tif
