import cv2

image = cv2.imread('ir.jpg')

if image is None:
    print("error")
else:
    print("ir.jpg")

cv2.imshow("window tile", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
