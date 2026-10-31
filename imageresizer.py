
import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully!")
    cv2.imshow("Original Image", img)

    small = cv2.resize(img, (200, 200))
    medium = cv2.resize(img, (400, 400))
    large = cv2.resize(img, (600, 600))

    cv2.imshow("Small Image", small)
    cv2.imshow("Medium Image", medium)
    cv2.imshow("Large Image", large)


    cv2.imwrite("small_image.jpg", small)
    cv2.imwrite("medium_image.jpg", medium)
    cv2.imwrite("large_image.jpg", large)

    print("All resized images saved successfully!")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
