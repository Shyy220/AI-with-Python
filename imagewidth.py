
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("cat.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

height, width, _ = img.shape

plt.imshow(img)

plt.annotate(
    "",
    xy=(width, height//2),
    xytext=(0, height//2),
    arrowprops=dict(arrowstyle="<->", color="red")
)

plt.title("Image Width: " + str(width) + " Pixels")
plt.axis("off")
plt.show()
