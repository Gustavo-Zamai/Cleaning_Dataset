import pandas as pd

dataset = pd.read_csv('Data/zomato.csv')

# Print the 5 rows into top
#print(dataset.head())

# Shows datatypes of columns, range index, etc
#print(dataset.info())

## Delete redundant columns

# Show all the columns
#print(dataset.columns)
columns_to_keep = ['name', 'online_order', 'book_table', 'rate', 'dish_liked', 'approx_cost(for two people)']
columns_to_drop = ['url', 'address', 'votes', 'phone', 'location', 'rest_type','cuisines','reviews_list', 'menu_item', 'listed_in(type)', 'listed_in(city)']

# 1st way, filtering data
data = dataset[columns_to_keep]
#print(data)

# 2nd way, dropping the columns
dataset.drop(columns= columns_to_drop, inplace= True)
#print(dataset)

## Renaming the columns

# 1 by 1
# dataset.rename(columns= {"old_name":"new_name", "old_name_another_column":"new_name_another_column"}
# dataset.rename(columns= {"old_name":"new_name", "old_name_another_column":"new_name_another_column", inplace = True}, to save

# All columns
new_columns_name = []

for i in dataset:
    new_columns_name.append(i.capitalize())

dataset.columns = new_columns_name
#print(dataset)

## Dropping duplicates

#print(dataset.duplicated().value_counts())

dataset.drop_duplicates(inplace= True)

#print(dataset.duplicated().sum())


## Remove NaN values

dataset.dropna(inplace= True)

#print(dataset.isna().sum())
#print(dataset)

## Reset column index

dataset.reset_index(inplace=True)
dataset.drop(columns="index", inplace=True)

print(dataset)

## Cleaning individual columns

# remove unnecessary space
dataset["Rate"] = dataset["Rate"].str.replace(" ", "")

# simpify Yes and No to 1 and 0
dataset["Online_order"] = dataset["Online_order"].apply(lambda x: 1 if x == "Yes" else 0)

print(dataset)

dataset.to_csv("Data/Cleaned_csv_file.csv")
