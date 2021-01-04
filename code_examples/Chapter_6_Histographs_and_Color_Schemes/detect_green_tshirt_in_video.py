from demo3 import employee_finder
import cv2
import time

vs = cv2.VideoCapture('./images/green_tshirt_on_floor.mov')

# vs = cv2.VideoCapture(0)
# time.sleep(2.0)

while True:
    # time.sleep(1)
    grabbed, frame = vs.read()
    if grabbed == False:
        break
    else:
        cv2.imshow('original', frame)
        cv2.waitKey(1)
        image = employee_finder(frame)
        cv2.imshow('output', frame)
        cv2.waitKey(1)
        # print(frame)


vs.release()
cv2.destroyAllWindows()

