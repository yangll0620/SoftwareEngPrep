# Ensemble Methods

Ensemble methods are techiniques in machine learning that combines the predictions of multiple base model (learners) to create a more robust and accurate predictive model. 

Common ensemble methods include:

* Bagging

    - bagging involves training multiple instance of the same model on different subsets of the training data. 
    - e.g. Random Forest

* Boosting

    - Boosting focuses on sequentially training multiple models, with each model giving more weight to the instances that the previous model misclassified. 
    - e.g. AdaBoost, Gradient Boosting (used in XGBoost), and LightGBM
        - AdaBoost: assigns weights to the training instances, increasing the importance of misclassified samples.

        - Gradient Boosting: build models sequentially by fitting each new model to the residuals of the previous model.


        - LightGBM: LightGBM is a gradient boosting framework known for its efficiency and speed. It uses a histogram-based learning method and is designed for large datasets.   

* Stacking
    - Stacking involves training multiple diverse models and using another model (often called a meta-learner) to combine their predictions.

