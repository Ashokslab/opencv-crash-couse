# import cv2

# image = cv2.imread('ir.jpg')

# if image is not None:
   
#    print("succes")
#    (h,w) = image.shape[:2]
#    center = [h//2 , w//2]
#    M = cv2.getRotationMatrix2D(center , 45 , 1.5)
#    rotation = cv2.warpAffine(image, M,(w, h))
  
#    cv2.imshow("new", rotation)
#    cv2.waitKey(0)
#    cv2.destroyAllWindows()
# else:
#    print("error")
    

#flip 

import cv2

image = cv2.imread('ir.jpg')

if image is not None:
   
   print("succes")
   flipH = cv2.flip(image , 1)
   flipV = cv2.flip(image , 0)
   flipB = cv2.flip(image , -1)
  
   cv2.imshow("horz", flipH)
   cv2.imshow("vertcl", flipV)
   cv2.imshow("both", flipB)
   cv2.waitKey(0)
   cv2.destroyAllWindows

else:
   print("error")