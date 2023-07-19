### logistic regression

* Hypothesis Function
$$

    f(x) = g(\bold w^T \bold x + \bold b) \\
    g(z) = \frac{1}{1 + e^{-z}}
$$


* [Lost Function](LossFunction.md)

$$ argmin (-\sum_i (y_ilog\ \hat{y_i} + (1-y_i)log \ (1-\hat{y_i})))$$



### Linear regression
* Hypothesis Function

$$
    f(x) = \bold w^T \bold x + \bold b \\
$$


* [Lost Function](LossFunction.md)

$$ argmin_\bold w \sum_i {(y_i - \hat{y_i})^2}$$


### SVM



