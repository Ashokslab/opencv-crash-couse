import cv2 
 
image = cv2.imread('ir.jpg')

if image is None:
    print("error")
else:
    print("success")
    pt1 = (50,100)
    pt2 = (50, 1050)
    color = (255, 0, 0)
    tkns = 20

    fin = cv2.line(image, pt1, pt2, color,thickness=10)
    cv2.imshow("new", fin)
    cv2.waitKey()
    cv2.destroyAllWindows()