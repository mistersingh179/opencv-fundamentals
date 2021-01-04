import cv2
from demo3 import employee_finder

image = cv2.imread('../Chapter_5_Color_Thresholding/images/carrom_board2.jpg')
cv2.imshow('input', image)
cv2.waitKey(-1)

image = employee_finder(image)

cv2.imshow('output', image)
cv2.waitKey(-1)