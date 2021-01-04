import cv2
import numpy as np
import random

# image = cv2.imread('./images/monalisa.jpg')
# print(image)
# cv2.imshow('output', image)
# cv2.waitKey(-1)
#
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# print(gray)
# cv2.imshow('output', gray)
# cv2.waitKey(-1)

# image = np.zeros((100, 100, 3), dtype='uint8')
# print(image)
#
# for row in range(100):
#   for col in range(100):
#     for channel in range(3):
#       number = int(random.random() * 255)
#       image[row][col][channel] = number
#
# cv2.imshow('output', image)
# cv2.waitKey(-1)

# image = cv2.imread('./images/monalisa.jpg')
# cv2.imshow('input', image)
# cv2.waitKey(-1)
#
# row = image[1000]
# print(row)
#
# message = "Send the infantry. We are ready! " * 3
# # print(message )
#
# column_count = 0
# for character in message:
#   # print(character, ord(character))
#   image[1000][column_count] = [ord(character), ord(character), ord(character)]
#   column_count = column_count + 1
#
# print(image[1000])
#
# cv2.imshow('output', image)
# cv2.waitKey(-1)
#
# cv2.imwrite('./our_little_secret.png', image)

image = cv2.imread('./our_little_secret.png')
cv2.imshow('input', image)
cv2.waitKey(-1)

message = ''
print(image[1000])
for col in image[1000]:
  message = message + chr(col[0])

print(message)