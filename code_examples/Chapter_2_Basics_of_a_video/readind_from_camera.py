import cv2
import time

vs = cv2.VideoCapture(0)
time.sleep(2.0)

while True:
  x = vs.read()

  print(x[0]) # true
  print(x[1]) # image numpy
  print(x[1].shape) # 720, 1080, 3

  cv2.imshow('output', x[1])
  key = cv2.waitKey(1000)
  print(key)
  if ord('q') == key:
    break

cv2.destroyAllWindows()
vs.release()