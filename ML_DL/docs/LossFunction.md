## Loss Function

### Mean Squared Error (MSE)

MSE (mean squared error) is a commonly used loss fucntion in regression problems. 

$$ MSE = \frac{1}{n}\sum_i(y - \hat y)^2$$

where $y$ represents the true or target variables, and $\hat y$ represents the predicted values.



### Cross Entropy

Cross entropy loss, also known as log loss or negative log-likelihood loss, is a commonly used loss function in classification problems.
    
* Binary Cross Entropy Loss

Binary cross entropy loss $ = -(ylog {\hat p} + (1-y)log(1-\hat p))$

where $y$ represents the actual label, and $p$ is the predicted probability of label 1. 

![](figures/binary_crossentropy_loss.png)


* Categorical Cross Entropy Loss

Categorical cross entropy loss, also known as softmax loss or multi-class log loss, is commonly in multi-class classification problems.

Categorical Cross Entropy loss $ = -\sum_i y_ilogp_i$

where $y_i$ represents the true class labels in one-hot encoded format, and $p_i$ is the predicted class probabilities.

* Sparse Categorical Cross Entropy Loss

The formula is the same as that for categorical cross entropy loss, but it takes into account the integer-encoded class labels instead of one-hot encoded labels.

### Hinge Loss

Hinge loss, also known as max-margin loss, is a loss function commonly used in support vector machine (SVM).

Hinge Loss = $max(0, 1- y * \hat y)$

where $y$ represents the true class label (+1 or -1), and $\hat y$ represent the predicted class labels or scores.

Hinge loss penalizes the model when the predicted score and the true label have opposite signs and are not separated by a margin of at least 1.


### KL Divergence & Cross Entropy

(ChatGPT)

KL divergence, short for Kullback-Leibler divergence, is a measure of the differernce between two probability distributions. 


$$ 

    DL_{KL}(P||Q) := \sum_{i=1}^m p_i \cdot (f_Q(q_i) - f_P(p_i)) \\

    = \sum_{i=1}^m pi \cdot ((-log_2q_i) -(-log_2 p_i) ) \\

    = \sum_{i=1}^m p_i \cdot (-log_2q_i) - \sum_{i=1}^m p_i \cdot (-log_2p_i)
$$ 
where $P$ is the base probability distribution. It measures for distribution $P$ from distribution $P$ the exprected additional amount of information required.


- The latter part $\sum_{i=1}^m p_i \cdot (-log_2p_i)$ of $DL_{KL}(P||Q)$ is the entropy of the base probability distribution $P$, thus it is a constant variable.

- It is proved that the first part $\sum_{i=1}^m p_i \cdot (-log_2q_i)$ is alwarys larger than the second part $\sum_{i=1}^m p_i \cdot (-log_2p_i)$, thus $DL_{KL}(P||Q)$ is larger than zero. And the first part is the cross entropy $H(P, Q)$.



![王木头学科学]https://www.youtube.com/watch?v=NgMa8H_8p8M&list=PLxIHUhMHF8okwhq8poRuiHBChWjkVUHLL&index=5


