import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('csv_files/sales_dataset.csv')


# creation of Total Sales column
df['Total Sales'] = df['Quantity Sold'] * df['Sale Price']


# bar chart for Total Product Sales
plt.bar(df['Product Name'], df['Total Sales'])
plt.title('Total Product Sales', fontsize=14)
plt.xlabel('Product Name', fontsize=14)
plt.xticks(rotation=90, horizontalalignment="center")
plt.ylabel('Total Sales', fontsize=14)
plt.grid(True)
plt.show()

product_sales = df.groupby('Product Name')['Total Sales'].max().reset_index().sort_values(['Total Sales'], ascending=False)
product_sales.to_csv('csv_files/product_sales.csv')

print()
print()
print("Total Sales by Product in descending order")
print()
print(product_sales)


avg_sale_price = df.groupby('Category')['Sale Price'].mean()
avg_sale_price.to_csv('csv_files/avg_sale_prices.csv')

print()
print()
print('Average Sale Price per Category')
print()
print(avg_sale_price)
