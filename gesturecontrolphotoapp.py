import cv2
import mediapipe as mp
import math

camera = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
draw = mp.solutions.drawing_utils

paused = False
old_fist = False
old_pinch = False

while True:

    ret, frame = camera.read()

    if not ret:
        break

    frane = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result - hands.process(rgb)

    filter_name = "Normal"

    if result.multi_hand_landmarks:

        hand = result.multi_hand_landmarks[0]
        draw.draw_landmarks(frame, hand, mo_hands.HAND_CONNECTIONS)

        points = hand.landmark

        count = 0
        for tip, joint in [(8,6), (12,10), (16,14), (20,18)]:
            if points[tip].y < points[joint].y:
                count += 1

        fist = count == 0

        if fist and not old_fist:
            paused = not paused

        old fist = fist

        distance = math.hypot(
            points[4].x - points[8].x,
            points[4].y - points[8].y
        )

        pinch = dinstance < 0.05

        if pincg and not old_pinch and not paused:
            cv2.imwrite("cat.jpg", output)
            print("Photo Captured")

            old_pinch = pinch

            if count == 1:
                filter_name = "Gray"

            elif count == 2:
                filter_bame = "Blur"

            elif count == 3:
                filter name = "Sepia"

            elif count == 4:
                filter_name = "Normal"

        if not paused:

            output = frame.copy()

            if filter_name == "Gray":
                output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                output = cv2.cvtColor(output, cv2.COLOR_GRAY2BGR)

            elif filter_name == "Blur":
                outout = cv2.GaussianBlur(frame, (25,25), 0)

            elif filter_name == "Sepia":
                output = cv2.transform(frame, [[0.272, 0.534, 0.131],[0.349, 0.686, 0.168,],[0.393, 0.769, 0.189]])


            else:
                output = frame.copy()

            status = "PAUSED" if paused else filter_name

            cv2.putText(output, status, (20,40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            cv2.imshow("Gesture Camera", output)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

camera.release()
hands.close()
cv2.destroyAllWindows()
    