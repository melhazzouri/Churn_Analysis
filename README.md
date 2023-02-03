# Customer's Churn Predictions
The departure of customers can be costly for any business, which is why detecting dissatisfaction early allows companies to retain them by offering incentives. This notebook discusses the use of machine learning (ML) to automate the process of predicting customer churn, or identifying unhappy customers.

There are various methods for measuring the churn rate, including the number of customers lost, the percentage of customers lost in comparison to the company's total customer base, the value of recurring business lost, or the percentage of recurring value lost. However, in this particular dataset, it is defined as a binary variable for each customer, and determining the rate is not the focus. The idea of the churn rate implies that there are factors that affect it, so the objective is to identify and quantify those factors.

## Modelling
###  1. Machine Learning models
Several models were tested:
1- Logistic Regression
2- Support Vector Classifier
3- Decision Tree Classifier
4- K-nearest Classifier
5- Random Forest Classfier

### 2. Neural Networks
A basic neural network model is formed using an Artificial Neural Network (ANN). Hyperparameter tuning for learning rate and number of layers is done. The performance is constant at 0.77.

## Performance of the models
Performnce of all the models were compared. Logistic Regression resulted in the best performance of 81% accuracy. 

## Conclusuin and Feature's Importance

The analysis shows that Total Charges is the most critical feature, and for good reason. The primary reason for customers to "churn" is if they perceive the service as being too expensive or unaffordable.

Tenure is also an important factor, as customers who have been using the service for a long time or who have long-term contracts, which are usually cheaper, are less likely to churn. It's interesting to note that the neural network model considers Tenure to be even more important.

The EDA revealed that customers with month-to-month contracts are more likely to churn. This can be attributed to the customer's personal reasons for not wanting long-term commitments or the higher cost per unit time associated with monthly contracts.

Other important features, as seen in the EDA, include online security, electronic payment methods, fiber optic internet service, and tech support. Features that are not considered important are gender, dependents, partner, streaming TV, backup, and device protection. 

For further details see the notebooks in the repository.
