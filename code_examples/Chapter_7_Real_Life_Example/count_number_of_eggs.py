import cv2
# from binary_image_helpers import various_binary_images
# from contour_helper import inspect_all_contours
import numpy as np
from imutils.perspective import four_point_transform

def number_of_eggs(frame, waitTime=500):
    image = frame.copy()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('processing', gray)
    cv2.waitKey(waitTime)

    blurred = cv2.GaussianBlur(gray, (3,3), None)
    cv2.imshow('processing', blurred)
    cv2.waitKey(waitTime)

    ret, binary_image = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    print('otsu says: ', ret)

    cv2.imshow('processing', binary_image)
    cv2.waitKey(waitTime)

    binary_image = cv2.erode(binary_image, None, iterations=1)

    contour_image = image.copy()
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    print('RETR_EXTERNAL: ', len(contours))
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 1)
    cv2.imshow('processing', contour_image)
    cv2.waitKey(waitTime)

    # contour_image = image.copy()
    # contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # print('RETR_TREE: ', len(contours))
    #
    # biggest_area = 0
    # biggest_index = -1
    # for index, cnt in enumerate(contours):
    #     area = cv2.contourArea(cnt)
    #     print('current biggest:', biggest_area, biggest_index)
    #     if area > biggest_area:
    #         biggest_area = area
    #         biggest_index = index
    #
    # print('showing the biggest contour index: ', biggest_index)
    # cv2.drawContours(contour_image, contours, biggest_index, (0, 255, 0), -1)
    # cv2.imshow('processing',  contour_image)
    # cv2.waitKey(waitTime)
    #
    # print(f'hierarchy info of {biggest_index}')
    # print(hierarchy[0][biggest_index])
    # first_child_in_box = hierarchy[0][biggest_index][2]
    # print('child index is: ', first_child_in_box)
    # print('child contour is: ', contours[first_child_in_box])
    #
    # all_contours_in_box = []
    # current_child = first_child_in_box
    # all_contours_in_box.append(contours[current_child])
    #
    # while hierarchy[0][current_child][0] != -1:
    #     current_child = hierarchy[0][current_child][0]
    #     print('sibbling child_index is: ', current_child)
    #     print('sibbling child_contour is: ', contours[current_child])
    #     all_contours_in_box.append(contours[current_child])
    #
    # print(all_contours_in_box)
    #
    # contour_image = image.copy()
    # cv2.drawContours(contour_image, all_contours_in_box, -1, (0, 255, 0), 3)
    # cv2.imshow('processing', contour_image)
    # cv2.waitKey(waitTime)

    # print('number of contours in the box: ', len(all_contours_in_box))

    box_contour = max(contours, key=cv2.contourArea)
    contour_image = image.copy()
    cv2.drawContours(contour_image, [box_contour], -1, (0, 255, 0), 3)
    cv2.imshow('processing', contour_image)
    cv2.waitKey(waitTime)

    peri = cv2.arcLength(box_contour, True)
    approx_cnt = cv2.approxPolyDP(box_contour, peri * 0.04, True)
    contour_image = image.copy()
    cv2.drawContours(contour_image, [approx_cnt], -1, (0, 255, 0), 3)
    cv2.imshow('processing', contour_image)
    cv2.waitKey(waitTime)

    rectangle_image = image.copy()
    x, y, w, h = cv2.boundingRect(approx_cnt)
    cv2.rectangle(rectangle_image, (x,y), (x+w, y+h), (0,255,0), 3)
    cv2.imshow('processing', rectangle_image)
    cv2.waitKey(waitTime)

    cropped_image = image[y:y+h,x:x+w]
    cv2.imshow('processing', cropped_image)
    cv2.waitKey(waitTime)

    # warped_image = image.copy()
    # warped_image = four_point_transform(image, approx_cnt.reshape(4, 2))
    # print('warped: ', warped_image)
    # cv2.imshow('processing', warped_image)
    # cv2.waitKey(waitTime)

    hullContour = cv2.convexHull(box_contour)
    contour_image = image.copy()
    cv2.drawContours(contour_image, [hullContour], -1, (0, 255, 0), 3)
    cv2.imshow('processing', contour_image)
    cv2.waitKey(waitTime)

    box_mask = np.zeros(image.shape[0:2], dtype='uint8')
    cv2.imshow('processing', box_mask)
    cv2.waitKey(waitTime)

    # cv2.drawContours(box_mask, [approx_cnt], -1, (255, 255, 255), -1)
    pts1 = np.array([[x, y], [x + w, y], [x + w, y + h], [x, y + h]])
    cv2.drawContours(box_mask, [pts1], -1, (255, 255, 255), -1)
    cv2.imshow('processing', box_mask)
    cv2.waitKey(waitTime)

    image = cv2.bitwise_and(image, image, mask=box_mask)
    cv2.imshow('processing', image)
    cv2.waitKey(waitTime)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('processing', gray)
    cv2.waitKey(waitTime)

    blurred = cv2.GaussianBlur(gray, (3,3), None)
    cv2.imshow('processing', blurred)
    cv2.waitKey(waitTime)

    retVal, binary_image = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)
    various_binary_images(blurred, waitPeriod=2000, windowName='binary images')

    cv2.imshow('processing', binary_image)
    cv2.waitKey(waitTime)

    contour_image = image.copy()
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))

    selected_contours = []
    for index, cnt in enumerate(contours):
        print(index, cv2.contourArea(cnt))
        if cv2.contourArea(cnt) > 500:
            selected_contours.append(cnt)
        else:
            print('skipping')

    print('selected contours: ', len(selected_contours))
    cv2.drawContours(contour_image, selected_contours, -1, (0, 255, 0), -1)
    cv2.imshow('processing', contour_image)
    cv2.waitKey(waitTime)

    circle_count = 0
    circle_contours = []
    for index, cnt in enumerate(selected_contours):
        contour_image = image.copy()
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        print(index, x, y, radius)
        cv2.drawContours(contour_image, [cnt], 0, (0, 255, 0), 3)
        cv2.circle(contour_image, (int(x),int(y)), int(radius), (255, 0, 0), 3)
        contour_area = cv2.contourArea(cnt)
        circle_area = int(np.pi * radius * radius)
        off_percentage = int(((circle_area - contour_area) / contour_area) * 100)
        if off_percentage <= 50:
            circle_count = circle_count + 1
            is_circle = True
            circle_contours.append(cnt)
        else:
            is_circle = False
        cv2.putText(contour_image, f"{contour_area} & {circle_area} & {off_percentage} & {is_circle}",
                    (30,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1)
        cv2.imshow('processing', contour_image)
        cv2.waitKey(waitTime)

    contour_image = image.copy()
    cv2.putText(contour_image, f"Number of eggs inside the box: {circle_count}", (30,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.drawContours(contour_image, circle_contours, -1, (0, 255, 0), 3)
    cv2.imshow('processing', contour_image)
    cv2.waitKey(0)

    cv2.destroyWindow('processing')

    return circle_count

if __name__ == '__main__':
    print('ran directly')
    image = cv2.imread('images/eggs_2_with_1_outside.jpeg')
    cv2.imshow('input', image)
    cv2.waitKey(0)
    count = number_of_eggs(image, waitTime=0)
    cv2.putText(image, f"Number of eggs inside the box: {count}", (30, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('output', image)
    cv2.waitKey(0)



