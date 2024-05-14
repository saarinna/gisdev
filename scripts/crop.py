from qgis.core import QgsApplication

# Supply path to qgis install location
# Linux and Anaconda
# Need to install QGIS into an environment
QgsApplication.setPrefixPath('/home/joona/anaconda3/envs/qgis311/share/qgis', True)

# Create a reference to the QgsApplication.  Setting the
# second argument to False disables the GUI.
qgs = QgsApplication([], False)

# Load providers
qgs.initQgis()

# Put your pyqgis code here:
print("Success!")

# Finally, exitQgis() is called to remove the
# provider and layer registries from memory
qgs.exitQgis()

import datetime
from osgeo import gdal
import numpy as np
from osgeo.gdalconst import *
from PyQt5.QtCore import QDate, QTime
import sys
import os
from qgis.core import QgsApplication
sys.path.append('/home/joona/.local/share/QGIS/QGIS3/profiles/default/python/plugins') # on linux
import processing
from processing_umep.processing_umep_provider import ProcessingUMEPProvider
umep_provider = ProcessingUMEPProvider()
QgsApplication.processingRegistry().addProvider(umep_provider)

from processing.core.Processing import Processing
Processing.initialize()

import warnings
warnings.filterwarnings("ignore")

# Input files definition
input_directory = "/home/joona/Desktop/UMEP_SERVER/Data/data_server/"

#input_cdsm = 'CDSM_KRbig.asc'
input_dsm = 'DSM_CLIP.tif'
input_dem = 'DEM_CLIP.tif'
#input_landcover = 'landcover.tif'
input_meteo = '/home/joona/Desktop/UMEP_SERVER/UMEP_SERVER/Data/data_server/WEATHER_UMEP_FORMAT.txt'

# Defines an output directory where will be stored your outputs (and intermediate results)
output_dir = "/home/joona/Desktop/UMEP_SERVER/Data/data_server/ouput/"
cropdsmout = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/croppedsm.tif'
cropdemout = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/croppedem.tif'

lyr = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/polygon/polygon_data.geojson'
parameter = {
    'INPUT': lyr,
    'TARGET_CRS': 'EPSG:3879',
    'OUTPUT': '/home/joona/Desktop/UMEP_SERVER/Data/data_server/polygon/polygon_data_reprojected.geojson'
}
result = processing.run('native:reprojectlayer', parameter)['OUTPUT']

input_mask = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/polygon/polygon_data_reprojected.geojson'

# Set the EPSG code for the .asc file which has no EPSG
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
