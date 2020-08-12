import cv2
import numpy as np
# from binary_image_helpers import various_binary_images
# from contour_helper import inspect_all_contours

image = cv2.imread('./images/many_m_n_m.jpg')
cv2.imshow('input', image)
cv2.waitKey(0)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('output', gray)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(gray, (11,11), None)
cv2.imshow('output', blurred)
cv2.waitKey(0)

# various_binary_images(blurred, True, 2500)

thresh_adapt = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
cv2.imshow('output', thresh_adapt)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(thresh_adapt, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

# inspect_all_contours(image, contours, waitPeriod=100)

contours_image = image.copy()
cv2.drawContours(contours_image, contours, -1, (0,255,0), -1)
cv2.imshow('output', contours_image)
cv2.waitKey(0)

selected_contours = []

for (index, cnt) in enumerate(contours):
    area = cv2.contourArea(cnt)
    print(index, ": ", area)
    if area > 1000:
        selected_contours.append(cnt)

contours_image = image.copy()
cv2.drawContours(contours_image, selected_contours, -1, (0,255,0), 10)
cv2.putText(contours_image, f"Candy Count: {len(selected_contours)}", (30,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
cv2.imshow('output', contours_image)
cv2.waitKey(0)

print(len(selected_contours))