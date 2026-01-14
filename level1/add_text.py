import cv2 
 
image = cv2.imread('ir.jpg')

if image is None:
    print("error")
else:
    print("success")
    fnt = cv2.FONT_HERSHEY_DUPLEX
    pt = (400,300)
    text = cv2.putText(image, "hello",pt, fnt ,1.5,(225,230,100),6,1)

    cv2.imshow("circle",text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()