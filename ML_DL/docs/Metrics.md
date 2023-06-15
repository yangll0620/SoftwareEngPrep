## Metrics to Evaluate ML/DL Algorithms

### Classification Performance Metrics

* Confusion Matrix

![Alt text](figures/ConfusionMatrix.jpg?raw=true "Confusion Matrix") 

* Sensitivity & Specificity

Sensitivity (recall, hit rate, true positive rate (TPR)):     $\frac{a}{a+c} $

Specificity (selectivity, true negative rate (TNR) ): $\frac{d}{b+d} $

Precision (positive predictive value): $\frac{a}{a+b} $

negative predictive rate: $\frac{d}{c+ d} $

Accuracy: $\frac{a+d}{a+b+c+d}$ 

* F1 score

$$ F1 = (\frac{recall^{-1} + precision^{-1}}{2})^{-1} = 2 \cdot \frac{precision \cdot recall}{precision + recall }$$

* ROC & AUC

An ROC curve (receiver operating characteristic curve) is a graph showing the performance of a classification model at all classification thresholds. It plots true positive rate (TPR) vs False positive rate (FPR)

AUC is the area under the ROC curve.

![Alt text](figures/ROC.jpg?raw=true "ROC curve")

ROC curve (downloaded from wiki https://en.wikipedia.org/wiki/Receiver_operating_characteristic)

    * ROC is used for identifying the best threshold while the AUC is used for identifying which model is better.

    * Note: people often replace false positive rate with precision.


### Regression Performance Metrics
* Mean Squre Error (MSE)
* Root Mean Squre Error (RMSE)