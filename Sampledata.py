import pandas as pd

netflix_data= pd.read_csv("netflix_titles.csv")

print(netflix_data.head())
print(netflix_data.shape)

missing_values_count = netflix_data.isnull() .sum()
print(missing_values_count[0:5])

dropcolumns = netflix_data.dropna(axis=1)
print(netflix_data.shape, dropcolumns.shape)

cleaned_data = netflix_data.fillna(0)

