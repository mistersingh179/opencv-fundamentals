import cv2
from datetime import datetime as dt

vs = cv2.VideoCapture('./images/A_large_rock_waterfall.mp4')

original_fps = int(vs.get(cv2.CAP_PROP_FPS))
orignal_width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
orignal_height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(original_fps, orignal_width, orignal_height)

output_width = orignal_width // 4
output_height = orignal_height // 4

print(output_width)
cv2.namedWindow('input',  cv2.WINDOW_NORMAL)
cv2.resizeWindow('input', output_width, output_height)
cv2.namedWindow('output',  cv2.WINDOW_NORMAL)
cv2.resizeWindow('output', output_width, output_height)
cv2.waitKey(0)

beginning_time = dt.now()

while True:
    grabbed, frame = vs.read()

    if grabbed == False:
        print('reached the end of the video')
        break
    frame = cv2.resize(frame, (output_width, output_height))
    cv2.imshow('input', frame)

    output_frame = frame.copy()
    delta_time = str((dt.now() - beginning_time).total_seconds())
    text = delta_time + " seconds elapsed"
    cv2.putText(output_frame, text, (10, 20), cv2.FONT_HERSHEY_COMPLEX, .6, (0, 255, 0), 1, cv2.LINE_AA)

    cv2.imshow('output', output_frame)
    keyCode = cv2.waitKey(40)
    if keyCode == ord('q'):
        print('q was pressed')
        break

cv2.destroyAllWindows()
vs.release()