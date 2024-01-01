import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.preprocessing import StandardScaler

base_credit = pd.read_csv('credit_data.csv')

wrong_ages = base_credit.loc[base_credit['age'] < 0]
base_credit2  = base_credit.drop(base_credit[base_credit['age'] < 0].index)

base_credit.loc[base_credit['age'] < 0, 'age'] = base_credit2['age'].mean() # Replacing wrong ages 
del base_credit2

null_ages = base_credit.loc[pd.isnull(base_credit['age'])]

base_credit['age'].fillna(base_credit['age'].mean(), inplace=True) # Replacing empty ages

X_credit = base_credit.iloc[:, 1:4].values
Y_credit = base_credit.iloc[:, 4].values

scaler_credit = StandardScaler()
X_credit = scaler_credit.fit_transform(X_credit) # Standardizing data
print(X_credit[:,0].min())