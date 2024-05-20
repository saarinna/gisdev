# GIS Development Project

# Installation Guide

## Prerequisites
- Linux
- QGIS
- Anaconda

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

## Scripts

The application has scripts that use PyQGIS and UMEP processing plugin

1. **crop.py**
   - The script takes the user defined polygon, reprojects it, and crops the digital elevation model and digital surface model.

2. **skyviewfactor.py**
   - The script creates skyviewfactor TIF files and shadowmats for input into the SOLWEIG analysis.

3. **solweig.py**
   - This script runs the SOLWEIG analysis, using the outputs from the previous scripts as input.
