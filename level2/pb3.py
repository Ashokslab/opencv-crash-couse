import cv2 
face_c = cv2.CascadeClassifier("leve2\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("D:\ASHOK\python classes\open cv\leve2\haarcascade_eye.xml")
smile_cas = cv2.CascadeClassifier("D:\ASHOK\python classes\open cv\leve2\haarcascade_smile.xml")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        d_face = face_c.detectMultiScale(gray, 1.1, 6)
 
        for (x,y,w,h) in d_face:
              cv2.rectangle(frame, (x,y), (x+w, y+h), (2, 220,130), 2)

              roig = gray[y:y+h, x:x+w]
              roic = frame[y:y+h, x:x+w]

              
              eyes = eye_cascade.detectMultiScale(roig, 2.0, 10)

              if len(eyes) > 0:
                   cv2.putText(frame, "eyes",(x , y-30),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
                   
              
              smile = smile_cas.detectMultiScale(roig, 2.0, 20)
              if len(smile) >0:
                   cv2.putText(frame,"smile",(x , y+30),cv2.FONT_HERSHEY_COMPLEX,0.6,(0,255,0),2)
        cv2.imshow("web", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
         print("exit")
         break
cap.release()
cv2.destroyAllWindows()     