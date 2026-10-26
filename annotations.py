import cv2
import numpy as np

img = np.ones((300, 500, 3), dtype=np.uint8) * 255

cv2.putText(img,"Hello Student",(50, 100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.arrowedLine(img,(50,150),(250,150),(255,0,0),3)

cv2.imshow("Annotations", img)
cv2.waitKey(0)
cv2.destroyAllWindows()