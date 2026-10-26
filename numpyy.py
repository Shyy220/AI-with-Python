import cv2
import numpy as np

img = np.ones((400,400,3), dtype=np.uint8) * 255

cv2.line(img, (20,20), (200,20), (255,0,0), 3)

cv2.rectangle(img, (50,60), (200,150), (0,255,0), 3)

cv2.circle(img, (280,100), 40, (0,0,255), 3)

cv2.imshow("Shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()