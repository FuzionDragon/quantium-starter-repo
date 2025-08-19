import pandas as pd

# 'product' filtered to only consist of 'Pink Morsels'
# New 'sales' field for each row, simply have it be 'quantity' * 'price'

file_0 = pd.read_csv('./data/daily_sales_data_0.csv')
file_1 = pd.read_csv('./data/daily_sales_data_1.csv')
file_2 = pd.read_csv('./data/daily_sales_data_2.csv')

all_files = pd.concat([file_0, file_1, file_2])

filtered_data = all_files.loc[all_files['product'] == "pink morsel"]
filtered_data['sales'] = filtered_data['quantity'] * filtered_data['price'].str.removeprefix('$').astype(float)

cleaned_data = filtered_data.drop(['product', 'quantity', 'price'], axis=1)

cleaned_data.to_csv('./data/pink_morsel_sales.csv', index=False)
