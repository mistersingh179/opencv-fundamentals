# Basics of a video

Video is nothing but lots of images coming in at a speed normally higher than 24 per second.

### Reading from video file

```
vs = cv2.VideoCapture('./images/video.mp4')
original_fps = int(vs.get(cv2.CAP_PROP_FPS))
orignal_width = int(vs.get(cv2.CAP_PROP_FRAME_WIDTH))
orignal_height = int(vs.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    grabbed, frame = vs.read()
    if grabbed == False:
        break
    else:
        print(grabbed, frame)
        writer.write(frame)
```

Here we are getting the image by calling `vs.read()`. This image is just a normal image. Its a matrix in BGR format. All knowldge of image processing applies to it.

### Writing to a video file

```
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
writer = cv2.VideoWriter("./output.avi", fourcc, original_fps, (orignal_width, orignal_height), True)
while True:
    frame = vs.read()[1]
    writer.write(frame)

vs.release()
writer.release()
```

**Note**: regardless of how fast your write the frame, the file is build based on the FPS you set up in the writer. So there is now need to slow down the writing. This is different than if you were showing this in a window where your speed of sending data to the window will control the FPS in the window.

```
while True:
    frame = vs.read()[1]
    cv2.imshow('frame', frame)
    cv2.waitKey(10)
```

Above adds 10ms delay so the frame window will be playing at 100FPS provided we can read that fast. Normally this showing in video frame is only for debugging and thus the exact FPS being off is not an issue.

For `fourcc` codec we have: `mjpg`, `divx` and `h264` and for file extensions we have `avi`, `mp4` and `mov`.

Note: It takes data in BGR, so just convert to that format before writing. Also the dimensions need to match what were specified. The speed of writing is irrelevant as FPS goes by what has been specified

### Reading from camera

Just like how we read from file, we call `cv2.VideoCapture` but instead of passing in file path we pass in camera device number.

```
import cv2
import time

stream = cv2.VideoCapture(0)
time.sleep(2.0)

x = stream.read()

print(x[0]) # true
print(x[1]) # image numpy
print(x[1].shape) # 720, 1080, 3

cv2.imshow('output', x[1])
cv2.waitKey(0)
cv2.destroyAllWindows()
vs.release()
```

## Project

Lets read from file and write time elapsed to it.

This requires using `cv2.putText`.  Other similar commands are `rectangle`,  `circle`,  `line` and  `copyMakeBorder`.

