import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('image.jpg')
r_gain = 1.0
g_gain = 1.0
b_gain = 1.0
filter_type = 0

while True:
    b, g, r = cv2.split(image)
    
    if filter_type == 1:
        b = cv2.bitwise_not(b)
        g = cv2.bitwise_not(g)
        r = cv2.bitwise_not(r)
    elif filter_type == 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        b = gray
        g = gray
        r = gray

    b = np.clip(b * b_gain, 0, 255).astype(np.uint8)
    g = np.clip(g * g_gain, 0, 255).astype(np.uint8)
    r = np.clip(r * r_gain, 0, 255).astype(np.uint8)

    modified = cv2.merge([b, g, r])
    cv2.imshow('Image Editor', modified)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        r_gain += 0.1
    elif key == ord('R'):
        r_gain = max(0.0, r_gain - 0.1)
    elif key == ord('g'):
        g_gain += 0.1
    elif key == ord('G'):
        g_gain = max(0.0, g_gain - 0.1)
    elif key == ord('b'):
        b_gain += 0.1
    elif key == ord('B'):
        b_gain = max(0.0, b_gain - 0.1)
    elif key == ord('1'):
        filter_type = 0
    elif key == ord('2'):
        filter_type = 1
    elif key == ord('3'):
        filter_type = 2
    elif key == ord('s'):
        filename = input('Enter filename to save: ')
        cv2.imwrite(filename, modified)
        plt.imshow(cv2.cvtColor(modified, cv2.COLOR_BGR2RGB))
        plt.axis('off')
        plt.savefig('matplotlib_' + filename)

cv2.destroyAllWindows()