import cv2

cam = cv2.VideoCapture(0)

face_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

face = cv2.CascadeClassifier(face_path)

if face.empty():

   print("Face detection model not loaded!")

exit()

print("Face detection model loaded successfully!")

while True:
    ret, frame = cam.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame(x, y),(x+w, y+h), (0,255,0),2)

    cv2.putText(frame, "Faces: " + str(len(faces)),
                (20,40), cv2.FONT_HERSHEY_SIMPLX, 1, (0, 0, 255), 2)

    cv2.imshow("Face Tracking", frame)

    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()



