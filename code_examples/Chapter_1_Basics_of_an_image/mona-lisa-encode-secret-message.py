import cv2
image = cv2.imread('./images/monalisa.jpg')
cv2.imshow('input', image)
cv2.waitKey(0)
print('before: ')
print(image[1000])

message = "This is a very important message. Please send the infantry. Do it Now! " * 3
counter = 0
for character in message:
    print(character, ' = ', ord(character))
    image[1000][counter] = ord(character)
    counter = counter + 1

# image[999] = (255, 255, 255)
# image[1001] = (255, 255, 255)

cv2.imshow('encoded output', image)
cv2.imwrite('images/monalisa_encoded.png', image, [cv2.IMWRITE_PNG_COMPRESSION, 0])
cv2.waitKey(0)

print(image[999])