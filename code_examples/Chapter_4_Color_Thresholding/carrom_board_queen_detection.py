import cv2

def find_queen(image):
    blurred = cv2.GaussianBlur(image, (3,3), None)
    cv2.imshow('output', blurred)
    cv2.waitKey(1000)

    lab_image = cv2.cvtColor(blurred, cv2.COLOR_BGR2LAB)

    lower_lab = (0, 165, 145)
    upper_lab = (255, 175, 155)

    binary = cv2.inRange(lab_image, lower_lab, upper_lab )
    cv2.imshow('output', binary)
    cv2.waitKey(1000)

    contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    the_contour = max(contours, key=cv2.contourArea)
    the_contour_area = cv2.contourArea(the_contour)
    if the_contour_area < 25:
        print('queen not found')
        rectangle_image = image.copy()
        cv2.putText(rectangle_image, "Queen Not Found", (30, 30), cv2.FONT_HERSHEY_COMPLEX, .5, (0, 255, 0), 1)
        cv2.imshow('output', rectangle_image)
        cv2.waitKey(1000)

    else:
        contours_image = image.copy()
        cv2.drawContours(contours_image, contours, -1, (0, 255, 0), 2)
        cv2.imshow('output', contours_image)
        cv2.waitKey(1000)

        print(len(contours))

        circle_image = image.copy()
        (x, y), radius = cv2.minEnclosingCircle(the_contour)
        cv2.circle(circle_image, (int(x), int(y)), int(radius), (0,255,0), 2)
        cv2.imshow('output', circle_image)
        cv2.waitKey(1000)

        rectangle_image = image.copy()
        x, y, w, h = cv2.boundingRect(the_contour)
        cv2.rectangle(rectangle_image, (x,y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(rectangle_image, f"Queen Found at x: {x} and y: {y}", (30,30), cv2.FONT_HERSHEY_COMPLEX, .5, (0,255,0), 1)
        cv2.imshow('output', rectangle_image)
        cv2.waitKey(0)

if __name__ == '__main__':
    print('ran directly')

    image = cv2.imread('./images/carrom_board.jpg')
    cv2.imshow('output', image)
    cv2.waitKey(0)

    find_queen(image)






