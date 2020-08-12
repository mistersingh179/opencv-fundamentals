from detect_green_tshirt import detect_tshirt
import cv2
import time

vs = cv2.VideoCapture('./images/green_tshirt_on_floor.mov')
# vs = cv2.VideoCapture(0)
# time.sleep(2.0)
cv2.namedWindow('output')
cv2.namedWindow('original')
cv2.waitKey(0)

while True:
    # time.sleep(1)
    grabbed, frame = vs.read()
    if grabbed == False:
        break
    else:
        cv2.imshow('original', frame);cv2.waitKey(1)
        ans = detect_tshirt(frame)
        print(f'answer is: {ans}')
        if ans == True:
            print('writing detected')
            cv2.putText(frame, "TSHIRT Detected", (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)
        else:
            print('writing nothing')
            cv2.putText(frame, "Nothing!", (45, 45), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)
        cv2.imshow('output', frame);cv2.waitKey(1)
        # print(frame)


vs.release()
cv2.destroyAllWindows()

