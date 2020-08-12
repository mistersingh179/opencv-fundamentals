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

## Manipulate Image Data

```python
image[4] = 0
print(image)
print(image)
```

# Resize an Image

- ` cv2.resize` takes a w,h tuple 
- and doesnt care of aspect ratio, you need to take care of that

```python
h, w = gray.shape
resized = cv2.resize(gray, (w*2, h*2)) # doubles the image
```


```python
h, w = gray.shape
height = 500
width = int(w/h * 500)
resized = cv2.resize(gray, (w*2, h*2)) # sets height to 500 and preserves the aspect ratio
```

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_geometric_transformations/py_geometric_transformations.html#scaling

# Crop an image to get ROI

```python
face = image[60:160,320:420] # rows first and then columns
```

- This is using numpys ability to access specified elements in each dimension. 

- It is inclusive of first element and not inclusive of last element specified in range.

```python
face = image[60:160][320:420] # this is not the same
```

- When we access via sqaure brackets we are changing the shape as we are just getting elements back.

## Build a Grayscale Image with random values

```python
a = np.random.rand(100)
b = a * 255
c = b.astype('uint8')
d = c.reshape(10,10)
cv2.imshow('output', d); cv2.waitKey(0);
cv2.imwrite('./d.png', d)
```

Build a Binary image with random values

```python
a = np.zeros(100, 100)
for i in range(100):
  for j in range(100):
    if random.random() >= 0.5:
	    a[i][j] = 255
cv2.imshow('output', a); cv2.waitKey(0);
cv2.imwrite('./d.png', d)
```

## Build a color image with random values

```python
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

# Project - Secret Communication Image

Take a message, encrypt in to an image, pass it forward and then decrypt it to read the message

**<u>TODO</u>**