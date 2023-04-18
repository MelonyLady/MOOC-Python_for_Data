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
# ********************************************************SUPER USEFUL!! ***********************************************

pivot_avg_sale_price = df.pivot_table(index=['Category'], values=['Sale Price'], aggfunc={'mean', 'median', 'min', 'max'})
print(pivot_avg_sale_price)

print("*********************************************************************************************")

pivot_monthly_sales = df.pivot_table(index=['Month'], values=['Quantity Sold'], aggfunc='sum')
print(pivot_monthly_sales)

print("*********************************************************************************************")

pivot_monthly_sales_p_cust = df.pivot_table(index=['Month', 'Customer Name'], values=['Quantity Sold'], aggfunc='sum')
print(pivot_monthly_sales_p_cust)

print("*********************************************************************************************")

# total_sales = df.pivot_table(index=['Category', 'Product Name'], values=['Total_price'], aggfunc='Quantity Sold' * 'Sale Price')
# print(total_sales)