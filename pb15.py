import cv2
 
img = cv2.imread('a1.jpg')

blr = cv2.medianBlur(img, 11)

cv2.imshow("ols", img)
cv2.imshow("new", blr)

cv2.waitKey(0)
cv2.destroyAllWindows()