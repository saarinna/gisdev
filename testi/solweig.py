import matplotlib as plt

from qgis.core import QgsApplication
QgsApplication.setPrefixPath('/home/joona/anaconda3/envs/qgis311/share/qgis', True)
qgs = QgsApplication([], False)
qgs.initQgis()
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

processing.run("umep:Outdoor Thermal Comfort: SOLWEIG",
               { 'ABS_L' : 0.95,
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
                'INPUTMET' : '/home/joona/Documents/UMEP/meteorologic/ERA5_UTC-60.125N-25.0E-116.6A_2020_data_60.txt',
                'INPUT_ANISO' : '',
                'INPUT_ASPECT' : '/home/joona/Documents/UMEP/wall_aspect_clip.tif',
                'INPUT_CDSM' : None,
                'INPUT_DEM' : '/home/joona/Documents/UMEP/DEM_clip_1x1.tif',
                'INPUT_DSM' : '/home/joona/Documents/UMEP/DSM_clip_1x1.tif',
                'INPUT_HEIGHT' : '/home/joona/Documents/UMEP/wall_height_clip.tif',
                'INPUT_LC' : None,
                'INPUT_SVF' : '/home/joona/Documents/UMEP/skyviewfactor_uusi/svfs.zip',
                'INPUT_TDSM' : None,
                'INPUT_THEIGHT' : 25, 
                'LEAF_END' : 300,
                'LEAF_START' : 97,
                'ONLYGLOBAL' : True,
                'OUTPUT_DIR' : '/home/joona/Documents/UMEP/solweigtesti',
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
                'UTC' : 0,
                'WEIGHT' : 75 })

