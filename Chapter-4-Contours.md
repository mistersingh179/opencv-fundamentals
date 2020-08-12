# Contours

A contour is a boundary of a shape with same color intensity. It is denoted as an list of x-y co-ordinates.

## Contour Extraction

https://docs.opencv.org/3.4/d9/d8b/tutorial_py_contours_hierarchy.html

**TL;DR:** When applied on binary images, its will find the white object from the black bacground

- Contour detection comes in to play when we need to extract or examine an ROI from an image. 
- Contour itseld is basically a list of x,y continuous points  have the same color intensity. 
- So when applied to a binary image where the ROI is all 255 (white) and the rest is all 0 (black) then it can gives us all the points of the ROI's bondary.

```python
contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

#### Common `mode` values:

- `cv2.RETR_EXTERNAL` : will returns only yhe outter extreme contours. 
- `cv2.RETR_LIST` : gives all contours without extablishing any hierarchical relationships
- `cv2.RETR_TREE` : gives all contours and full hierarchy of nested contours

#### Common `method` values:

- `cv2.CHAIN_APPROX_NONE` : This will return every point along the boundary. Most of the time this is unnecessary.
- `cv2.CHAIN_APPROX_SIMPLE`: This will remove redundany points needed to draw a straight line

#### Returns:

`contours` is the main returned value which is a list of detected contours. Each contour in the list is a further list of xy cordinates which when connected with straight lines forms the shape.

`hierarchy` : is an optional array with same length as that of the returned  `contours` array. For the `ith` contour in list `contours`, `hierarychy[i]` is an array with 4 values. 

- value of `hierarchy[0][i][0]`is the index of the contour which is the next contour at the same hierarchical value
- value of `hierarchy[0][i][1]`is the index of the contour which is the previous contour at the same hierarchical value
- value of `hierarchy[0][i][2]`is the index of the contour which is the first child contour
- value of `hierarchy[0][i][3]`is the index of the contour which is the first parent contour

https://docs.opencv.org/3.4/d9/d8b/tutorial_py_contours_hierarchy.html

#### Structure of a contour:

A single contour which there are many in the contours list, looks like this:

```
[
    [[1,2]],
    [[12,3]],
    [[21,4]],
    [[15,5]]    
]
```

This shows 4 points which when connected will make the contour. The values are nested in an array twice. We can solve for that and just get the co-ordinates when needed:

```
contour = np.array([
    [[1,2]],
    [[12,3]],
    [[21,4]],
    [[15,5]]    
])
ans = contour.reshape(4,2)
print(ans)	
```

Output: 

```
array([[ 1,  2],
       [12,  3],
       [21,  4],
       [15,  5]])
```

## Approximate a Contour:

We used ``cv2.CHAIN_APPROX_SIMPLE` which got rid of redundant contours, but still there are more which can be removed but weren't. This is because their are errors in the way the picture was captured by the camera. At the pixel level things are not exactly how they should be. To solve for this we can use Contour Approximation – `cv2.approxPolyDP` .

TL;DR: Contour Approximation is converting a contour to another contour with reduced number of points bases upon a precision number.

```python
peri = cv2.arcLength(cnt, True)
approx_cnt = cv2.approxPolyDP(cnt, peri * 0.04, True)
```

`arclength` gives us the permiter length of the contour. They we take 4% of that as the precision number and run it through `approxPolyDP`. This will correct any error with a 4% tolerance and reduce the number of points. Lastly we tell it that the contour is a closed shaped.

I see myself doing this almost always as nothing is ever perfect. The amount of correction is something which needs to be set based on experience and heuristics.



## Draw Contours

- It just connects all the contour point forming a shape. 

- The  order of the contours doesnt matter

- You can pass in the actual contour itself, the reduced contour set based on approximation or just a np.array of x-y indexes

```python
contours, hierarchy = cv2.findContouts(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, 0, (0, 255, 0), -1)
cv2.drawContours(image, [np.array([[10,300], [200, 300], [300, 400]])], 0, (0, 255, 0), -1)
```

For `contourIdx` you can pass the index of the contour to draw or -1 to draw all contours

For `thickness` a negative number will fill the entire contour's shape with the passed in color.

Draw just contour Points



## Draw just the contour points

