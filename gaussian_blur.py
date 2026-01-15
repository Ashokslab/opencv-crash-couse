# Gaussian Blur Script
# This script reads an image ('ir.jpg'), applies Gaussian blur to reduce noise,
# saves the blurred image as 'a1.jpg', and displays both original and blurred images.

import cv2

img = cv2.imread('ir.jpg')

new = cv2.GaussianBlur(img, (7,7), 4)
cv2.imwrite("a1.jpg", new)
cv2.imshow("hi", img)
cv2.imshow("ols", new)

cv2.waitKey(0)
cv2.destroyAllWindows()

