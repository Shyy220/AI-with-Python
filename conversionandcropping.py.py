import cv2

image = cv2.imread("example.jpg")

rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB Image", rgb)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayscaleImage", gray)

cropped = image[100:300, 200:400]
cv2.imshow("Cropped Image", cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()


