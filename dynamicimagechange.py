import cv2

camera = cv2.VideoCapture(0)

while True:

    ret, frame = camera.read()

    if not ret:
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        result = frame

    elif key == ord('2'):
        result = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif key == ord('3'):
        result = frame.copy()
        result[:, :, 1] = 0
        result[:, :, 2] = 0

    elif key == ord('4'):
        gray = cv2.cvtColor(frame, cv2.COLOR_BG2GRAY)
        result = cv2.Canny(gray, 100, 200)

    else:
        result = frame

    cv2.imshow("My Camera Filters", result)

    if key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()