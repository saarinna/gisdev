from qgis.core import QgsApplication
# Supply path to qgis install location
# Linux and Anaconda
# Need to install QGIS into an environment
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


# Set output paths
svftifoutput = '/home/user/Documents/django_server/data/output/SVF/SkyViewFactor.tif'
svfoutput = '/home/user/Documents/django_server/data/output/SVF/'
wallaspect_output = '/home/user/Documents/django_server/data/output/wallAspect.tif'
wallheight_output = '/home/user/Documents/django_server/data/output/wallHeight.tif'

# Calculates SVF from cropped data
# Set INPUT: directory as the same as cropdsmout path in crop.py
svf_outputs = processing.run("umep:Urban Geometry: Sky View Factor",
                             { 'ANISO' : True,
                              'INPUT_DSM' : '/home/user/Documents/django_server/data/output/croppedsm.tif',
                              'INPUT_TDSM' : None, 'INPUT_THEIGHT' : 25,
                              'OUTPUT_DIR' : svfoutput,
                              'OUTPUT_FILE' : svftifoutput,
                              'TRANS_VEG' : 3 })

# Calculates wall height and wall aspect from cropped data
# Set INPUT: directory as the same as cropdsmout path in crop.py
wallHeightRatioOutputs = processing.run("umep:Urban Geometry: Wall Height and Aspect",
                                        {'INPUT': '/home/user/Documents/django_server/data/output/croppedsm.tif',
                                         'INPUT_LIMIT': 3,
                                         'OUTPUT_HEIGHT': wallheight_output,
                                         'OUTPUT_ASPECT': wallaspect_output})
