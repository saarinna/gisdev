from qgis.core import QgsApplication

# Supply path to qgis install location
# Linux and Anaconda
# Need to install QGIS into an environment
QgsApplication.setPrefixPath('/home/user/anaconda3/envs/qgis311/share/qgis', True)

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
sys.path.append('/home/user/.local/share/QGIS/QGIS3/profiles/default/python/plugins') # on linux
import processing
from processing_umep.processing_umep_provider import ProcessingUMEPProvider
umep_provider = ProcessingUMEPProvider()
QgsApplication.processingRegistry().addProvider(umep_provider)

from processing.core.Processing import Processing
Processing.initialize()

# CHANGE "/user/" TO YOUR OWN USERNAME
# Input directories
shadowmats_input = '/home/user/Documents/django_server/data/output/SVF/shadowmats.npz'
skyviewfactor_tif_input = '/home/user/Documents/django_server/data/output/SVF/SkyViewFactor.tif'
skyviewfactor_input = '/home/user/Documents/django_server/data/output/SVF/svfs.zip'
wallaspect_input = '/home/user/Documents/django_server/data/output/wallAspect.tif'
wallheight_input = '/home/user/Documents/django_server/data/output/wallHeight.tif'
input_dsm = '/home/user/Documents/django_server/data/output/croppedsm.tif'
input_dem = '/home/user/Documents/django_server/data/output/croppedem.tif'
input_weather = '/home/user/Documents/django_server/data/weather_umep.txt'

# Output directory
output_directory = '/home/user/Documents/django_server/data/output/solweig'


processing.run("umep:Outdoor Thermal Comfort: SOLWEIG",
               { 'INPUTMET' : input_weather,
                'INPUT_ANISO' : shadowmats_input,
                'INPUT_ASPECT' : wallaspect_input,
                'INPUT_DEM' : input_dem,
                'INPUT_DSM' : input_dsm,
                'INPUT_HEIGHT' : wallheight_input,
                'INPUT_SVF' : skyviewfactor_input,
                'OUTPUT_DIR' : output_directory,
                'ABS_L' : 0.95,
                'ABS_S' : 0.7,
                'ACTIVITY' : 80,
                'AGE' : 35,
                'ALBEDO_GROUND' : 0.15,
                'ALBEDO_WALLS' : 0.2,
                'CLO' : 0.9,
                'CONIFER_TREES' : False,
                'CYL' : True,
                'EMIS_GROUND' : 0.95,
                'EMIS_WALLS' : 0.9,
                'HEIGHT' : 180,
                'INPUT_CDSM' : None,
                'INPUT_LC' : None,
                'INPUT_TDSM' : None,
                'INPUT_THEIGHT' : 25,
                'LEAF_END' : 300,
                'LEAF_START' : 97,
                'ONLYGLOBAL' : True,
                'OUTPUT_KDOWN' : False,
                'OUTPUT_KUP' : False,
                'OUTPUT_LDOWN' : False,
                'OUTPUT_LUP' : False,
                'OUTPUT_SH' : False,
                'OUTPUT_TMRT' : True,
                'OUTPUT_TREEPLANTER' : False,
                'POI_FIELD' : '',
                'POI_FILE' : None,
                'POSTURE' : 0,
                'SAVE_BUILD' : False,
                'SENSOR_HEIGHT' : 10,
                'SEX' : 0,
                'TRANS_VEG' : 3,
                'USE_LC_BUILD' : False,
                'UTC' : 3,
                'WEIGHT' : 75 })
