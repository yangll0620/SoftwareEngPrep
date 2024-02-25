## Overfitting and Underfitting

### Bias and Variance

Bias and variance describe different aspects of a model's performance and generalization ability.

Let $Y$ be the true value of a variable, and $\hat Y$ be the estimator of $Y$ based on sample data:

Bias is the difference between the expected value of the predicted values and the actual value.
$$
    Bias(\hat Y) = E(\hat Y) - Y
$$

Variance is the expected value of the square of the difference between predicted values and the expected value of the predicted values.
$$
    Variance(\hat Y) = E((\hat Y - E(\hat Y))^2)
$$

Bias:

- Bias measures the systematic error in the predictions of a model.

- It reflects how closely the average prediction of the model matches the true value or target value across different training datasets.

- A model with high bias tends to oversimplify the underlying patterns in the data and may underfit the training data.

- Common causes of bias include using an overly simple model that cannot capture the true relationship between features and target, or having insufficient features to represent the underlying complexity of the data.

- High bias can lead to poor performance on both training and test data (high training error and high test error).

Variance:

- Variance measures the variability or sensitivity of the model's predictions to fluctuations in the training data. It reflects how much the predictions of the model vary across different training datasets.

- A model with high variance tends to capture noise or random fluctuations in the training data and may overfit the training data.
Overfitting occurs when the model learns the training data too well, including its noise and random variations, leading to poor generalization to new, unseen data.

- Common causes of variance include using a highly complex model that can fit the training data too closely, or having insufficient training data to estimate the model parameters reliably.

- High variance can lead to low training error but high test error (overfitting), indicating poor generalization to new data.



### Overfitting

ref: ChatGPT

Overfitting is a common issue in machine learning models where the model performs very well on the training data but fail to generalize well to new, unseen data. It occurs when the model becomes too complex and starts to memorize the noise or random flutuations in the training data instead of learning the underlying patterns or relationships.

Key causes and ways to address overfitting:

* Insuffient Training data

Having a small training dataset can lead to overfitting because the model may not have enough sample data to learn the underlying patterns.

Gathering more data or considering [data augmentation](Augmentation.md)  techniques.

* Model Complexity

A complex model with a large number of parameters can easily memorize the noise, random flutuations etc.

Reducing the number of layers, hidden units, or using regularization techniques.

* Lack of regularization

L1 and L2 regularization add a penalty term to the loss function to limit the magnitude of the model's weights.

Dropout: Random deactivates a certain percentage of neurons during training.

* Early Stopping

Monitoring the model's performance on the validation set and stopping the training when the performance starts to degrade.

* Cross-validation

A technique measures the model's performance on multiple subsets of the data. It helps to evaluate the models' generalization ability and detect overfitting. 

* Feature Selection


The goal is to find the balance between model complexity and generalization performance.


### Underfitting

Underfitting occurs when a machine learning model is unable to capture the underlying patterns in the training data. It results in poor performance on both the training data and new, unseen data.  Underfitting typically happens when the model is too simple or lacks the capacity to learn the complexities of the data.

