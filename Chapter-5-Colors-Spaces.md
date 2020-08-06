# Color Spaces

Color's can be represented in a variety of ways and openCV supports many of them and makes conversions between them easy. First we need to understand how these color spaces differ and what their pros and cons are and then we would know when to use which one.

## BGR

- This is the most common and default color space.

- It has 3 channels Blue, Green & Red

- The output color of the pixel is the additive value obtained by combination of these 3 channels.

- The channel values includes the amount of light hitting the surface
- It is easy to reason as its additive Blue, green and red values but hard to compare as same image with same object may have different lighting and thus different values.

```python
image = cv2.imread('./path/to/image.jpeg')
b, g, r = cv2.split(image)
mean_bgr = cv2.mean(image)

B = image[:,:,0]
G = image[:,:,1]
R = image[:,:,2]
np.mean(B)
np.median(B)
```

## GRAY

- has only 1 channel
- single channel value is between 0 and 255
- so much easier to understand and reason as 0 is black and higher the value the lighter it gets till it hits 255 which is white
- lighter in size as single channe
- a required step in may pre-processing steps and algorithms

```python
cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```



## LAB 

- 3 channels
- Light (Light intensity), A (Green to Magenta), B (Blue to Yellow)
- Since light is seperate, we can now compare colors even when light intensity is different
- the light channel carries all the brightness information
- A & B have a uinform color space so its intutive to reason
- its independent of device

```python
cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
```



## HSV

- 3 channels
- Hue (color), Saturation (shade) & Value (Inensity)
- color is represented by only 1 channel making it easier to specify and reason
- light is included in 1 channel so we can seperate it
- values are device dependent
- Hue is specifed in a circle with 0 and 180 both are the same i.e. Red

https://i.stack.imgur.com/gyuw4.png

```python
cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
```



## Eucildean Distance

Computes the euclidean distance between 2 1-D arrays. Here each 1D array holds three values. If those values are x,y & z co-ordinates in 3D space, we are here getting the distance between the two.

If we have two colors with 3 channels which we get by doing `cv2.mean`, then we can see how similar they are by `dist.euclidean`

```python
from scipy.spatial import distance as dist
a = [255, 255, 255]
b = [0, 0, 0]
c = [127,127,127]
d = [0, 255, 0]
dist.euclidean(a,b) #441.6729559300637
dist.euclidean(a,c) # 221.70250336881628
dist.euclidean(a,d) # 360.62445840513925
```



## Histographs

An easy way to visulize the color of an image or an ROI is to plot them using a Histograph.

Histogram represents the distribution of colors in an image.
When visualized in a graph or plot, it gives high level intuition of pixel distribution.

X axis is the color channel value 0 - 255
Y axis is how many pixels are at that value
Optionally, X axis can be in bins and then Y value will represent total number of pixels which have values in that bin.

```python
cv2.calcHist(images, channels, mask, histSize, ranges)	
```

- images is an array - [image1]
- channels is list of indexes we want to compute histograph for. for grayscale [0] and RGB its [0,1,2]
- mask is a mask image with `dtype='unit8'`, binary image with 1's (white) at the region where want to compute the histograph. To get the entire image that is have no mask, set it to `None or np.ones(image1.shape, dtype='uint8')`
- histSize - list with number of bins for each channel. if its RGB then max bins could be [255, 255, 255]
- ranges - range of possible pixel values for each channel. for RGB each channel has [0,256]

- It returns an array where each value represents the number of pixels belong to the bin represented by the bin's index.

```python
hist = cv2.calcHist([gray_image], [0], None, [2], [0,256])
print(hist)
```

```python
[
    [ 14469.] # number of pixels in first bin
    [106031.] # number of pixels in second bin
]
```

this shows most pixels are lighter i.e. in 2nd bin. 

###  Plotting the Histograph

For a GRAY (grayscale) image, we only need to plot the first and only channel

```python
from matplotlib import pyplot as plt

histogram_array = cv2.calcHist([blurred], [0], None, [256], [0,256])
plt.figure()
plt.plot(histogram_array)
plt.show()
```

For a LAB image, we would want to plot the 2nd and 3rd channel as light is situation dependent.

```python
lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
blurred_lab_image = cv2.GaussianBlur(lab_image, (5, 5), None)

a_channel_hist_data = cv2.calcHist([blurred_lab_image], [1], None, [256], [0,256])
print('channel A max: ', a_channel_hist_data.argmax())
plt.plot(a_channel_hist_data, color='g')
plt.xlim([0,256])
plt.xticks(np.arange(0, 256, 25))

b_channel_hist_data = cv2.calcHist([blurred_lab_image], [2], None, [256], [0,256])
print('channel B max: ', b_channel_hist_data.argmax())
plt.plot(b_channel_hist_data, color='b')
plt.xlim([0,256])
plt.xticks(np.arange(0, 256, 25))

plt.ylabel('number of pixels')
plt.show()
```

