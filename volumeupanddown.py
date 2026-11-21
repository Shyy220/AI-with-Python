import cv2
import mediapipe as mp
import pyautogui
import math

camera = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands()

while True:

    success, frame = camera.read()

    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        thumb = hand.landmark[4]
        finger = hand.landmark[8]

        distance = math.hypot(
            thumb.x - finger.x,
            thumb.y - finger.y
        )

        if distance < 0.05:
            pyautogui.press("volumedown")
            print("Volume Down")

        elif distance > 0.20:
            pyautogui.press("volumeup")
            print("Volume Up")

    cv2.imshow("Volume Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
        
