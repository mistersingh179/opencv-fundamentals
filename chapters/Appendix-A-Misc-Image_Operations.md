# Rotate an Image

## `warpAffine` & `getRotationMatrix2D`

geometry unit circle states that positive angles are counter-clockwise and negative angles are clockwise.

To rotate we first need the center of the image

```python
center = (width//2, height//2)
```

Use `//` to perform division with no decimals

Then we need the rotation matrix. OpenCV allows rotation from any angle.

```python
M = cv2.getRotationMatrix2D(center, -45, 1.0)
```

Then we use `warpAffine` which modifies the source image based on the transforamtion matrix

```python
center = (width//2, height//2)
M = cv2.getRotationMatrix2D(center, -45, .25)
rotated_image = cv2.warpAffine(image,M,(width,height))
```

When we rotate an image, its size may also need adjusting or things will go off screen.

#### `imutils.rotate`

Scale can be provided when rotating, and this can be done automatically:

```python
rotated = imutils.rotate(image, angle)
rotated = imutils.rotate_bound(image, angle)
```

