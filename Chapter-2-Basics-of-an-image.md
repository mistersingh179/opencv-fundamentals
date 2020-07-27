# Basics of an image

## Read, print & Show

```
image = cv2.imread('./path/to/file.jpg')
cv2.imshow('windowname', image)
print(image)
print(image.shape)
```

## Convert to grayscale

```
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image)
print(image.shape)
```

## Manipulate

```
image[4] = 0
print(image)
print(image)
```

## Build a Random Image

```
a = np.random.rand(100)
b = a * 255
c = b.astype('uint8')
d = c.reshape(10,10)
cv2.imshow('output', d); cv2.waitKey(0);
cv2.imwrite('./d.png', d)
```

## Build a color image with random values

```
import numpy as np
import random
import cv2

image = np.zeros((100,100,3), dtype='uint8')

for i in range(100):
    for j in range(100):
        for k in range(3):
            random_number = int(random.random() * 255)
            print(i, j, k, random_number)
            image[i][j][k] = random_number

print(image)
cv2.imshow('output', image); cv2.waitKey(0);
```

## Project - Secret Communication Image

Take a message, encrypt in to an image, pass it forward and then decrypt it to read the message

TODO