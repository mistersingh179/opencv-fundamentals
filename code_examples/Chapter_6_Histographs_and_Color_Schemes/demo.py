import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('./images/IMG_0973.jpeg')
cv2.imshow('original', image)
cv2.waitKey(-1)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (21,21), None)

cv2.imshow('input', blurred)
cv2.waitKey(-1)

retVal, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
print('retVal: ', retVal)
print(thresh)
cv2.imshow('input', thresh)
cv2.waitKey(-1)

M = np.ones((11,11))
print(M)

thresh = cv2.erode(thresh, M, iterations=2)
cv2.imshow('input', thresh)
cv2.waitKey(-1)

thresh = cv2.dilate(thresh, M, iterations=2)
cv2.imshow('input', thresh)
cv2.waitKey(-1)

cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(cnts))

contours_image = image.copy()
cv2.drawContours(contours_image, cnts, -1, (255,0,0), 1)
cv2.imshow('input', contours_image)
cv2.waitKey(-1)


mask = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')
mask = cv2.drawContours(mask, cnts, 0, (255,255,255), -1)
cv2.imshow('mask', mask)
cv2.waitKey(-1)

tshirt_image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('output', tshirt_image)
cv2.waitKey(-1)

lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

blue_data = cv2.calcHist([lab_image], [0], mask, [256], [0,256])
green_data = cv2.calcHist([lab_image], [1], mask, [256], [0,256])
red_data = cv2.calcHist([lab_image], [2], mask, [256], [0,256])

plt.figure()
plt.title('Number of Pixels over Color Intensities')
plt.plot(blue_data, color='b', label='L')
plt.plot(green_data, color='g', label='A')
plt.plot(red_data, color='r', label='B')
plt.xticks(np.arange(0,256,25))
plt.legend()
plt.show()

