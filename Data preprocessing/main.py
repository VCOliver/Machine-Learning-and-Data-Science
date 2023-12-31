import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

base_credit = pd.read_csv('credit_data.csv')

wrong_ages = base_credit.loc[base_credit['age'] < 0]
base_credit2  = base_credit.drop(base_credit[base_credit['age'] < 0].index)

base_credit.loc[base_credit['age'] < 0, 'age'] = base_credit2['age'].mean()

print(base_credit.head(27))