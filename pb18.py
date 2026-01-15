import cv2

img = cv2.imread("hi.webp", cv2.IMREAD_GRAYSCALE)

ret, sharpened = cv2.threshold(img, 150, 225,  cv2.THRESH_BINARY)




cv2.imshow("ols", img)
cv2.imshow("new", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()