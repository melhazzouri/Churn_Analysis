# -*- coding: utf-8 -*-
"""Untitled38.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eBgHE1tPNTiFLjJLCQHk_UsykkFLNXr8
"""

# Commented out IPython magic to ensure Python compatibility.
# Import Necessary Libraries
import pandas as pd
import numpy as np
import plotly.offline as po
import plotly.graph_objs as go
from matplotlib import pyplot as plt
# %matplotlib inline

#Import Customer Churn Dataset
churn_dataset = pd.read_csv('Tel_Customer_Churn_Dataset.csv')
churn_dataset.head()

# Number of Columns and Rows in the Dataset
churn_dataset.shape

# Types of columns in the Dataset
churn_dataset.dtypes

# Convert 'Total Charges' column values to float data type
### Glance at above makes me realize that TotalCharges should be float but it is an object.
churn_dataset.TotalCharges.values

### Remove rows with space in TotalCharges
churn_dataset.iloc[488].TotalCharges
churn_dataset= churn_dataset[churn_dataset.TotalCharges!=' ']
churn_dataset.shape

churn_dataset.TotalCharges = pd.to_numeric(churn_dataset.TotalCharges)
churn_dataset.dtypes

# Convert 'No internet service' and 'no phone service' to 'No' 
churn_dataset.replace('No internet service','No',inplace=True)
churn_dataset.replace('No phone service','No',inplace=True)



# Convert String values (Yes and No) in  columns to 1 and 0
yes_no_columns = ['Partner','Dependents','PhoneService','MultipleLines','OnlineSecurity','OnlineBackup',
                  'DeviceProtection','TechSupport','StreamingTV','StreamingMovies','PaperlessBilling','Churn']
for col in yes_no_columns:
    churn_dataset[col].replace({'Yes': 1,'No': 0},inplace=True)

# Drop Customer ID column
churn_dataset.drop('customerID',axis='columns',inplace=True)

# Convert Male and Female in gender to 0 and 1
churn_dataset['gender'].replace({'Female':1,'Male':0},inplace=True)

# Perform One Hot Encoding using get_dummies method for the categorical columns
churn_dataset = pd.get_dummies(data= churn_dataset, columns=['InternetService','Contract','PaymentMethod'])
churn_dataset.columns



# Churn Dataset
churn_dataset.sample(5)

# Churn Dataset shape
churn_dataset.shape

# Churn Dataset Data Types
churn_dataset.dtypes

# Visualize Total Customer Churn
plot_by_churn_labels = churn_dataset["Churn"].value_counts().keys().tolist()
plot_by_churn_values = churn_dataset["Churn"].value_counts().values.tolist()

plot_data= [
    go.Pie(labels = plot_by_churn_labels,
           values = plot_by_churn_values,
           marker = dict(colors =  [ 'Teal' ,'Grey'],
                         line = dict(color = "white",
                                     width =  1.5)),
           rotation = 90,
           hoverinfo = "label+value+text",
           hole = .6)
]
plot_layout = go.Layout(dict(title = "Customer Churn",
                   plot_bgcolor  = "rgb(243,243,243)",
                   paper_bgcolor = "rgb(243,243,243)",))


fig = go.Figure(data=plot_data, layout=plot_layout)
po.iplot(fig)

# Visualize Churn Rate by Gender
plot_by_gender = churn_dataset.groupby('gender').Churn.mean().reset_index()
plot_data = [
    go.Bar(
        x=plot_by_gender['gender'],
        y=plot_by_gender['Churn'],
        width = [0.3, 0.3],
        marker=dict(
        color=['orange', 'green'])
    )
]
plot_layout = go.Layout(
        xaxis={"type": "category"},
        yaxis={"title": "Churn Rate"},
        title='Churn Rate by Gender',
        plot_bgcolor  = 'rgb(243,243,243)',
        paper_bgcolor  = 'rgb(243,243,243)',
    )
fig = go.Figure(data=plot_data, layout=plot_layout)
po.iplot(fig)

# Visualize Churn Rate by Tech Support
plot_by_techsupport = churn_dataset.groupby('TechSupport').Churn.mean().reset_index()
plot_data = [
    go.Bar(
        x=plot_by_techsupport['TechSupport'],
        y=plot_by_techsupport['Churn'],
        width = [0.3, 0.3, 0.3],
        marker=dict(
        color=['orange', 'green', 'teal'])
    )
]
plot_layout = go.Layout(
        xaxis={"type": "category"},
        yaxis={"title": "Churn Rate"},
        title='Churn Rate by Tech Support',
        plot_bgcolor  = 'rgb(243,243,243)',
        paper_bgcolor  = 'rgb(243,243,243)',
    )
fig = go.Figure(data=plot_data, layout=plot_layout)
po.iplot(fig)

