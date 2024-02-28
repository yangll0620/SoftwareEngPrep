

### logistic regression

* Hypothesis Function
  
$$
    f(x) = g(\bf w^T \bf x + \bf b) \\
$$

$$
    g(z) = \frac{1}{1 + e^{-z}}
$$


* [Lost Function](LossFunction.md)

$$ argmin (-\sum_i (y_ilog\ \hat{y_i} + (1-y_i)log \ (1-\hat{y_i})))$$

* Regularization 

    Lasso Regression (L1)

    Ridge Regression (L2)

The key differences between L1 and L2 regularizations is that L1 shrinks the less important features' coefficient to zero, thus removing some feature. So, this works well for feature selection in case we have huge number of features.

### Linear regression
* Hypothesis Function

$$
    f(x) = \bf w^T \bf x + \bf b \\
$$


* [Lost Function](LossFunction.md)

$$ argmin_\bf w \sum_i {(y_i - \hat{y_i})^2}$$


### SVM