If you dont want to connect the contour points, but instead want to see the contours, that can be accomplished by drawing a circle at each point.

This is no longer contour related, but instead is using the drawCircle method along with the knowledge that a contour is nothing but a list of vertices.

```python
cnt = cnt.reshape(4,2)
for i in cnt:
    cv2.circle(image, (i[0], i[1]), 3, (0, 255, 0), -1)
```



## Convex Hull Contour

It takes the existing contour and builds another contour such that the new contour is convex in shape. This means that this new contour goes around the original contour / object / ROI such that it most tightly encloses/surrounds it. Since its convex no interior angle is greater than 180 degrees.

Use case: Given a bunch contour points, using convexHull we can extract the boundary of the entire object which cover the etnire scene. So given a car's contour, we can calculate its convex hull and then use that to detect collision.

```python
hullContour = cv2.convexHull(the_contour)
```

A convex hull is also a contour. It has the same structure of points etc. So we can use `cv2.drawContours` to visualize it.



## Draw shapes around the contour

Once we have a contour, which has then be simplied with `approxyPolyDP` we have the object we want. But each contour is different and by enclosing it a shape we can then reason about all of them in a generic way. We can also compare it to a shape its a subset of. We can also extract it and draw masks of it. Although a mask can be made of the contour directly as well.



### Straight Bounding Rectangle

Gives co-ordinates to draw a rectangle which encloses the contour. Similar to convex hull, but this one is a rectangle and it doesnt return a contour but parameters which can then be used to draw a rectangle.

```python
x, y, w, h = cv2.boundingRect(all_enclosing_contour)
cv2.rectangle(bounding_rectangle_image, (x,y), (x+w, y+h), (0,255,0), 3)
```



### Minimum Enclosing Circle

Gives center co-ordinates and radius to enclose the contour in a radius.

```python
(x, y), radius = cv2.minEnclosingCircle(all_enclosing_contour)
cv2.circle(circle_image, (int(x), int(y)), int(radius), (0,255,0), 3)
```

This can be used to detect if the contour is a circle. Just draw this circle and then compare its area and other properties with the existing contour.

### Rotated Rectangle

This fits a rectangle around it.

```python
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
im = cv2.drawContours(im,[box],0,(0,0,255),2)
```

It also gives the angle the contour is at starting with 0 on the right and 90 degrees is straight perpendicular to it.

```python
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
	angle = -(90 + angle)
else:
	angle = -angle
```



### Fitting an Eclipse

This makes an ellipse around the contour. It returns a tuple with a tuple which has 2 points and a radius. These can then be used to to build an eclipse.

```python
ellipse = cv2.fitEllipse(all_enclosing_contour)
cv2.ellipse(ellipse_image, ellipse, (0,255,0), 3)
```



## ROI Extraction with a mask built with Contours

A mask is a binary image with just the object or objects you want filled in with white and everything else black. It is normally used  to pass in to other functions like `bitwise_and`, `cv2.mean` , `cv2.calcHist ` along with the image so that function knows where in the image to operate. 

- Draw contours and identify the contour which is of interest
- Make a new blank image of same shape but with black background
- Draw the contour of interest on this black image and fill it with white
- Now you have a binary image with just your ROI highlighted
- This is a mask
- `Bitwise_and` it with the original image to extract your ROI in color



If you have multiple contours to extract do the same process for all of them or `bitwise_or` multiple binary images.



```python
mask = np.zeros(gray.shape, dtype='uint8')
cv2.drawContours(mask, [the_contour], 0, 255, -1)

blue_item = cv2.bitwise_and(image, image, mask=mask)
ans = cv2.mean(image, mask=mask)
```



## Contour Features

### Centroid

This is the center of a contour.

```python
M = cv2.moments(cnt)
cx = int(M['m10']/M['m00'])
cy = int(M['m01']/M['m00'])
```

### Area

```python
M = cv2.moments(cnt)
area = M['m00']
area = cv2.contourArea(cnt)
```

### Permiter

```python
perimeter = cv2.arcLength(cnt,True)
```

### Convex Hull

Converts the contour in to a convex shape and can also return the contour points and convex points so you can see how much defect was fixed to make the convex hull

