import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('sales_dataset.csv')


df['Total Sales'] = df['Quantity Sold'] * df['Sale Price']
product_sales = df.pivot_table(index=['Product Name'], values=['Quantity Sold', 'Sale Price', 'Total Sales'])
print(product_sales)


plt.bar(df['Product Name'], df['Total Sales'])
plt.title('Total Product Sales', fontsize=14)
plt.xlabel('Product Name', fontsize=14)
plt.xticks(rotation=90, horizontalalignment="center")
plt.ylabel('Total Sales', fontsize=14)
plt.grid(True)
plt.show()
