# Image Pre-Processing

## Change Color Scheme to Gray

https://docs.opencv.org/2.4/modules/imgproc/doc/miscellaneous_transformations.html#cvtcolor

```python
image = cv2.imread('./images/test.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

#### What it does?

- This reduces the number of channels from 3 to 1. 
- BGR is default and has 3 channels. 
- Gray is single channel with a value between 0 and 255.

#### Why do it?

- It reduces the size of the image and thus speeds up things
- makes it easy to intuitively work with the image as each pixel has 1 value
- Many pre-build neural networks require grayscale image
- Makes it easy to build binary images by applying techniques like thresholding, canny etc.



## Blur an image

### Why do it?

- Often an image has noise which needs to be removed?
- The lighting may be producing a glare which is throwing off the results between different image sets
- The picture may have rough edges which are not of significance to the logic we want to apply and need to be taken in to consideration

### How to do it?

The most common way is to use `cv2.GaussianBlur`. Below 3 way are discussed.

### Gaussian Blur

https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#gaussianblur

```python
blurred = cv2.GaussianBlur(image, (11, 11), None)
```

#### What it does?

- convulated the source image with a Gaussian Kernel of the specified size.
- Size of the Gaussian kernel can be give n in ksize or sigmaX
- a linear operation and preserve of edges is based on the kernel size

#### Why do it?

- smoothing things so edge detection algorithms dont make mistakes and detect edges when there aren't any
- with blur, things are getting averaged and now its easier to extract the ROI
- Often a must do before building the binary image

### Median Blur

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html#median-filtering

```python
cv2.medianBlur(image, 5)
```

#### What it does?

- computes median of all pixels under the kernel
-  and replaces the central value with the median value.
- uses median value i.e. middle value

#### Why do it?

- highly effective when removing salt and pepper noise
- preserves edges as its actually using a value which is present

### PyrMeanShiftFiltering

https://docs.opencv.org/2.4/modules/imgproc/doc/filtering.html#pyrmeanshiftfiltering

```
cv2.pyrMeanShiftFiltering(image, 21, 51)
```

as input it takes the image, spatial window radius & color window radius

#### Why do it?

- helps detect better edges in certain scenerios
- works on color image

#### What it does?

- works on a color image
- output is a filtered "posterized" image with color gradients and fine grain texture flattened



## Binary Image

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html

#### What is it?

- It is an image where each pixel can have one of only 2 possible values. 
- They can be 0 which makes the pixel black, or it can be 255, which makes it white. 

#### Why do it?

- allows to seperate the region of interest from everything else. 
- e.g.when analyzing a football, we make football have pixel value of 255 and everything else have value of 0.
- its a crucial prelimanry step to detecting object contours. without first having a binary image, we can detect contours and thus can proceed with computer vision on an object.

#### How to do it?

Three popular ways of building a binary image are:

- thresholding 
- inRange
- canny

They all work differently but the goal and output is the same, which is to have a binary image where each pixel is either black or white.

### Thresholding

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#image-thresholding

https://docs.opencv.org/master/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57

#### Simple Thresholding

- The simplest way of thresholding is to start with a pre-determined value, lets say its 127. 
- Then for every pixel whose value is above it gets assigned one value (255 i.e. white) and all others get the other value (0 i.e. black).
- And you end up with a binary image.

```python
retval, thresh = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY)
```

Here we have provided an arbitary value of 127 to segment the image in to two parts. We could pass any number here like 10, 50, 100 etc. It is however a common practive to use the middle value of 127 for many cases. This works very well when the object we want has a specific color and everything we dont want is a different color. Then we can just pick a number between the two and seperate what we want from what we dont and get that as a binary image.

The type of binary image here is set to `cv2.THRESH_BINARY`. Another option is to set it to `cv2.THRESH_BINARY_INV` which produces the output image. This means what was going to be white becomes black and vice-versa.

#### Adaptive Thresholding

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_thresholding/py_thresholding.html#adaptive-thresholding

The concern with simple thresholding was that it takes 1 constant value as input to pivot on and build the binary image. This may not work well for many images where the object we are looking to extract has range of color value depending on where it is in the picture. This could be because it is lighter in color at one part and darker on the other.

This is where `cv2.adaptiveThreshold` comes to help. It doesn't need any constant input value to pivot on. Instead for every small region in the image it calculates the 

```python
thresh_adapt = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh_adapt = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
```

- `cv2.ADAPTIVE_THRESH_MEAN_C` uses the mean value of the neighborhood pixels
- `cv2.ADAPTIVE_THRESH_GAUSSIAN_C` uses the weighted sum of the neighbordhoosd values where weights are a gaussian window.
- `11` here is the block-size which decides how big the neighbordhood value should be
- `2` is just a constant which is subtracted from the calculated mean or weighted mean.

#### Otzu Binarization

So Simple thresholding uses one inputed global value. This doesnt work many times. Then Adaptive Thresholding looked at the neighboring values and calculated the value to pivot on. Now we have Otzu Binarization which works very well for Bimodal images. These are images which have 2 peaks in their histograph. Basically it caculates the two peaks and then takes the middle value between then. So very much like simple-thresholding where we passed in the middle value of 127, but here it automatically calculates the middle vaue from the 2 peaks.

```python
retVal, thresh_otsu = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
```

It also returns the value it picked as `retVal`.

### InRange

Another way to build a binary imag, similar to `thresholding` which works on on color ranges rather than just a specific value.

It takes an image, lower range of the color and higher range of the color.
returns binary image with everything in that range as 255 (white) and rest of the pixels which are not in the range as 0 (black).

```python
inRange = cv2.inRange(blurred, 50, 110)
```

It can work on a grayscale image or on any specific channel of a color image

```python
img = cv2.imread("test.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,(10, 100, 20), (25, 255, 255) )
cv2.imshow("orange", mask);cv2.waitKey();cv2.destroyAllWindows()
```

A common use case is to first know the color range of the ROI you want. You could know this by using a third party tool or just plotting it on a histograph. Then use that information to build a binary image using `inRange`. Once you have your ROI in white you can easily capture its contour as it will be the only one.

### Canny

https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html

Canny is an edge detection algorithm which can produce binary images. The detected edge is 255 (white in color) and everything else is 0 (black in color).

It takes 2 values `lower` and `upper`. 

First it tries to detect the edges of an image. 

- Then for every possible detected edge pixel it checks if the value is greater than the supplied `upper`. If yes it is confirmed to be a "sure edge" and set to 255 (white). 
- If value is below `lower` its discarded as its not an edge and set to 0 (black)
- And for other values which lay between `lower` and `upper` range, it checks if that pixel is connected to another "sure edge" and if yes, then it is also set to 255 (white).

The values of lower and upper are user provided and good heuristic is to take 1 standard deviation from the media value

```
v = np.median(blurred)
lower = int(max(0, (1.0 - 0.33) *  v))
upper = int(min(255, (1.0 + 0.33) * v))
edged = cv2.Canny(blurred, lower, upper)
```



















































