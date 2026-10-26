import cv2
import numpy as np

img = np.ones((400, 500, 3), dtype=np.uint8) * 255

cv2.circle(img,(100, 120), 40, (0,0,255), 3)

cv2.rectangle(img, (200,80), (350,170), (0,255,0), 3)

cv2.line(img, (50,220), (400,220), (255,0,0), 3)

cv2.putText(img,"My first image",(80, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,0),2)

height, width, channels = img.shape
print("Height:", height)
print("Width:", width)
print("Channels:", channels)

cv2.imshow("My Poster", img)
cv2.waitKey(0)
cv2.destroyAllWindows()