import numpy as np
import cv2

img = cv2.imread("cat.jpg")

if img is None:
    print("Image not there")
    exit()


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(img, (15,15),0)

edges = cv2.Canny(gray,100,200)

kernel = np.array([[0, -1, 0],
                   [-1, 5, -1], 
                   [0, -1, 0]
])

sharp=cv2.filter2D(img,-1,kernel)

cv2.imshow("Original Image",img

cv2.imshow("Gray Scale Image", gray)

cv2.imshow("Edge Detetion", edges)

cv2.imshow("Sharpen Image", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
