import cv2
import matplotlib.pyplot as plt

image = cv2.imread("cat.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

cropped_image = image[50:250, 50:250]

bright_image = cv2.convertScaleAbs(image, alpha=1, beta=50)

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 2, 2)
plt.imshow(rotated_image)
plt.title("Rotated Image")
plt.axis("off")

plt.subplot(2, 2, 3)
plt.imshow(cropped_image)
plt.title("Cropped Image")
plt.axis("off")

plt.subplot(2, 2, 4)
plt.imshow(bright_image)
plt.title("Brightness Adjusted Image")
plt.axis("off")

plt.tight_layout()
plt.show()