import cv2

image = cv2.imread('ir.jpg')

if image is None:
    print("error")
else:
    print("succes")

    resize = cv2.resize(image, (300, 300),)

    cv2.imshow("old", image)
    cv2.imshow("new", resize)

    cv2.waitKey(0)
    cv2.destroyAllWindows()