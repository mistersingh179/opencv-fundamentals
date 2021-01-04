import cv2
from matplotlib import pyplot as plt
import numpy as np
# from binary_image_helpers import various_binary_images

image = cv2.imread('./images/foo2.jpg')
cv2.imshow('input', image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (21,21), None)
cv2.imshow('output', blurred)
cv2.waitKey(0)
# various_binary_images(blurred)

ret, thresh_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

M = np.ones((11,11))
thresh_otsu = cv2.erode(thresh_otsu, M, iterations=1)
# thresh_otsu = cv2.dilate(thresh_otsu, None, iterations=2)

cv2.imshow('output', thresh_otsu)
cv2.waitKey(0)

cnts, hierarchy = cv2.findContours(thresh_otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contours_image = image.copy()
cv2.drawContours(contours_image, cnts, -1, (255,0,0), 1)
cv2.imshow('output', contours_image)
cv2.waitKey(0)

the_contour = max(cnts, key=cv2.contourArea)

contours_image = image.copy()
cv2.drawContours(contours_image, [the_contour], -1, (255,0,0), 1)
cv2.imshow('output', contours_image)
cv2.waitKey(0)

mask = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')
cv2.drawContours(mask, [the_contour], -1, (255, 255 ,255), -1)
cv2.imshow('mask', mask)
cv2.waitKey(0)

print(mask.shape)
print(image.shape)
tshirt_image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('tshirt_image', tshirt_image)
cv2.waitKey(0)

hist = cv2.calcHist([blurred], [0], None, [255], [0,255])
plt.figure('grayscale blurred image histogram')
plt.xlabel('bins'); plt.ylabel('# of pixels');
plt.plot(hist)
plt.show()

blue_hist = cv2.calcHist([image], [0], None, [256], [0,256])
green_hist = cv2.calcHist([image], [1], None, [256], [0,256])
red_hist = cv2.calcHist([image], [2], None, [256], [0,256])

plt.figure()
plt.title('BGR Color Histogram')
plt.xlabel('bins'); plt.ylabel('# of pixels');
plt.xlim([0,256])

plt.plot(blue_hist, color='b')
plt.plot(green_hist, color='g')
plt.plot(red_hist, color='r')

plt.show()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue_hist = cv2.calcHist([hsv_image], [0], None, [256], [0,256])
saturation_hist = cv2.calcHist([hsv_image], [1], None, [256], [0,256])
value_hist = cv2.calcHist([hsv_image], [2], None, [256], [0,256])

plt.figure()
plt.title('HSR Color Histogram without mask')
plt.xlabel('bins'); plt.ylabel('# of pixels');
plt.xlim([0,256])

plt.plot(hue_hist, color='b')
plt.plot(saturation_hist, color='g')
plt.plot(value_hist, color='r')

plt.show()

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue_hist = cv2.calcHist([hsv_image], [0], mask, [256], [0,256])
saturation_hist = cv2.calcHist([hsv_image], [1], mask, [256], [0,256])
value_hist = cv2.calcHist([hsv_image], [2], mask, [256], [0,256])

plt.figure()
plt.title('HSV Color Histogram with mask')
plt.xlabel('bins'); plt.ylabel('# of pixels');
plt.xticks(np.arange(0, 256, 25))
# plt.xlim([0,256])

plt.plot(hue_hist, color='b', label='Hue')
plt.plot(saturation_hist, color='g', label='Saturation')
plt.plot(value_hist, color='r', label='Value')

plt.legend()
plt.show()

lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
l_hist = cv2.calcHist([lab_image], [0], mask, [256], [0,256])
a_hist = cv2.calcHist([lab_image], [1], mask, [256], [0,256])
b_hist = cv2.calcHist([lab_image], [2], mask, [256], [0,256])

plt.figure()
plt.title('LAB Color Histogram with mask')
plt.xlabel('bins'); plt.ylabel('# of pixels');
plt.xticks(np.arange(0, 256, 25))
# plt.xlim([0,256])

plt.plot(l_hist, color='b', label='L')
plt.plot(a_hist, color='g', label='A')
plt.plot(b_hist, color='r', label='B')

plt.legend()
plt.show()

exit(0)

print('after exiting')