from qgis.core import QgsApplication
# Supply path to qgis install location inside a conda environment
# Linux and Anaconda
QgsApplication.setPrefixPath('/home/user/anaconda3/envs/qgis311/share/qgis', True)
# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)
qgs.initQgis()
qgs.exitQgis()
import datetime
from osgeo import gdal
import numpy as np
from osgeo.gdalconst import *
from PyQt5.QtCore import QDate, QTime
import sys
import os
from qgis.core import QgsApplication
sys.path.append('/home/user/.local/share/QGIS/QGIS3/profiles/default/python/plugins') # on linux
import processing
from processing_umep.processing_umep_provider import ProcessingUMEPProvider
umep_provider = ProcessingUMEPProvider()
QgsApplication.processingRegistry().addProvider(umep_provider)
from processing.core.Processing import Processing
Processing.initialize()

# SET PATH TO INPUT DIRECTORY
input_directory = "/home/user/Documents/django_server/data"
# INPUT DATA NAMES
input_dsm = 'DSM_Helsinki.tif'
input_dem = 'DEM_Helsinki.tif'

# SET PATH FOR OUTPUT
output_dir = "/home/user/Documents/django_server/data/ouput/"
cropdsmout = '/home/user/Documents/django_server/data/output/croppedsm.tif'
cropdemout = '/home/user/Documents/django_server/data/output/croppedem.tif'

# SET THE SAME PATH AS IN VARIABLE "polygon_output_path" IN views.py
polygon_input = '/home/user/Documents/django_server/data/polygon/polygon_data.geojson'

# This needs to be the same as the output path for the reprojected polygon
input_mask = '/home/user/Documents/django_server/data/polygon/polygon_data_reprojected.geojson'


parameter = {
    'INPUT': polygon_input,
    'TARGET_CRS': 'EPSG:3879',
    # Set the output path for the reprojected geojson
    'OUTPUT': '/home/user/Documents/django_server/data/polygon/polygon_data_reprojected.geojson'
}
result = processing.run('native:reprojectlayer', parameter)['OUTPUT']



# Crop the DSM with the reprojected polygon
from qgis.core import QgsCoordinateReferenceSystem
input_dsm_filename = input_dsm.split(".")[0]
crop_dsm = processing.run("gdal:cliprasterbymasklayer",
                           {'INPUT': os.path.join(input_directory, input_dsm),
                            'MASK': os.path.join(input_directory, input_mask),
                            'SOURCE_CRS':None,
                            'TARGET_CRS':None,
                            'NODATA':None,'ALPHA_BAND':False,'CROP_TO_CUTLINE':True,
                            'KEEP_RESOLUTION':True,'SET_RESOLUTION':False,'X_RESOLUTION':None,
                            'Y_RESOLUTION':None,'MULTITHREADING':False,'OPTIONS':'',
                            'DATA_TYPE':0,'EXTRA':'','OUTPUT': cropdsmout
                            })

# Crop the DEM with the reprojected polygon
input_dem_filename = input_dem.split(".")[0]
crop_dem = processing.run("gdal:cliprasterbymasklayer",
                           {'INPUT': os.path.join(input_directory, input_dem),
                            'MASK': os.path.join(input_directory, input_mask),
                            'SOURCE_CRS':None,
                            'TARGET_CRS':None,
                            'NODATA':None,'ALPHA_BAND':False,'CROP_TO_CUTLINE':True,
                            'KEEP_RESOLUTION':True,'SET_RESOLUTION':False,'X_RESOLUTION':None,
                            'Y_RESOLUTION':None,'MULTITHREADING':False,'OPTIONS':'',
                            'DATA_TYPE':0,'EXTRA':'','OUTPUT': cropdemout
                            })
