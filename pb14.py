import cv2

img = cv2.imread('ir.jpg')

new = cv2.GaussianBlur(img, (7,7), 4)
cv2.imwrite("a1.jpg", new)
cv2.imshow("hi", img)
cv2.imshow("ols", new)

cv2.waitKey(0)
cv2.destroyAllWindows()

