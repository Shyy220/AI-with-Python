import cv2
import numpy as np

img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found.")
    exit()

def apply_filter(image, color):
    result = np.zeros_like(image)

    if color == 'r':
        result[:, :, 2] = image[:, :, 2]
    elif color == 'g':
        result[:, :, 1] = image[:, :, 1]
    elif color == 'b':
        result[:, :, 0] = image[:, :, 0]

    return result

def apply_sobel(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
    result = cv2.magnitude(sobel_x, sobel_y)
    return cv2.convertScaleAbs(result)

def apply_canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, 100, 200)

mode = 'original'

while True:
    if mode == 'original':
        result = img
    elif mode in ['r', 'g', 'b']:
        result = apply_filter(img, mode)
    elif mode == 's':
        result = apply_sobel(img)
    elif mode == 'c':
        result = apply_canny(img)

    cv2.imshow("Image Processing", result)

    key = cv2.waitKey(0) & 0xFF

    if key == ord('q'):
        break
    elif key in [ord('r'), ord('g'), ord('b'), ord('s'), ord('c')]:
        mode = chr(key)
    else:
        print("Invalid key! Press r, g, b, s, c or q.")

cv2.destroyAllWindows()