import cv2
import numpy as np
import random

a = np.zeros((100, 100), dtype='uint8')
for i in range(100):
  for j in range(100):
    if random.random() >= 0.5:
      a[i][j] = 255

cv2.imshow('output', a)
cv2.waitKey(0)

cv2.imwrite('./random_binary_image.png', a)