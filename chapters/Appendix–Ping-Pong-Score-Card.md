## Another Real Life OpenCV Example and our final Project

Below is a score-card filled out by each table, playing table-tennis at the neighborhood league. The league organizer reads each score card and enters the results in to the system. We want to remove relying on a human being to read the scores, interpret the results and then enter them. This presents a vision problem and OpenCV is being used to build the image pipeline to remove unnecessary things and focus on the ROI which is the box represing a win or loss. 



### A side note on the use of deep learning algorithm

The actual determination of Win/Lost could be done by a deep learning algorithm but in this case we will also be coding that logic directly using OpenCV as the logic is straightforward and I want to use every opportunity to teach you more OpenCV.

<img src="https://s3.amazonaws.com/images.179ways.com/table_tennis_score_card_2.gif1" alt="Table Tennis Score Card" style="zoom:50%;" />

- Read Image in to a Matrix
- Change color scheme as the colors are irrelevant to the problem at hand
- blur the image to remove smudge, make edges smooth and remove picture defects
- build a binary image 
- detect edges of paper
- find contours detect various objects in the scene
- perform analysis on each contour to remove everything but the paper
- apply contour fixing to compensate for paper and picture defects
- fix the angle at which the paper sits, so the paper is in the center as if it was scanned in
- re-apply every step above again now on just the extracted paper
- extract each box
- arrange the boxes in a left to right, top to bottom way so they represt the order in which the players played each-other
- analyze each box and detect if its filled or not. This part could be done by a deep learning algorithm like an image classification algorith which detects cats vs dogs. But in this case we just count the number black pixels and white pixels. Using their ratio we can determine if the box is filled or not.
- Then for user confirmation purposes draw on the original sheet who won/loss and then process the results

Replace with counting eggs. **TODO**

Machine Learning could be used if there maybe a white ping pong ball, orange ping pong ball, white egg, brown egg, ostritch egg, broken egg or a golf ball. if we need to distinguish between them then yes apply deep learning, but the steps taken to get to that ROI are openCV and critical and necessary.