

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

* Derivation of Loss Function

1. Given a dataset $\\{(\bf x_i, y_i) \\}_i^N$, where $\bf x_i$ represents the input features and $y_i$ represents the corresponding binary output (0 or 1) 

2. The likelihood function is

$$
L({\bf w}) = \prod_i^N \ p(y_i|{\bf x_i}; {\bf w})
$$

Taking the logarithm of the likelihood function, we get the log-likelihood:

$$
l({\bf w}) = \log L({\bf w}) = \sum_i^N \ p(y_i|{\bf x_i}; {\bf w})
$$

3. We want to maximize the likelihood (or log-likelihood) function, which is equivalent to minimizing the negative log-likelihood, Therefore, the loss function for logistic regression is the negative log-likelihood:

$$
J({\bf w}) = - l({\bf w}) = -\sum_i^N \ p(y_i|{\bf x_i}; {\bf w})
$$


4. For logistic regression, we have

$$
  p(y_i|{\bf x_i}; {\bf w}) = \left \{ \right
$$




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



