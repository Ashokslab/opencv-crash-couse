# Image Sharpening Script
# This script reads an image ('a1.jpg'), applies a sharpening filter using a convolution kernel,
# and displays both the original and sharpened images.

import cv2
import numpy as np

img = cv2.imread('a1.jpg')

sharp = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharpened = cv2.filter2D(img, -5, sharp)

cv2.imshow("ols", img)
cv2.imshow("new", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()