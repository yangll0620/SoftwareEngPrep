## Overfitting and Underfitting

### Bias and Variance

* Bias is the difference between the predictions of the model and the actual values. High bias can cause an algorithm to miss the relevant relations between features and target outputs (underfitting)

* Variance is the variability of model prediction. High variance may result from an algorithm modelling the random noise in the training data (overfitting).

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


Underfitting occurs when a machine learning model is unable to capture the underlying patterns in the training data. It results in poor performance on both the training data and new, unseen data. Underfitting typically happens when the model is too simple or lacks the capacity to learn the complexities of the data.


