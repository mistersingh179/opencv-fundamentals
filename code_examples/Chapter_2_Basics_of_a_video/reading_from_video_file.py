import cv2
vs = cv2.VideoCapture('./images/video.mp4')

original_fps = int(vs.get(cv2.CAP_PROP_FPS))
orignal_width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
orignal_height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f'original_fps: {original_fps}, orignal_width: {orignal_width}, orignal_height: {orignal_height}')

cv2.namedWindow("output")
cv2.waitKey(0)
while True:
    grabbed, frame = vs.read()
    if grabbed == False:
        break
    else:
        frame[150,10:50] = (255, 255, 255 )
        print(grabbed, frame)
        cv2.imshow('output', frame)
        cv2.waitKey(1)