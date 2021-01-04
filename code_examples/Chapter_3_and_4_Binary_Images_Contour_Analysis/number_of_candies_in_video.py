import cv2
import numpy as np
from number_of_candies_in_image import candy_count

vs = cv2.VideoCapture('./images/candies_on_table.mov')
original_fps = int(vs.get(cv2.CAP_PROP_FPS))
orignal_width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
orignal_height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(original_fps, orignal_width, orignal_height)

while True:
  grabbed, frame = vs.read()
  if grabbed == False:
    break
  else:
    count = candy_count(frame)
    print('count: ', count)
    cv2.putText(frame, f"count: {count}", (30,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255,0), 1)
    cv2.imshow('output', frame)
    cv2.waitKey(15)