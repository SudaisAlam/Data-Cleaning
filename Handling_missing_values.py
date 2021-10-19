import pandas as pd
import numpy as np

Data = pd.read_csv("/Users/sudaisalam/Downloads/titanic/train.csv")

# How many missing Data points do we have?

missing_val_count = Data.isnull().sum()
print(missing_val_count)

# what's the percentage of missing  values?

total_values = np.product(Data.shape)
total_missing = missing_val_count.sum()

percentage = (total_missing/total_values) * 100
print(percentage)

## DROPPING MISSING VALUES METHOD

dropping = Data.dropna() #(NOT RECOMMENDED)
print(dropping.shape)

# DROPPING JUST THE COLUMNS WITH MISSING VALUES

dropping = Data.dropna(axis=1)
print(dropping.shape)


#### FILLING IN MISSING VALUES

filling = Data.fillna(0)
print(filling.head())

# replace all missing values that comes directly after it in the same column, 
# then replace all the remaining na's with 0

filling = Data.fillna(method='bfill', axis=0).fillna(0)
print(filling.head())