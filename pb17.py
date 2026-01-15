import cv2

img = cv2.imread("hi.webp", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 10)
cv2.imshow("olg", img)
cv2.imshow("new", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()