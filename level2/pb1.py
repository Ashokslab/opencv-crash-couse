import cv2
import numpy as np

img1 = np.zeros((300,300), dtype="uint8")
img2 = np.zeros((300,300), dtype = "uint8")

cv2.circle(img1, (150, 150), 100, 255,-1)

cv2.rectangle(img2, (100,100), (250,250), color=(255,0,0), thickness=-1)

bitand = cv2.bitwise_and(img1,img2)
bit_or = cv2.bitwise_or(img1,img2)
bit_not =cv2.bitwise_not(img1)
cv2.imwrite("leve2/crc.jpg", img1)
cv2.imwrite("leve2/rec.jpg", img2)
cv2.imshow("circle", img1)
cv2.imshow("hi", img2)
cv2.imshow("and",bitand)
cv2.imshow("or",bit_or)
cv2.imshow("as",bit_not)

cv2.waitKey()
cv2.destroyAllWindows()

