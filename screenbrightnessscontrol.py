import cv2
import mediapipe as mp
import screen_brightness_control as sbc

camera = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands()

while True:

    success, frame = camera.read()

    if not success:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(rgb)

    if result.multi_hand_landmarks:

        for hand in result.multi_hand_landmarks:

            finger = hand.landmark[8]

            if finger.y  < 0.3:
                sbc.set_brightness(100)
                print("Brightness Increased")

            elif finger.y > 0.7:
                sbc.set_brightness(30)
                print("Brightness Decreased")

    cv2.imshow("Brightness Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()