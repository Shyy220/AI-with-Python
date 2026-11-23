import cv2
import mediapipe as mp
import math

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

x_prev = 0
y_prev = 0
color = (0, 255, 0)
size = 30
direction = "None"
points = []

while True:
    success, img = cap.read()

    if not success:
        print("Camera not detected!")
        break

    img = cv2.flip(img, 1)
    h, w, c = img.shape

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            index = landmarks[8]
            thumb = landmarks[4]
            thumb_ip = landmarks[3]
            middle = landmarks[12]
            ring = landmarks[16]
            pinky = landmarks[20]

            x = int(index.x * w)
            y = int(index.y * h)

            if x_prev != 0 and y_prev != 0:
                dx = x - x_prev
                dy = y - y_prev

                if abs(dx) > abs(dy) and abs(dx) > 15:
                    direction = "Right" if dx > 0 else "Left"

                elif abs(dy) > 15:
                    direction = "Down" if dy > 0 else "Up"

            x_prev = x
            y_prev = y

            cv2.circle(img, (x, y), size, color, -1)

            fingers_up = (
                landmarks[8].y < landmarks[6].y,
                landmarks[12].y < landmarks[10].y,
                landmarks[16].y < landmarks[14].y,
                landmarks[20].y < landmarks[18].y
            )

            if all(fingers_up) and thumb.y < thumb_ip.y:
                color = (255, 0, 0)
                cv2.putText(img, "Open Hand", (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            elif thumb.y < thumb_ip.y and not any(fingers_up):
                color = (0, 255, 0)
                cv2.putText(img, "Thumbs Up", (20, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            if fingers_up[0] and not any(fingers_up[1:]):
                points.append((x, y))

            else:
                points.clear()

            for i in range(1, len(points)):
                cv2.line(img, points[i - 1], points[i], color, 4)

            hand_width = abs(int(landmarks[5].x * w) - int(landmarks[17].x * w))
            size = max(15, min(80, hand_width // 2))

            cv2.putText(img, "Movement: " + direction, (20, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    else:
        x_prev = 0
        y_prev = 0
        direction = "None"

        cv2.putText(img, "No Hand Detected", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Hand Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
hands.close()
cv2.destroyAllWindows()