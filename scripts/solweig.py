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

svftifoutput = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/SVF/SkyViewFactor.tif'
svfoutput = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/SVF/'
wallaspect_output = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/wallAspect.tif'
wallheight_output = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/wallHeight.tif'
# Input files definition
input_directory = "/home/joona/Desktop/UMEP_SERVER/Data/data_server/"
input_mask = "mask_layer_geojson.geojson"
#input_cdsm = 'CDSM_KRbig.asc'
input_dsm = 'DSM_CLIP.tif'
input_dem = 'DEM_CLIP.tif'
#input_landcover = 'landcover.tif'
input_meteo = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/WEATHER_UMEP_FORMAT.txt'

# Defines an output directory where will be stored your outputs (and intermediate results)
output_dir = "/home/joona/Desktop/UMEP_SERVER/Data/data_server/ouput/"
cropdsmout = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/croppedsm.tif'
cropdemout = '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/croppedem.tif'



processing.run("umep:Outdoor Thermal Comfort: SOLWEIG",
               {'INPUT_DSM': cropdsmout,
                'INPUT_SVF': os.path.join(svfoutput,'svfs.zip'),
                'INPUT_HEIGHT': wallheight_output,
                'INPUT_ASPECT': wallaspect_output,
                #'INPUT_CDSM': crop_cdsm["OUTPUT"],
                'TRANS_VEG':3,'INPUT_TDSM':None,'INPUT_THEIGHT':25,
                #'INPUT_LC': crop_landcover["OUTPUT"],
                'USE_LC_BUILD':False,
                'INPUT_DEM': cropdemout,
                'SAVE_BUILD':False,
                'INPUT_ANISO': os.path.join(svfoutput,'shadowmats.npz'),
                'ALBEDO_WALLS':0.2,'ALBEDO_GROUND':0.15,'EMIS_WALLS':0.9,'EMIS_GROUND':0.95,
                'ABS_S':0.7,'ABS_L':0.95,'POSTURE':0,'CYL':True,
                'INPUTMET': input_meteo,
                'ONLYGLOBAL':True,'UTC':0,'POI_FILE':None,'POI_FIELD':'','AGE':35,
                'ACTIVITY':80,'CLO':0.9,'WEIGHT':75,'HEIGHT':180,'SEX':0,'SENSOR_HEIGHT':10,
                'OUTPUT_TMRT':True,'OUTPUT_KDOWN':False,'OUTPUT_KUP':False,'OUTPUT_LDOWN':False,
                'OUTPUT_LUP':False,'OUTPUT_SH':False,'OUTPUT_TREEPLANTER':False,
                'OUTPUT_DIR': '/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/solweig'})
