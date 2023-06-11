### Mixed Precision

- Problem

There are various levels of floating-point precision, range from binary16 (half-precision) to binary256 (octuple-precision).

Deep learning has used single-precision (binary32, or FP32) to represent parameters. Due to the large amount of parameters in deep learning model, there is a great increament in the memory and compute requirements

- Mixede Precision Training

In 2017, NVIDIA proposed a technique called Mixed Precision Training to reduce the memory requirement. 

In the mixed precision training, FP16 is used instead to store the weights, activations and gradients during training iterations.


![Alt text](../figures/FP16_FP32.webp?raw=true "FP16 vs FP32") 
*FP16 vs FP32*

![Alt text](../figures/FP16_FP32_Range.webp?raw=true "FP16 vs FP32 Range and Precision") 
*FP16 vs FP32 Range and Precision*

reference to https://towardsdatascience.com/understanding-mixed-precision-training-4b246679c7c4

