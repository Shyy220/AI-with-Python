import cv2

img = cv2.imread("flower.jpg")

rotate = cv2.rotate(img, cv2.ROTATE_90_ClOCKWISE)

cv2.imsgow("Rotated Image", rotate)
cv2.WaitKey(0)
cv2.destroyAllWindows()