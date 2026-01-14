import cv2

image = cv2.imread("ir.jpg")

if image is not None:
    h , w , c = image.shape
    print(f"height{h}\n width{w} \n colour{c}")
else:
    print("error")