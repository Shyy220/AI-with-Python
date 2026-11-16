import cv2
import mediapipe as mp

camera = cv2.VideoCapture(0)

mp_hands = mp.solutuons.hands
hands = mp_hands.Hands(max_num_hands=1)

draw = mp.solutions.drawing_utils

while True:
    success, frame = camera.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        
        for hand in result.multi_hand_landmarks:

            points = hand.landmark
            count = 0

            fingers = [8, 12, 16, 20]
            joints = [6, 10, 14, 18]

            for tip, joint in zip(fingers, joints):
                if points[tip].y < points[joint].y:
                    count +=1

            if points[4].x < points[3].x:
                count += 1 

            if count == 0:
                message = "First"
            elif count == 1:
                message = "One Finger"
            elif count == 2:
                message = "Two Fingers"
            elif count == 5:
                message = "Open Palm"
            else:
                message = str(count) + "Fingers"

            cv2.putText(frame, message, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            draw.draw_landmarks(frame, hand,mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Gesture Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

        
