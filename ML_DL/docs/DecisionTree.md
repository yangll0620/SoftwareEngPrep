# Decision Tree

## Tree Building

from chatGPT
- Decision trees are built in a recursive manner. The process starts at the root node, which selectes the feature and the threshold for splitting the data.

- The data is splitted into subsets based on this decision, and the process continues for each subset.

- The tree-building process continues until a stopping criterion is met. This might be a predefined depth limit, a minimum number of samples in a leaf, or until no further splits improve the model's performance.


### Selection Criterion and Different DT algorithms

- Information Gain

Information Gain measures the reduction in entropy or impurity achieved by partitioning a dataset based on a particular attribute of feature.

The information gain of T for attribute $\alpha$ the difference between the a priori Shannon entropy $H(T)$ of the training set and the conditional entropy $H(T|\alpha)$.

$$
    IG(T|\alpha) = H(T) - H(T|\alpha) 
$$
$$
    H(T|\alpha) = \sum_{v\in vals(\alpha)}\frac{|S_{\alpha(v)}|}{|T|}H(S_{\alpha}(v))
    $$

- Gini impurity:

$$
    Gini(p) = \sum_{k}p_k(1-p_k) 
    
    \\ = 1- \sum_k p_k^2
$$

- Algorithms:

    - ID3: informaiton gain
    - C4.5: Information gain rate
    - CART (classification and regression Tree): 
    



## Advantages:
from chatGPT

- Interpretability: Decision trees are easy to visualize and understand. They provide insights into how decisions are made.

- Simple to use: They don't require much data preprocessing or feature scaling.

- Handle both categorical and numerical data: Decision trees can work with a mix of feature types.

- Can be used for feature selection: The importance of features can be inferred from the tree.


## Challenges
from chatGPT

- Prone to overfitting: Decision trees can become very complex and overfit the training data. Techniques like pruning are used to mitigate this.

- Can be unstable: Small changes in the data can lead to different tree structures.

- Bias toward dominant classes: In imbalanced datasets, decision trees may have a bias toward the majority class.

- Limited expressiveness: Decision trees may not capture complex relationships as well as more advanced algorithms.

To mitigate some of these challenges, ensemble methods like random forests and gradient boosting are often used in conjunction with decision trees. 
