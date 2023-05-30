## Different types of convolutions

### Convolutions

A few parameters: 
- kernal size
- Stride
- Padding

### Dilation

Dilated convolution is another variant of convolution in which the kernal is inflated as per a dilation rate prior to the process.

Parameter
- Dilation rate


### Separable Convolution
https://www.analyticsvidhya.com/blog/2021/11/an-introduction-to-separable-convolutions/

- Defination

    A separable convolution is a process in which a single process can be divided into two or more convolutions to produce the same output.

    Two types of main separable convolutions
    - Spatially Separable Convolutions
    - Depth-wise Separable Convolutions

- Advantages:
    - less number of parameters, reducing overfitting
    - fewer computations

- Spatially Separable Convolution

    In images, height and width are called spatial axes. The kernel that can be separeted across sptial axes is called the spatially separate kernel.

- Depth-wise Separable Convolution

    Each channel is convolved with a different kernel (called depthwise kernal).