# Visualize Relation between Tenure & Churn rate
plot_by_tenure = churn_dataset.groupby('tenure').Churn.mean().reset_index()
plot_data = [
    go.Scatter(
        x=plot_by_tenure['tenure'],
        y=plot_by_tenure['Churn'],
        mode='markers',
        name='Low',
        marker= dict(size= 5,
            line= dict(width=0.8),
            color= 'green'
           ),
    )
]
plot_layout = go.Layout(
        yaxis= {'title': "Churn Rate"},
        xaxis= {'title': "Tenure"},
        title='Relation between Tenure & Churn rate',
        plot_bgcolor  = "rgb(243,243,243)",
        paper_bgcolor  = "rgb(243,243,243)",
    )
fig = go.Figure(data=plot_data, layout=plot_layout)
po.iplot(fig)

#Perform Feature Scaling 
cols_to_scale = ['tenure','MonthlyCharges','TotalCharges']

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
churn_dataset[cols_to_scale] = scaler.fit_transform(churn_dataset[cols_to_scale])

#Split the data into training set (80%) and test set (20%)
X = churn_dataset.drop('Churn',axis='columns')
y = churn_dataset['Churn']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=5)

# Machine Learning classification model libraries
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics

# Logistic Regression
### Fit the logistic Regression Model
logmodel = LogisticRegression(random_state=50)
logmodel.fit(X_train,y_train)

### Predict the value for new, unseen data
pred = logmodel.predict(X_test)

### Find Accuracy using accuracy_score method
logmodel_accuracy = round(metrics.accuracy_score(y_test, pred) * 100, 2)

print(logmodel_accuracy)

# Support Vector Classifier 
### Fit the Support Vector Machine Model
svcmodel = SVC(kernel='linear', random_state=50, probability=True)
svcmodel.fit(X_train,y_train)

### Predict the value for new, unseen data
svc_pred = svcmodel.predict(X_test)

### Find Accuracy using accuracy_score method
svc_accuracy = round(metrics.accuracy_score(y_test, svc_pred) * 100, 2)

print(svc_accuracy)

# K-Nearest
### Fit the K-Nearest Neighbor Model
from sklearn.neighbors import KNeighborsClassifier
knnmodel = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2) #p=2 represents Euclidean distance, p=1 represents Manhattan Distance
knnmodel.fit(X_train, y_train) 
  
### Predict the value for new, unseen data
knn_pred = knnmodel.predict(X_test)

### Find Accuracy using accuracy_score method
knn_accuracy = round(metrics.accuracy_score(y_test, knn_pred) * 100, 2)

print(knn_accuracy)

# Decision Tree
### Fit the Decision Tree Classification Model
from sklearn.tree import DecisionTreeClassifier
dtmodel = DecisionTreeClassifier(criterion = "gini", random_state = 50)
dtmodel.fit(X_train, y_train) 
  
### Predict the value for new, unseen data
dt_pred = dtmodel.predict(X_test)

### Find Accuracy using accuracy_score method
dt_accuracy = round(metrics.accuracy_score(y_test, dt_pred) * 100, 2)

print(dt_accuracy)

# Random Forest
### Fit the Random Forest Classification Model
from sklearn.ensemble import RandomForestClassifier
rfmodel = RandomForestClassifier(n_estimators = 100, criterion = 'entropy', random_state = 0)
rfmodel.fit(X_train, y_train) 
  
### Predict the value for new, unseen data
rf_pred = rfmodel.predict(X_test)

### Find Accuracy using accuracy_score method
rf_accuracy = round(metrics.accuracy_score(y_test, rf_pred) * 100, 2)

print(rf_accuracy)

# Build a model (ANN) in tensorflow/keras
import tensorflow as tf
from tensorflow import keras


model = keras.Sequential([
    keras.layers.Dense(26, input_shape=(26,), activation='relu'),
    keras.layers.Dense(15, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

opt = keras.optimizers.Adam(learning_rate=0.01)

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=200)

test_loss, test_acc= model.evaluate(X_test, y_test)
ANN_accuracy = test_acc*100

# Compare Several models according to their Accuracies
Model_Comparison = pd.DataFrame({
    'Model': ['Logistic Regression', 'Support Vector Machine', 'K-Nearest Neighbor', 
              'Decision Tree', 'Random Forest', "Artificial Neural Network"],
    'Score': [logmodel_accuracy, svc_accuracy, knn_accuracy, 
              dt_accuracy, rf_accuracy, ANN_accuracy]})
Model_Comparison_df = Model_Comparison.sort_values(by='Score', ascending=False)
Model_Comparison_df = Model_Comparison_df.set_index('Score')
Model_Comparison_df.reset_index()

#Generate confusion matrix for logistics regression model as it has maximum Accuracy
from sklearn.metrics import confusion_matrix
conf_mat_logmodel = confusion_matrix(y_test,pred)
conf_mat_logmodel

import seaborn as sn
cm = tf.math.confusion_matrix(labels=y_test,predictions=pred)

plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

# Predict the probability of Churn of each customer
churn_dataset['Probability_of_Churn'] = logmodel.predict_proba(churn_dataset[X_test.columns])[:,1]

# Create a Dataframe showcasing probability of Churn of each customer
churn_dataset[['Probability_of_Churn']].head()
churn_dataset.head()
