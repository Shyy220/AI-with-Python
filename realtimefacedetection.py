import cv2
camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(

"haarcascade_frontalface_default.xml"

)

while True:

    success, frame = camera.read()

    gray = cv2.CvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiscale(gray,1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0),3)

    cv2.imshow("My face detector", frame)
    if cv2.waitkey(1) == ord('q'):
     break
camera.release()
cv2.DestroyAllWindows()
