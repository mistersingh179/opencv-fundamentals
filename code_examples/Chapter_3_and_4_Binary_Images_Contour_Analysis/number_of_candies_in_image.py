import cv2


# from binary_image_helpers import various_binary_images
# from contour_helper import inspect_all_contours

def candy_count(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3,3), None)
    thresh_adapt = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    contours, hierarchy = cv2.findContours(thresh_adapt, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # foo = image.copy()
    # cv2.drawContours(foo, contours, -1, (0, 255, 0), 1)
    # cv2.imshow('foo', foo)
    # cv2.waitKey(-1)

    selected_contours = []

    for (index, cnt) in enumerate(contours):
        area = cv2.contourArea(cnt)
        print(index, ": ", area)
        if area > 100:
            selected_contours.append(cnt)

    # foo = image.copy()
    # cv2.drawContours(foo, contours, -1, (0, 255, 0), 1)
    # cv2.imshow('foo', foo)
    # cv2.waitKey(-1)

    return len(selected_contours)

if __name__ == '__main__':
    print('running directly')
    image = cv2.imread('./images/many_m_n_m.jpg')
    count = candy_count(image)
    print('count: ', count)