import cv2
import time

vs = cv2.VideoCapture('./images/video.mp4')

original_fps = int(vs.get(cv2.CAP_PROP_FPS))
orignal_width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
orignal_height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f'original_fps: {original_fps}, orignal_width: {orignal_width}, orignal_height: {orignal_height}')

time.sleep(2)

fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
writer = cv2.VideoWriter("./images/output_video.avi", fourcc, original_fps, (orignal_width, orignal_height), True)

while True:
  grabbed, frame = vs.read()
  if grabbed == False:
    break
  else:
    writer.write(frame)

vs.release()
writer.release()