import cv2
from datetime import datetime as dt

vs = cv2.VideoCapture(0)
original_fps = int(vs.get(cv2.CAP_PROP_FPS))
original_width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(original_fps, original_width, original_height)

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
writer = cv2.VideoWriter("./our_new_file.avi", fourcc, original_fps, (original_width, original_height), True)


start_time = dt.now()
print(start_time)

while True:
  grabbed, frame = vs.read()
  now_time = dt.now()
  if grabbed == False:
    print('reached end of video')
  else:
    delta_time = str((now_time - start_time).total_seconds())
    print(delta_time)
    message = delta_time + " seconds have elapsed"
    cv2.putText(frame, message, (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
    cv2.imshow('output', frame)
    cv2.waitKey(1)
    writer.write(frame)