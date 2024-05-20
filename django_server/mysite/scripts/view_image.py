from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# Load the TIFF file using Pillow
img = Image.open('/home/joona/Desktop/UMEP_SERVER/Data/data_server/output/solweig/Tmrt_average.tif')

# Convert to NumPy array for visualization
img_array = np.array(img)

# Define the minimum and maximum values for the colormap scaling
vmin = 10  # Adjust these as per your data's requirements
vmax = 35

# Display the image with the specified value range and inverted colormap
plt.imshow(img_array, cmap='RdYlGn_r', vmin=vmin, vmax=vmax)
plt.colorbar(label='Intensity')  # Optionally add a color bar
plt.title('TIFF Image Display with Inverted Colormap (Pillow)')
plt.show()
