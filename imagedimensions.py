#Measuring Image Dimensions

import cv2
import numpy as np

img = np.ones((300, 500, 3), dtype=np.uint8) * 255

height, width, channels = img.shape

print("Height:", height)
print("Width:", width)
print("Channels:", channels)