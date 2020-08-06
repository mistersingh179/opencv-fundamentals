import cv2
import numpy as np
import os
print(os.getcwd())
image = cv2.imread('../images/salt-and-pepper-noise-mona-lisa.png')
print(image)
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# g_blurred = cv2.GaussianBlur(gray, (5,5), None)
# m_blurred = cv2.medianBlur(gray, 5)
# cv2.imshow('foo', np.hstack([gray, g_blurred, m_blurred]))
# cv2.waitKey(0)