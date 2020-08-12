import numpy as np
import random
import cv2

image = np.zeros((100,100,3), dtype='uint8')

for i in range(100):
    for j in range(100):
        for k in range(3):
            random_number = int(random.random() * 255)
            print(i, j, k, random_number)
            image[i][j][k] = random_number

print(image)
cv2.imshow('output', image);
cv2.waitKey(0);
cv2.imwrite('./random_color_image.png', image)