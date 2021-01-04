# What is in this course?

This course covers the fundamental of OpenCV and it is desinged to be project oriented. Instead of going over command after command available in OpenCV, we will be tackling various computer vision problems. And then while working through each vision problem, we will learn new openCV commands and apply them to solve the vision problem at hand.

Below are 7 vision problems we will work through. The vision problems in the begining are rather simple and you will encounter many new concepts and commands in them. As we progress through, the problems will get harder and they will build on top of the knowledge you would have gained in the previous problems.



# Course Content

## 7 Vision problems

### Encode/Decode Secret Messages in the Mona Lisa Painting

- what is an image,
- how are they stored and structured,
- what does their content look like
- color vs black n white
- how can it be manipulated etc.

<img src="https://s3.amazonaws.com/images.179ways.com/mona_list_input_and_encoded_output.jpg" alt="Input &amp; Encoded Mo. List" style="zoom:25%;" />



### Adding time Elaspsed to an existing video, like in those director's cut movies

- using camera or video file

- converting video to images

- Writing text to video

  <img src="https://s3.amazonaws.com/images.179ways.com/waterfall_video_with_and_without_timestamp.gif" alt="waterfall_video_with_and_without_timestamp" style="zoom: 100%;" />



### Determine how many pieces of candy are left

- grayscaling an image
- blurring
- Binary 
- count Contours
- drawing rectangle on an image
- writing text

<img src="https://s3.amazonaws.com/images.179ways.com/M_and_M_Candy_Counting.gif" alt="Candies Count" style="zoom:50%;" />

