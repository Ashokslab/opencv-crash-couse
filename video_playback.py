# Video Playback Script
# This script reads a video file ('hi.mp4') and displays it frame by frame.
# Press 'q' to exit the playback.

import cv2

cap = cv2.VideoCapture('hi.mp4')

while True:
    ret, frame = cap.read()

    if not ret:
        print("error")
        break

    cv2.imshow("ashok", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print('exit')
        break
cap.release()
cv2.destroyAllWindows()
