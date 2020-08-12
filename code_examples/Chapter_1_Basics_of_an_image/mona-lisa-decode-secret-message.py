import cv2
image = cv2.imread('./images/monalisa_encoded.png', cv2.IMREAD_UNCHANGED)
cv2.imshow('input', image)
cv2.waitKey(0)

print('before: ')
print(image[1000])
row = image[1000]
message = ''
for col in row:
    message = message + chr(col[0])

print(message)


