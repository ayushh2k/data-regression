
import pandas  as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
%matplotlib inline

plt.rcParams['figure.figsize'] = [8,5]
plt.rcParams['font.size'] =14
plt.rcParams['font.weight']= 'bold'
plt.style.use('seaborn-whitegrid')

#Loading the Dataset
df = pd.read_csv('./dataset/Fish.csv')

sns.lmplot(x='Weight',y='Height',data=df,aspect=2,height=6)
plt.xlabel('Weight')
plt.ylabel('Height')
plt.title('Weight vs Height');
