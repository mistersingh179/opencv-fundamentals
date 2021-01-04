# Introduction

## TL;DR

OpenCV helps remove unwanted things (aka noise) so that deep learning algorithms can be applied on the correct object of interest.



## Why are we learning OpenCV?

We want to solve vision related problems and OpenCV enables us to process images and build an image processing pipeline so we can simplify the problem or solve it completely. OpenCV enables us to do many of those pre-requisite things which needs to be done before deep learning can be applied. These are things which are part of the image pipeline, they are those pre-processing things which must be done to get to the region of interest, on which then you may apply deep learning.

For example:

- getting access to the camera
- getting access to images off network or camera
- read the image as a matrix
- convert color schemes
- remove high frequency noise
- remove salt & pepper noise
- remove glare from lighting
- remove shadows and changing shadows
- handle change in color which happens with moving indoor and outdoor, day and night, yellow bulbs and white bulbs
- remove background 
- remove foreground items which are not of interest
- detect the edges of the interest object and zooming in
- Computing position co-ordinates, dimensions and other properties of the interested object 
- etc. etc.

Some or all of the above mentioned operations are used to build an image processing pipeline to get to the real object we want to study and apply sophisticated machine learning algorithms. The deep learning algorithms are important but so are the steps needed to get to the object which needs to be studied. 

Additionally in many instances machine learning maybe an over-kill and it may make more sense to use heuristics and build the logic yourself. For example machine learning may make a lot of sense when we want to detect between a cat and dog, but if we want to detect the between a circle and a square then the logic to do so can coded directly with the help of OpenCV.

Many time you may end up solving all trivial things with openCV and removing them from the equation and leaving behind the harder vision problem for a deep learning algorithm.



## What if I don't learn it?

If you dont take the above mentioned steps then:

-  the problem unnecessarly becomes harder and expensive to solve
-  your deep learning algorithm many learn wrong things 
- or it may take a lot longer to learn
- or it may overfit 
- and you maybe running in circles trying to fit a square peg in circlular hole
- in other words you will be over-engineering things which have simpler and more elegant solutions

I guess what i am trying to say is that there is a scappel and then there is a bazooka. Its best to know both rather than pulling out the bazooka on every occasion.



## What is OpenCV ( background)?

It stands for Open Source Computer Vision Library. It includes a number of functions built to solve vision related problems. It is written in C++ with bindings in Python, Java, Matlab & a limited subject in JavaScript.

https://en.wikipedia.org/wiki/OpenCV

It was initially launched by Intel in 1999 and has not evolved to an openSource project supported and maintained by the community.



## A Real Life OpenCV Example and our final Project

Below is a carton of eggs and we want to know how many eggs are in it. This is a classic vision problem and we will use OpenCV to build the image pipeline to remove things outside the box and then count the number of eggs in the box

### A side note on the use of deep learning algorithm

The actual determination of whether the thing in the carton is an egg or not, can very well be done by a deep learning algorithm, but in this case we will use simple huristics and code the logic to detect an egg ourselves using OpenCV. On the other hand, if the problem had been slightly harder where inside the carton there could be:

- a golf ball or
- a ping pong ball or
- a cracked egg which we dont want to count or
- a brown/golden egg which we do want to count

Then Yes, absolutely we would want to make our lives easier and use a deep learning algorithm to decide if the thing is an egg or not. Even if we had used an image classification algorithm we would still use all the tools provided by openCV to build the image pipeline to get to the object in question both at training and at inference time.

### Image Pipeline steps

- load image in to a matrix
- Change color scheme as the colors are irrelevant to the problem at hand
- blur the image to remove smudge, make edges smooth and remove picture defects
- build a binary image 
- detect edges of the carton
- detect contours of various objects in the scene
- perform analysis on each contour to remove everything but the carton
- apply contour fixing to compensate for contour and picture defects
- extract just the contour box from the image
- re-apply every step above again now on just the carton
- build binary to detect eggs
- find all conoturs
- analyze each contours property and check for it to be an egg
- Store count of eggs and build new image with count stamped

<img src="https://s3.amazonaws.com/images.179ways.com/eggs_counting.gif" alt="Number of eggs in the box"  />