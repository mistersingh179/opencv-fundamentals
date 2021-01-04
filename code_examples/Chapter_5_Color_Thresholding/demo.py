import cv2

image = cv2.imread('./images/carrom_board2.jpg')
cv2.imshow('output', image)
cv2.waitKey(-1)

blurred = cv2.GaussianBlur(image, (3,3), None)

lab_image = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

binary = cv2.inRange(lab_image, (0, 165, 145), (255, 175, 155))
cv2.imshow('output', binary)
cv2.waitKey(-1)

contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(len(contours))

the_biggest_contour_by_area = max(contours, key=cv2.contourArea)
biggest_area = cv2.contourArea(the_biggest_contour_by_area)

print(biggest_area)

if biggest_area < 25:
  print('queen not found')
  cv2.putText(image, 'No Queen Found', (30,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0))
else:
  # cv2.drawContours(image, [the_biggest_contour_by_area], 0, (0,255,0), 1)
  x, y, w, h = cv2.boundingRect(the_biggest_contour_by_area)
  (x,y), radius = cv2.minEnclosingCircle(the_biggest_contour_by_area)
  x = int(x)
  y = int(y)
  radius = int(radius)
  # cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 1)
  cv2.circle(image, (x,y), radius, (0,255,0), 2)
  cv2.putText(image, f'Yes Queen Found at {x},{y}', (30, 30), cv2.FONT_HERSHEY_COMPLEX, .5, (0, 255, 0))
  print('queen found')


cv2.imshow('output', image)
cv2.waitKey(-1)

