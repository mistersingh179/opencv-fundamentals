# Convulation

Convulation is just a mathametical operation. The exact operation is:

- lay 2 matrixes on top of each other. 
- multiple each overlapping element. (Not all elements may overlap as the sizes are different)
- take the results we get after each pair is multiplied and then add it up to get 1 number i.e. the result
- place the result in the bigger matrix at the position which is at the center with the overlapping matrix.



### Process

- There is one big matrix (this is the image) and one much much smaller image (this is the kernel).
- Small matrix slides across left to right and top to bottom covnulating and change data of the image.
- Size of the output image is smaller by half of the size of the kernel as those regions didnt overlap with the center of the kernel.



## Kernel

- This is the name given to the smaller matrix.

- It moves around the bigger matrix, convulating and changing its data.
- The values and size of this kernel determine the effect of convulation and thus the output image.

- They are an odd number in size as this guarantees a center item



###  Various Kernels – Blur, Sharpen, Outline

```python
# https://en.wikipedia.org/wiki/Kernel_(image_processing)
blur_kernel = [
  [0.0625, 0.125, 0.0625],
  [0.125, 0.25, 0.125],
	[0.0625, 0.125, 0.0625]
]
sharpen_kernel = [
  [0, -1, 0],
  [-1, 5, -1],
  [0, -1, 0]
]
outline_kernel = [
	[-1, -1, -1],
  [-1, 8, -1],
  [-1, -,1, -1]
]
output = cv2.filter2D(gray, -1, kernel)
```

`cv2.filter2D` is doing the work of applying the kernel so we dont have to manually do all those operations.

Live example of applying various kernels: https://setosa.io/ev/image-kernels/

## Practical Use

Convulation is actually been happening everywhere in all those steps of image processing like detecting edges etc. We never actaully applied a kernel directly with filter2D, but instead used other methods which internally knew which kernel numbers to use and applied them. Every method which took kernel size was for this reason. It internally is convulating.