[Gif](https://s3.amazonaws.com/images.179ways.com/M_and_M_Candy_Counting.gif)

### Count Candy pieces off Camera Video

- accessing camera video
- frame extraction at lowers FPS
- re-using image analysis function from video
- writing text

<img src="https://s3.amazonaws.com/images.179ways.com/candies_on_table_from_video.gif" alt="Candies Count" style="zoom:50%;" />

[Gif](https://s3.amazonaws.com/images.179ways.com/candies_on_table_from_video.gif)

### Detect Position Of an Object in a plane

Skills you will learn & pracitce:

- contour Properties - x,y co-ordinates, circle area
- Erode & dilate
- draw circle, rectangle & write text
- color scheme & LAB



<img src="https://s3.amazonaws.com/images.179ways.com/carrom_board_with_queen_found.gif" alt="Carrom Board Position of Queen" style="zoom: 45%;" />

[Gif](https://s3.amazonaws.com/images.179ways.com/carrom_board_with_queen_found.gif)

### Determine if an employee wearing company t-shirt is present on the floor via camera?

- color schemes
- binary image by using inRange and masks
- histographs
- contour analysis

<img src="https://s3.amazonaws.com/images.179ways.com/tshirt_histogram.jpg" alt="T-Shirt Histogram" style="zoom: 45%;" />

<img src="https://s3.amazonaws.com/images.179ways.com/green_tshirt_detect_on_floor.gif" alt="T-Shirt Detected"  />

[Gif](https://s3.amazonaws.com/images.179ways.com/green_tshirt_detected.jpg)

### Count the number of eggs in the box?

- contours
- mask
- Binary operations
- erode
- contour analysis

<img src="https://s3.amazonaws.com/images.179ways.com/eggs_counting.gif" alt="Number of eggs in the box"  />

[Gif](https://s3.amazonaws.com/images.179ways.com/eggs_counting.jpg)

# Introduction

## TL;DR

OpenCV helps remove unwanted things (aka noise) so that deep learning algorithms can be applied on the correct object of interest.

## Why are we learning OpenCV?

We want to solve vision related problems and OpenCV enables us to process images and build an image processing pipeline so we can simplify the problem or solve it completely. OpenCV enables us to do many of those pre-requisite things which needs to be done before deep learning can be applied. These are things which are part of the image pipeline, they are those pre-processing things which must be done to get to the region of interest, on which then you may apply deep learning.



## A Real Life OpenCV Example and our final Project

Below is a carton of eggs and we want to know how many eggs are in it. This is a classic vision problem and we will use OpenCV to build the image pipeline to remove things outside the box and then count the number of eggs in the box

<img src="https://s3.amazonaws.com/images.179ways.com/eggs_counting.gif" alt="Number of eggs in the box"  />



### Image Pipeline steps

- load image in to a matrix
- Change color scheme as the colors are irrelevant to the problem at hand
- blur the image to remove smudge, make edges smooth and remove picture defects
- build a Binaryimage 
- detect edges of the carton
- detect contours of various objects in the scene
- perform analysis on each contour to remove everything but the carton
- apply contour fixing to compensate for contour and picture defects
- extract just the contour box from the image
- re-apply every step above again now on just the carton
- build Binary to detect eggs
- find all conoturs
- analyze each contours property and check for it to be an egg
- Store count of eggs and build new image with count stamped

Some or all of the above mentioned operations are used to build an image processing pipeline to get to the real object we want to study and apply sophisticated machine learning algorithms. The deep learning algorithms are important but so are the steps needed to get to the object which needs to be studied. 

In many instances machine learning maybe an over-kill and it may make more sense to use heuristics and build the logic yourself. For example machine learning may make a lot of sense when we want to detect between a cat and dog, but if we want to detect the between a circle and a square then the logic to do so can coded directly with the help of OpenCV.

Many time you may end up solving all trivial things with openCV and removing them from the equation and leaving behind the harder vision problem for a deep learning algorithm.



## What if I don't learn it?

If you dont take the above mentioned steps then:

-  the problem unnecessarly becomes harder and expensive to solve
-  your deep learning algorithm many learn wrong things 
-  or it may take a lot longer to learn
-  or it may overfit 
-  and you maybe running in circles trying to fit a square peg in circlular hole
-  in other words you will be over-engineering things which have simpler and more elegant solutions

I guess what i am trying to say is that there is a scappel and then there is a bazooka. Its best to know both rather than pulling out the bazooka on every occasion.



## A side note on the use of deep learning algorithm

The actual determination of whether the thing in the carton is an egg or not, can very well be done by a deep learning algorithm, but in this case we will use simple huristics and code the logic to detect an egg ourselves using OpenCV. On the other hand, if the problem had been slightly harder where inside the carton there could be:

- a golf ball or
- a ping pong ball or
- a cracked egg which we dont want to count or
- a brown/golden egg which we do want to count

Then Yes, absolutely we would want to make our lives easier and use a deep learning algorithm to decide if the thing is an egg or not. Even if we had used an image classification algorithm we would still use all the tools provided by openCV to build the image pipeline to get to the object in question both at training and at inference time.



## What is OpenCV ( background)?

It stands for Open Source Computer Vision Library. It includes a number of functions built to solve vision related problems. It is written in C++ with bindings in Python, Java, Matlab & a limited subset in JavaScript.

https://en.wikipedia.org/wiki/OpenCV

It was initially launched by Intel in 1999 and has not evolved to an openSource project supported and maintained by the community.









# Chapter 1 –Basics of an Image

## What we will cover in this chapter?

This is the absolute beginning. We will start by understanding:

- what is an image
- how is it loaded
- how do we display it
- how do we modify it
- how do we build it

And then we will solve our first vision problem of encoding a secret message in the mona lisa painting. Let's Begin

### Read, print & Show

```
image = cv2.imread('./path/to/file.jpg')
cv2.imshow('window.me', image)
print(image)
print(image.shape)
```

### Convert to grayscale

```
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image)
print(image.shape)
```

### Manipulate Image Data

```python
image[4] = 0
print(image)
print(image)
```

### Resize an Image

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

### Crop an image to get ROI

```python
face = image[60:160,320:420] # rows first and then columns
```

- This is using numpys ability to access specified elements in each dimension. 

- It is inclusive of first element and not inclusive of last element specified in range.

```python
face = image[60:160][320:420] # this is not the same
```

- When we access via sqaure brackets we are changing the shape as we are just getting elements back.

## Coding Session

### Random Binary Image

We will  build a Binary image with random values

[Build Binary Image](https://raw.githubusercontent.com/mistersingh179/opencv-fundamentals/master/code_examples/Chapter_1_Basics_of_an_image/build_binary_image_with_random_values.py)

### Random Grayscale Image

We will build a Grayscale Image with random values

[Build Grayscale Image](https://raw.githubusercontent.com/mistersingh179/opencv-fundamentals/master/code_examples/Chapter_1_Basics_of_an_image/build_random_grayscale_image.py)

### Random Color Image

We will build a color image with random values

[Build Color Image](https://raw.githubusercontent.com/mistersingh179/opencv-fundamentals/master/code_examples/Chapter_1_Basics_of_an_image/build_random_color_image.py)

## Project

### Secret Message in the Mona Lisa Painting

This is our first Vision Problem. We will encode a secret message in the Mon Lisa Painting and then later will work on decoding the image and extract the message

[Encode message in Mona Lisa](https://raw.githubusercontent.com/mistersingh179/opencv-fundamentals/master/code_examples/Chapter_1_Basics_of_an_image/mona-lisa-decode-secret-message.py)

[Decode message in Mina Lisa](https://raw.githubusercontent.com/mistersingh179/opencv-fundamentals/master/code_examples/Chapter_1_Basics_of_an_image/mona-lisa-decode-secret-message.py)

# Chapter 2 – Basics of a Video

## What's video all about and what will we learn?

So we now understand what an image is and ready to move on to Videos. It turns out that videos are not much different. Video is nothing but lots of images coming in at a speed normally higher than 24 per second. In this chapter we will cover:

- Reading a video from file
- Writing new a video file
- Reading video from camera

And then we will tackle our first video based vision problem of reading video from file and then building new video file with time elapsed stamped on it.

## Coding Session

### Reading from video file

Here we are getting the image by calling `vs.read()`. This image is just a normal image. Its a matrix in BGR format. All knowldge of image processing applies to it.

[Read video stream from a video file](https://raw.githubusercontent.com/mistersingh179/opencv-fundamentals/master/code_examples/Chapter_2_Basics_of_a_video/reading_from_video_file.py)

### Writing to a video file

Now lets read the video, inspect each frame and build our new video from the frames.

**Note**: regardless of how fast your write the frame, the file is build based on the FPS you set up in the writer. So there is now need to slow down the writing. This is different than if you were showing this in a window where your speed of sending data to the window will control the FPS in the window.

```
while True:
    frame = vs.read()[1]
    cv2.imshow('frame', frame)
    cv2.waitKey(10)
```

Above adds 10ms delay so the frame window will be playing at 100FPS provided we can read that fast. Normally this showing in video frame is only for debugging and thus the exact FPS being off is not an issue.

For `fourcc` codec we have: `mjpg`, `divx` and `h264` and for file extensions we have `avi`, `mp4` and `mov`.

Note: It takes data in BGR, so just convert to that format before writing. Also the dimensions need to match what were specified. The speed of writing is irrelevant as FPS goes by what has been specified

[Write to video stream to a file](https://raw.githubusercontent.com/mistersingh179/opencv-fundamentals/master/code_examples/Chapter_2_Basics_of_a_video/writing_to_video_file.py)

### Reading from camera

Just like how we read from file, we call `cv2.VideoCapture` but instead of passing in file path we pass in camera device number.

[Read video stream from camera](https://raw.githubusercontent.com/mistersingh179/opencv-fundamentals/master/code_examples/Chapter_2_Basics_of_a_video/readind_from_camera.py)

## Project

### Read a video file & Write a directot's cut Video file

Lets now put to practice what we have learned. We will open a video file, put the number of seconds which have elapsed since the video started and then write that frame witht timestamp to our output. This would be kinda like those director cut videos you may seen.

# Chapter 3 – Binary Images

Now that we know what an image is, and that a video just produces images, we are ready to learn how to process these image. Image processing, is the art & science of manipulating an image so that we can extract what we want from it with ease.

There are many, many operations which are done in image processing. To keep things interesting we will start with a vision problem and then study the operations required to solve the vision problem.

## Vision Problem: Count M&M's

We have a picture of a few M&M's and we want to know how many we have in front of us. Our first goal is to build a binary image. 

## To do so we will study:

- Gray Color Scheme
- Image Blur
- Binary Image
  - Thresholding
    - Simple Thresholding
    - Adaptive Thresholding
    - Otzu Thresholding
    - InRange
    - Canny

# Chatper 4 – Contour Extraction

So we have a binary image. Now we need to extract these contours and count them.

## Vision Problem: Count M&M's

Let's continue on our existing vision problem. At this point we have a binaru image and we need to count how M&M's are there.

## To do so we will study:

- Finding Contours
  - External
  - List
  - Tree
- Drawing Contours
- Writing on Image
- Contour Area



# Chapter 5 – Color Thresholding

In this chapter we will build upon our knowledge of image processing and learn building of binary images based on color threshold.

## Vision Problem: Find the Queen

We have a picture of a game of carrom board. Our vision task is to find if the queen is still in the game or not.

## What will we cover in this chapter?

- We will use already learned things like - grayscale, blur, binary images & findContours
- LAB color scheme
- inRange produced binary images
- max contour extraction
- contour area



# Chapter 6 – Histographs & Color Schemes

We will continue our jounrey in to color schemes and learn to use hitographs. We will learn on an image and then apply the learning on a video.

## Vision Problem

We have to find employees on the factory floor. We will do this by looking for their T-Shirts.

## What will we learn in this chapter?

- color schemes
- historgraphs
- Contour extraction & analysis
- video analysis



# Chapter 7 – Real Life Project

In this chapter we will work on our final and most important project. We will use everything we have learned and learn more image processing techniques

<img src="https://s3.amazonaws.com/images.179ways.com/eggs_counting.jpg" alt="Number of eggs in the box"  />

## Vision Problem

Given a picture of a carton, we need to know how many eggs are inside it.

## What we will do in this chapter?

In addition to using and applying everything we have learned so far, we will learn the things itemized below. These seem like a lot, and they are and we will take our time working through this project as it is a real life project.

- Morphological Operations
  - Erode
  - Dilate
  - Morphological Gradient

- Contours
  - Finding Contours
    - External
    - List
    - Tree
  - Approximating Contours
  - Drawing Contours
- Convex Hull
- Shapes
  - Straight Bounding Rectangle
  - Minimum Enclising Circle
  - Rotated Rectangle
  - Eclipse
- ROI Extraction
- mask
- bitwise operations
- Contour Fetures
  - Centroid
  - Area
  - Permiter
- Filtering Contours

## Note on Deep Learning

We have gone through many many steps here to get to the eggs and then counted them. We used the heuristic that eggs are really white in color and circularish in shape. This may suffice in reality but is no where near perfect. Alternatley we could run each contour found inside the box through a deep learned algorithm and asked it if the contour represented an egg or not. 

Had this problem been slighter harder where inside the box we have:

- a golf ball which we dont want to count or
- a ping pong ball which again we dont want to count
- a cracked egg which again we dont want to count or
- a brown/golden egg which we yes do want to count or
- again a orange ping pong ball which we do want to count

Then Yes using the deep learned solution would be a must.  as it could learn by looking a large dataset of pictures and tell us if thing is an egg or not. But keep in in mind, even if we had used an image classification algorithm we would still use all the tools provided by openCV to build the image pipeline to get to the object in question both at training and at inference time.



# .

# .

# .

# .

# .

# .

# .

# .

# .

# .

# .

# .

# .

# .

# .

# Appendix – Extra Tic Tac Toe Project

- ~~Whose turn is it next in a game of Tick-Tac-Toe?~~
  - ~~Binaryimage~~
  - ~~contour a.lysis - square~~
  - ~~more contour a.lysis - countNonZero~~



# Appendix – Ping Pong Score Sheet Project

- ~~Determine results of a ping-pong league game~~ 
  - ~~Binaryimage~~
  - ~~contour paper extraction~~
  - ~~perspective transform~~
  - ~~contour a.lysis square~~
  - ~~arranging contours in right order~~
  - ~~counting non zeros~~
  - ~~Highlighting read values~~

<img src="https://s3.amazonaws.com/images.179ways.com/table_tennis_input_and_output.jpg" alt="Table Tennis Score Card Before and After" style="zoom: 50%;" />

