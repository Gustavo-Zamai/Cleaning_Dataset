import pandas as pd

dataset = pd.read_csv('Data/zomato.csv')
pd.set_option('display.max_columns', None)
print(dataset)