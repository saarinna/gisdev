from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


img = Image.open('/home/joona/Documents/django_server/data/output/solweig/Tmrt_average.tif')


img_array = np.array(img)

# Define the minimum and maximum values for the colormap scaling
vmin = 10
vmax = 35

# Display the image with the specified value range and inverted colormap
plt.imshow(img_array, cmap='RdYlGn_r', vmin=vmin, vmax=vmax)
plt.colorbar(label='Temperature')
plt.title('Temperature')
plt.show()
