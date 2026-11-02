
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("cat.jpg")

if img is None:
    print("Image not found")
    exit()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

blur = cv2.GaussianBlur(gray, (5, 5), 0)

canny = cv2.Canny(gray, 100, 200)

sobel = cv2.Sobel(gray, cv2.CV_64F, 1, 1, ksize=3)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)

result = np.hstack((gray, canny))

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(img)
plt.title("Original Image")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(blur, cmap="gray")
plt.title("Gaussian Blur")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(canny, cmap="gray")
plt.title("Canny Edge")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(sobel, cmap="gray")
plt.title("Sobel Edge")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(laplacian, cmap="gray")
plt.title("Laplacian Edge")
plt.axis("off")

plt.tight_layout()
plt.show()
