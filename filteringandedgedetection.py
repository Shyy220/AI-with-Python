import cv2
img = cv2.imread("flowerr.jpeg")

if img is None:
    print("Image not there!")
else:
    print("Image downloaded successfully!")

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    average = cv2.blur(img, (5,5))

    gaussian = cv2.GaussianBlur(img, (5,5), 0)

    median = cv2.medianBlur(img, 5)

    edges = cv2.Canny(gray, 100,200)

    cv2.imshow("Original Image", img)

    cv2.imshow("Gray Scale Image", gray)

    cv2.imshow("Average Blur", average)

    cv2.imshow("Guassian Blur", gaussian)

    cv2.imshow("Edge Detector", edges)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

