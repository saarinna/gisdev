from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


img = Image.open('/home/user/Documents/django_server/data/output/solweig/Tmrt_average.tif')


img_array = np.array(img)

# Change these values as needed
vmin = 10
vmax = 40

# Display the image with the chosen colormap
plt.imshow(img_array, cmap='RdYlGn_r', vmin=vmin, vmax=vmax)
plt.colorbar(label='Temperature (Celsius)')
plt.title('Mean Radian Temperature')
plt.show()
