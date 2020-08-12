import cv2
import numpy as np

a = np.random.rand(10000)
b = a * 255
c = b.astype('uint8')
d = c.reshape(100,100)
cv2.imshow('output', d); cv2.waitKey(0);
cv2.imwrite('./random_grayscale.png', d)