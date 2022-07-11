import pandas  as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
%matplotlib inline

plt.rcParams['figure.figsize'] = [8,5]
plt.rcParams['font.size'] =14
plt.rcParams['font.weight']= 'bold'
plt.style.use('seaborn-whitegrid')

X=df.loc[:,'Weight':'Width']
y=df['Species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
logreg=LogisticRegression(max_iter=100000).fit(X_train,y_train)
print("Training set score: {:.2f}".format(logreg.score(X_train, y_train)))
print("Test set score: {:.2f}".format(logreg.score(X_test, y_test)))
pred1=logreg.predict(X_test)
print(confusion_matrix(y_test,pred1))
print('\n')
print(classification_report(y_test,pred1))
#prediction
res = logreg.predict([[300,30.0,20.0,37.0,12.3,5.0]])
print("Predicted Type:", res)
