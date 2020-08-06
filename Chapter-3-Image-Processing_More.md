# Morphological Transformations

At many times the contours we get are not perfect due to the quality of the image. Morphological oeprations can help here. 

First what happens in the transformation?

- it takes the input image with foreground in white and background in black
- and it takes a kernel aka structuring element
- then the specific morphological operation is applied

## Most common morphological operations:

#### `erode` – will get rid of small blobs of white noise in the foreground

- reduce noise in a bianary image 
- it reduces the size of foreground objects 
- the more the iterations the more reduction you will get

since it reducing the white colored items, we should prepare the image such that noise is white and then we can get rid of it.

```
mask = thresh4.copy()
mask = cv2.erode(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
```

#### dilate – will make disconnected foreground contours connect as it will increase the size of foreground(white) images

It does the opposite, it increases the size of the foreground images.
it makes the white parts bigger.

__Point__ is that you can erode way the while blobs, once they dissapear then you can dilate back up. Things which became smaller will become big again with dialte, but thigns which have dissapeared wont come back with dilate.

```python
mask = thresh4.copy()
mask = cv2.dilate(mask, None, iterations=5)
cv2.imshow("Eroded", mask)
```

#### Morphological Gradient

Its the difference between dilation and erosion of an image.
The result will be the outline of an image.
Dilate is adding pixels, Erosion is removing pixels. If we subtract one from the other, we will get a good boundary. Thats what Morphological Gradient gives.

```python
gradient2 = cv2.morphologyEx(thresh127, cv2.MORPH_GRADIENT, M);
cv2.imshow('gradient2', gradient2)
cv2.waitKey(0)
```

`morphologyEx` is the main function which does the morphological transformations. `erode` and `dilate` are just syntactical sugar.

It supports various operations like cv2.MORPH_ERODE, cv2.MORPH_DILATE, cv2.MORPH_GRADIENT etc.

It also takes the kernel which can be built as a rectangle of ones `np.ones((2,3))` or be built using `cv2.getStructuringElement`

```python
cv2.getStructuringElement((2,3), cv2.MORPH_RECT)
```

other shapes:
- MORPH_CROSS
- MORPH_ELLIPSE

Complete method:

```python
thresh2 = cv2.morphologyEx(thresh, cv2.MORPH_ERODE, kernel, iterations=1)
```

