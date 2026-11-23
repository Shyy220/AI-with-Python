import cv2

img = cv2.imread("image.jpg")

rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

bright = cv2.convertScaleAbs(rotated, alpha=1.2, beta=30)

h, w = bright.shape[:2]

cropped = bright[int(h*0.15):int(h*0.85), int(w*0.15):int(w*0.85)]

cv2.imwrite("final_image.jpg", cropped)

cv2.imshow("Original Image", img)
cv2.imshow("Final Image", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()