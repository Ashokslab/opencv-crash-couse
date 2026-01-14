import cv2 
 
image = cv2.imread('ir.jpg')

if image is None:
    print("error")
else:
    print("success")
    center = (500,415)
    r = 40
    color = (0,255,0)

    circle = cv2.circle(image, center, r, color, thickness=2)

    cv2.imshow("circle",circle)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
