import csv
import pandas as pd


df = pd.read_csv('sales_dataset.csv')

print(df.to_string())

# print(df.info())

# group by
groupby_category = df.groupby(['Category']).count()

print(f'Grouped by Category: {groupby_category}')
print("*********************************************************************************************")

# Simple stats
mean_sale_price = df['Sale Price'].mean()
sum_products_sold = df['Quantity Sold'].sum()

print(f"total sale price mean: {mean_sale_price}")
print(f"Total Quantity of items sold: {sum_products_sold}")
print("*********************************************************************************************")


# attempt at pivot table
# ********************************************************SUPER USEFUL!! ***************************************************************************

pivot = df.pivot_table(index=['Category', 'Product Name'], values=['Sale Price'], aggfunc='sum')
print(pivot)
