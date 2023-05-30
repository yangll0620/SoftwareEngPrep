## Optimizer

Optimizers are methods or algorithms that are iteratively updating the model's parameters to minimize the [loss function](LossFunction.md).

### Types of optimizers

* Gradient Descent
    * Stochastic Gradient Descent
    * Mini-Batch Gradient Descent

* Newton's Method
* Momentum
* AdaGrad & AdaDelta
* RMSProp
* Adam & AdamW
* Nadam


### Gradient Descent

Steps:

1. Pick random values for the parameters

2. Computer the gradients

3. Plug the paramter values into the gradients, and calculate the Step Sizes: Step Size = learning_rate * gradient 

4. Calculte the new parameters: new_parameter = old_parameter - Step Size


Then repeat steps 3 and 4 for a specified number of iterations or until a convergence criterion is met.

The update equation is as follows:

$$ W_{t} = W_{t-1} - \eta * \nabla J_{t-1}$$

where $W$ is parameter vector, $\eta$ is learning rate, $J$ is the loss function.

Advantage

* Easy to understand 
* Easy to implement

Disadvantage

It calculates the gradient based on the entire data

* The calculation is very slow 

* Require large memory


Variants

* Stochastic Gradient Descent

One random selected sample is used to calculate the gradient and update the parameters in each iteration.

Advantage:

Faster Update Speed, Memory Efficiency, 

Avoidance of Local Minima: Due to the noisy updates in SGD, it has the ability to escape from local minima and converges to a global minimum.

Disadvantage:  

Noisy update: the updates in SGD are noisy and have a high variance, which can make the optimization process less stable and lead to oscillations around the minimum.

Slow convergence, Sensitive to Learning Reate, Less accurate


* Mini-batch Gradient Descent

A subset or mini-batch of the training data is used to update the parameter in each iteration.


### Momentum

Considering the history data for updating parameters.


$$ V_{t}^i = \beta V_{t-1}^i + (1- \beta)\Delta W_t^i  $$
$$ W_t^i = W_{t-1} - \eta V_{t} $$

where  $\Delta W_{t}^i = \frac{\partial J({W_{(t-1)}^i})}{\partial W^i}$,i represent dimension $i$.

### Nesterov

Considering the history data and the forward data for updating parameters.

$$ V_{t}^i = \beta V_{t-1}^i + (1- \beta)\Delta W_t^i  $$
$$ W_t^i = W_{t-1} - \eta V_{t} $$

where  $\Delta W_{t}^i = \frac{\partial J({W_{(t-1)}^i} + \gamma V_{t-1})}{\partial W^i}$,i represent dimension $i$.

### AdaGrad

$$ W_t^i = W_{t-1} - \frac{\eta}{\sqrt{S_t} + \epsilon} \Delta W_{t}^i $$
$$ S_t = S_{t-1} + \Delta W_{t}^i \cdot \Delta W_{t}^i $$

where  $\Delta W_{t}^i = \frac{\partial J({W_{(t-1)}^i})}{\partial W^i}$

Advantage:

1. Learning rate changes for each training parameter

2. Don't need to manually tune the learning rate

3. Able to train on sparse data

Disadvantage:

1. The learning rate is always decreasing results in slow training

### RMSProp 

RMSprop is short for root mean square propagation. Improved based on AdaGrad

$$ S_t = \beta S_{t-1} + (1- \beta )\Delta W_{t}^i \cdot \Delta W_{t}^i $$
$$ W_t^i = W_{t-1} - \frac{\eta}{\sqrt{S_t} + \epsilon} \Delta W_{t}^i $$

### Adam

Adam is short for adaptive moment estimation, which combines momentum and RMSProp.

$$ V_{t}^i = \beta_1 V_{t-1}^i + (1- \beta_1)\Delta W_t^i  $$
$$ S_t = \beta_2 S_{t-1} + (1- \beta_2 )\Delta W_{t}^i \cdot \Delta W_{t}^i $$
$$ W_t^i = W_{t-1}^i - \frac{\eta}{\sqrt{S_t} + \epsilon} V_{t}^i $$


### Nadam

Combines Nesterov and AdaGrad