```python
hull = cv2.convexHull(cnt)
indexes__of_contour_points_which_were_fixed = cv2.convexHull(cnt, returnPoints = False)
```

### Extend

ratio of contour area to bounding rectangle area

```python
area = cv2.contourArea(cnt)
x,y,w,h = cv2.boundingRect(cnt)
rect_area = w*h
extent = float(area)/rect_area
```

### Solidity

```python
area = cv2.contourArea(cnt)
hull = cv2.convexHull(cnt)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area
```

	### Diameter

```python
area = cv2.contourArea(cnt)
equi_diameter = np.sqrt(4*area / np.pi)
```



## Merging 2 or more contours

contours are nothing but co-ordinate points. so just draw all the contours on a mask and fill them with white color. Then just get all nonzero corindates. the list of co-ordinates is your new merged contour. Or another option is after drawing it then findContours again on the new mask and it will find the collected contour. Or another option is to just merge the points of all contours.

```python
mask = np.zeros(thresh.shape)
mask = cv2.drawContours(mask, contours, -1, 255, -1)
y_cords, x_cords = np.where(mask == 255)
coordinates = np.transpose((x_cords, y_cords))

mask2 = np.zeros(thresh.shape)
cv2.drawContours(mask2, [coordinates], -1, 255, 1)

all_enclosing_contour = []
for contour in contours:
    for point in contour:
        print('looking at point: ', point)
        all_enclosing_contour.append(np.asarray(point))

all_enclosing_contour = np.asarray(all_enclosing_contour)
```



## Persepctive Transform

Given 4 points on the input image
and the wanted 4 points on the output image
we can call `cv2.getPersepctiveTransform` and it will give us a 3x3 transformation matrix
then we can apply this matrix using `cv2.getPersepctiveTransform`
this will get us the output image



```python
pts1 = np.float32([[x,y], [x+w,y], [x+w, y+h], [x,y+h]])
pts2 = np.float32([[0,0],[w,0],[w,h],[0,h]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(image,M,(w,h))
```



For this to work, we need 4 points, this is simpler in sum cases when you have a piece of paper which has 4 distinct corners specially when surrounded by a rectangle but much harder when the contour is not a nice rectangle. Then we need to arange them in a consitent order between the input points and output points and then we also need the output width & height. `pyimagesearch` has a `four_point_transform` a helper function to do this for you. all it needs is the contour to be fixed as input



```python
from pyimagesearch.transform import four_point_transform
dst = four_point_transform(image, contour.reshape(4, 2))
cv2.imshow('image', dst)
cv2.waitKey(0)
```



### Filtering Contours

Once you have found the contours in an image, at many times you need to find the contour which you are interested in. This can normally be done by finding the contour which is:

- Biggest area 
- smallest area
- has a specific strcuture like based on numner of sides like 3, 4, 5 etc.
- dimension of sides as in its a rectangle, square, right etc.
- sorted based on some property like width, height etc.
- filtered on solidity, extend, area or some other comparison to the enclosing contour
- specific top, bottom, left, right co-ordinates in absolute numbers or as a percentage of image

All of these can be used to zoom in the contour you want.

```python
for idx, cnt in enumerate(cnts):
    x, y, w, h = cv2.boundingRect(cnt)
    ca = cv2.contourArea(cnt)
    ra = w*h
    text_to_write = f'idx: {idx}, contour area: {ca}, rect area: {ra}, x: {x}, y: {y}, w: {w}, h: {h} '
    print(text_to_write)
    bounding_boxes_image = image.copy()
    cv2.rectangle(bounding_boxes_image, (x, y), (x + w, y + h), (0, 0, 255), 1)
    cv2.drawContours(bounding_boxes_image, [cnt], 0, (0, 255, 0), 1)
    bounding_boxes_image = cv2.copyMakeBorder(bounding_boxes_image,
                                              top=0, bottom=bottom, left=0, right=right,
                                              borderType=cv2.BORDER_CONSTANT, value=0)
    cv2.putText(bounding_boxes_image, text_to_write,
                (20, bounding_boxes_image.shape[0]-5),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 1)
    cv2.imshow('bounding_boxes_image', bounding_boxes_image)
    key = cv2.waitKey(0)
    if chr(key) == 'q':
        break
```











