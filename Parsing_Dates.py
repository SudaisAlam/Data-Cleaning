import pandas as pd
import numpy as np
import seaborn as sns
import datetime

Data = pd.read_csv("catalog.csv")

Data['Parsing dates'] = pd.to_datetime(Data['date'], format="%m/%d/%y")

print(Data['Parsing dates'].head())

dof = Data['Parsing dates'].dt.day
dof = dof.dropna()
print(sns.displot(dof, kde=False, bins=31))