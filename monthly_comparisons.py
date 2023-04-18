import pandas as pd


df = pd.read_csv('sales_dataset.csv')

print(df.to_string())

df['Total Price'] = df['Quantity Sold'] * df['Sale Price']
monthly_sales = df.pivot_table(index=['Month', 'Product Name'], values=['Quantity Sold', 'Sale Price', 'Total Price'])
print(monthly_sales)
