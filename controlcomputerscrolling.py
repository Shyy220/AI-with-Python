import cv2
import mediapipe as mp
import pyautogui

camera = cv2.VideoCapture(0)

mp_hand = mp.solutions.hands
hand = mp_hand.Hands()

old_y = None

while True:
   

  _,img = camera.read()
  img = cv2.flip(img,1)

  rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  result = hand.process(rgb)

  if result.multi_hand_landmarks:
      for h in result.multi_hand_landmarks:
        y = h.landmark[8].y

        if old_y is not None:
           if y < old_y - 0.02:
            pyautogui.scroll(3)
            print("Scroll Up")

           elif y > old_y + 0.02:
             pyautogui.scroll(-3)
             print("Scroll Down")
        old_y = y

  cv2.imshow("Gesture Control", img)

  if cv2.waitKey(1) & 0xFF == ord('q'):
          break

camera.release()
cv2.destroyAllWindows()


