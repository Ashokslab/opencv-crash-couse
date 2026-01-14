import cv2

image = cv2.imread('ir.jpg')

if image is  None:
    print("error")
else:
    print("succes")
    crop = image[100:200, 50:150]
    cv2.imshow("old" ,image)
    cv2.imshow("new" ,crop)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    