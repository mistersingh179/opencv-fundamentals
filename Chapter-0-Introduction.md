# Introduction

## TL;DR

Helps remove unwanted things aka noise so that deep learning algorithms can be applied on the correct object of interest

## Why OpenCV?

In the world of machine learning and specifically in vision realted problems, OpenCV plays an important role in the processing pipe-line. It enables us to do many of those pre-requisite things which needs to be done before deep learning can be applied. These are things which are part of the image pipeline, they are those pre-processing things which must be done to get to the region of interest. For example:

- getting access to the camera
- getting access to images off network or camera
- read the image as a matrix
- convert color schemes
- remove high frequency noise
- remove salt & pepper noise
- remove glare from lighting
- remove background 
- remove foreground items which are not of interest
- detect the edges of the interest object and zooming in
- Computing position co-ordinates, dimensions and other properties of the interested object 
- etc. etc.

Some or all of the above mentioned operations are used to build an image processing pipeline to get to the real object we want to study and apply sophisticated machine learning algorithms. The deep learning algorithms are important but so are the steps needed to get to the object which needs to be studied.

Additionally in many instances machine learning maybe an over-kill and it may make more sense to use heuristics and build the logic yourself. For example machine learning may make a lot of sense when we want to detect between a cat and dog, but if we want to detect the between a circle and a square then the logic to do so can coded directly with the help of OpenCV.

Many time you may end up solving all trivial things with openCV and removing them from the equation and leaving behind the harder vision problem for a deep learning algorithm.

## What is OpenCV

It stands for Open Source Computer Vision Library. It includes a number of functions built to solve vision related problems. It is written in C++ with bindings in Python, Java, Matlab & a limited subject in JavaScript.

https://en.wikipedia.org/wiki/OpenCV

It was initially launched by Intel in 1999 and has not evolved to an openSource project supported and maintained by the community.

## Example

Below is a score-card filled out by each table playing table-tennis at the league. The lead organizer reads the score 