import cv2
import numpy as np
image = cv2.imread('./images/eggs_5_top_view_2.jpeg')
cv2.imshow('input', image)
cv2.waitKey(100)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('input', gray)
cv2.waitKey(100)

blurred = cv2.GaussianBlur(gray, (3,3), None)
cv2.imshow('input', blurred)
cv2.waitKey(100)

retVal, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print('retVal: ', retVal)
cv2.imshow('input', thresh)
cv2.waitKey(100)

thresh = cv2.erode(thresh, None, iterations=1)
cv2.imshow('input', thresh)
cv2.waitKey(100)

contours_image = image.copy()
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(contours_image, contours, -1, (0,255,0), 1)
cv2.imshow('input', contours_image)
cv2.waitKey(100)

box_contour = max(contours, key=cv2.contourArea)
contours_image = image.copy()
cv2.drawContours(contours_image, [box_contour], -1, (0,255,0), 1)
cv2.imshow('input', contours_image)
cv2.waitKey(100)

peri = cv2.arcLength(box_contour, True)
approx_cnt = cv2.approxPolyDP(box_contour, peri * .04, True)
contours_image = image.copy()
cv2.drawContours(contours_image, [approx_cnt], -1, (0,255,0), 1)
cv2.imshow('input', contours_image)
cv2.waitKey(100)

rectangle_image = image.copy()
x, y, w, h = cv2.boundingRect(approx_cnt)
cv2.rectangle(rectangle_image, (x,y), (x+w, y+h), (255,0,0), 1)
cv2.imshow('input', rectangle_image)
cv2.waitKey(100)

mask = np.zeros((image.shape[0], image.shape[1]), dtype='uint8')
cv2.imshow('output', mask)
cv2.waitKey(100)

# cv2.rectangle(mask, (x,y), (x+w, y+w), (255, 255, 255), -1)
# cv2.imshow('output', mask)
# cv2.waitKey(100)

my_hand_made_contour = np.array([[x,y], [x+w, y], [x+w, y+h], [x, y+h]])
cv2.drawContours(mask, [my_hand_made_contour], 0, (255,255,255), -1)
cv2.imshow('output', mask)
cv2.waitKey(100)

image = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow('output', image)
cv2.waitKey(100)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3,3), None)
cv2.imshow('output', blurred)
cv2.waitKey(100)

retVal, thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
cv2.imshow('output', thresh)
cv2.waitKey(100)

cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print('total number of possible eggs: ', len(cnts))

selected_contours = []
for index, cnt in enumerate(cnts):
  area = cv2.contourArea(cnt)
  print(f'index: {index} has area: {area}')
  if area > 500:
    selected_contours.append(cnt)

print('reduced number of selected contours size: ', len(selected_contours))
# cv2.drawContours(image, selected_contours, -1, (0,255,0), 1)
# cv2.imshow('output', image)
# cv2.waitKey(100)

circle_contours = []
circle_count = 0
for index, contour in enumerate(selected_contours):
  circle_check_image = image.copy()
  (x, y), radius = cv2.minEnclosingCircle(contour)
  x = int(x)
  y = int(y)
  circle_area = np.pi * radius * radius
  contour_area = cv2.contourArea(contour)
  radius = int(radius)
  print('looking at contour index: ', index, "circle attributes: ", x, y, radius)
  off_percentage = int(((circle_area - contour_area) / contour_area) * 100)
  if off_percentage <= 50:
    is_circle = True
    circle_contours.append(contour)
    circle_count = circle_count + 1
  else:
    is_circle = False

  print('circle_area: ', circle_area, ' and contour_area: ', contour_area, " off percentage: ", off_percentage)
  print('stats: ', index, is_circle, circle_count)

  cv2.drawContours(circle_check_image, [contour], -1, (0, 255, 0), 1)
  cv2.circle(circle_check_image, (x,y), radius, (255, 0, 0), 1)
  cv2.imshow('output', circle_check_image)
  cv2.waitKey(100)

cv2.drawContours(image, circle_contours, -1, (0,255,0), 2)
cv2.putText(image, f"Count of Eggs: {circle_count}", (30,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
cv2.imshow('output', image)
cv2.waitKey(-1)







