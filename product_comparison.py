import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('csv_files/sales_dataset.csv')


df['Total Sales'] = df['Quantity Sold'] * df['Sale Price']



plt.bar(df['Product Name'], df['Total Sales'])
plt.title('Total Product Sales', fontsize=14)
plt.xlabel('Product Name', fontsize=14)
plt.xticks(rotation=90, horizontalalignment="center")
plt.ylabel('Total Sales', fontsize=14)
plt.grid(True)
plt.show()

print()
print()
print("Total Sales by Product in descending order")
print()
print(df.groupby('Product Name')['Total Sales'].max().reset_index().sort_values(['Total Sales'], ascending=False))

print()
print()
print('Average Sale Price per Category')
print()
print(df.groupby('Category')['Sale Price'].mean())
