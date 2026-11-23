import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

Hands = mp.solutions.hands
hands = Hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Webcam not accessible.")
    exit()

SCROLL_SPEED = 10
SCROLL_DELAY = 0.15

last_scroll = 0
prev_time = 0

while True:
    success, img = cap.read()

    if not success:
        print("Error: Could not read camera.")
        break

    img = cv2.flip(img, 1)
    h, w, c = img.shape

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    current_time = time.time()
    fps = 1 / (current_time - prev_time) if prev_time else 0
    prev_time = current_time

    gesture = "No Hand Detected"
    hand_side = "None"

    if result.multi_hand_landmarks and result.multi_handedness:
        for i, hand in enumerate(result.multi_hand_landmarks):

            label = result.multi_handedness[i].classification[0].label

            draw.draw_landmarks(img, hand, Hands.HAND_CONNECTIONS)

            lm = hand.landmark

            points = [(int(p.x * w), int(p.y * h)) for p in lm]

            x_values = [p[0] for p in points]
            y_values = [p[1] for p in points]

            x1 = max(0, min(x_values) - 20)
            y1 = max(0, min(y_values) - 20)
            x2 = min(w, max(x_values) + 20)
            y2 = min(h, max(y_values) + 20)

            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            fingers = [
                lm[8].y < lm[6].y,
                lm[12].y < lm[10].y,
                lm[16].y < lm[14].y,
                lm[20].y < lm[18].y
            ]

            thumb = (int(lm[4].x * w), int(lm[4].y * h))
            index = (int(lm[8].x * w), int(lm[8].y * h))

            cv2.circle(img, thumb, 8, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, index, 8, (255, 0, 0), cv2.FILLED)
            cv2.line(img, thumb, index, (0, 255, 0), 2)

            dist = np.hypot(index[0] - thumb[0], index[1] - thumb[1])

            speed = int(np.interp(dist, [30, 200], [1, SCROLL_SPEED]))

            if all(fingers):
                gesture = "Open Palm"
                hand_side = label

                if current_time - last_scroll > SCROLL_DELAY:
                    pyautogui.scroll(speed)
                    last_scroll = current_time

            elif not any(fingers):
                gesture = "Closed Fist"
                hand_side = label

                if current_time - last_scroll > SCROLL_DELAY:
                    pyautogui.scroll(-speed)
                    last_scroll = current_time

            else:
                gesture = "Other Gesture"
                hand_side = label

            cv2.putText(img, "Gesture: " + gesture, (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            cv2.putText(img, "Hand: " + hand_side, (20, 85),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

            cv2.putText(img, "Speed: " + str(speed), (20, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

    else:
        gesture = "No Hand Detected"

    cv2.putText(img, "FPS: " + str(int(fps)), (20, 160),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.putText(img, "Open Palm: Scroll Up", (20, h - 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.putText(img, "Closed Fist: Scroll Down", (20, h - 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Hand Gesture Scroll Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
hands.close()
cv2.destroyAllWindows()