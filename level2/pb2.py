import cv2 

img = cv2.imread("hi.webp")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 100,255, cv2.THRESH_BINARY)

countours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, countours, -1, (0,225,0), 3)
cv2.imshow("as", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
