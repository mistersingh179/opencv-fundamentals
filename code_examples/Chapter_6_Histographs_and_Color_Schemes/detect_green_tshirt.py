import cv2
import imutils

def detect_tshirt(image):

    # HSV by using interactiveColorDetect.py
    lower_range_in_lab = (0, 85, 115)
    higher_range_in_lab = (255, 110, 135)

    labimage = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    blurred_lab_image = cv2.GaussianBlur(labimage, (5, 5), None)
    thresh = cv2.inRange(blurred_lab_image, lower_range_in_lab, higher_range_in_lab)
    # thresh = cv2.erode(thresh, None, iterations=5)
    # thresh = cv2.dilate(thresh, None, iterations=5)

    # cv2.imshow('thresh', thresh)
    # cv2.waitKey(0)

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    print('contours length: ', len(cnts))
    if(len(cnts) == 0):
        print('nothing found')
        return False
    else:
        biggest_contour = max(cnts, key=cv2.contourArea)
        biggest_contour_area = cv2.contourArea(biggest_contour)
        print(' biggest_contour_area: ',  biggest_contour_area)
        if(biggest_contour_area > 100):
            print('detected a contour with area bigger than 100px')
            cv2.drawContours(image, cnts, -1, (0, 200, 200), -1)
            # cv2.drawContours(image, [biggest_contour], -1, (0, 255, 255), -1)
            return True
        else:
            print('nothing big enough')
            return False

if __name__ == '__main__':
    image = cv2.imread('./images/green_tshirt4.jpg')
    cv2.imshow('foo', image)
    cv2.waitKey(0)
    ans = detect_tshirt(image)
    print(f'answer is: {ans}')
    cv2.imshow('foo', image)
    cv2.waitKey(0)
else:
    print(f'ran from: {__name__}')






