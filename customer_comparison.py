import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('csv_files/sales_dataset.csv')

df['Total Money Spent'] = df['Quantity Sold'] * df['Sale Price']

print("Total Money Spent by Customer in descending order")
print()
print(df.groupby('Customer Name')['Total Money Spent'].max().reset_index().sort_values(['Total Money Spent'], ascending=False))

customer_sales = df.pivot_table(index=['Customer Name', 'Product Name'], values=['Quantity Sold', 'Sale Price', 'Total Money Spent'])
print(customer_sales)
