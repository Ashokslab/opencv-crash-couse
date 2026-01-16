# Webcam Recording Script
# This script captures video from the default webcam, records it to 'my_video.mp4',
# and displays the live feed. Press 'q' to stop recording.

import cv2 

cam = cv2.VideoCapture(0)

framew = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frameh = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

codec = cv2.VideoWriter_fourcc(*'mp4v')
recoder = cv2.VideoWriter("my_video.mp4", codec, 30, (framew, frameh))

while True:
    success, image = cam.read()
    
    if not success:
        break

    recoder.write(image)
    cv2.imshow("live", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exit pressed")
        break
cam.release()
recoder.release()

cv2.destroyAllWindows()
