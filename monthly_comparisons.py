import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('sales_dataset.csv')


df['Total Sales'] = df['Quantity Sold'] * df['Sale Price']
# monthly_sales = df.pivot_table(index=['Month', 'Product Name'], values=['Quantity Sold', 'Sale Price', 'Total Sales'])
# print(monthly_sales)

plt.bar(df['Month'], df['Total Sales'])
plt.title('Total Sales per Month', fontsize=14)
plt.xlabel('Month', fontsize=14)
plt.xticks(rotation=30, horizontalalignment="center")
plt.ylabel('Total Sales', fontsize=14)
plt.grid(True)
plt.show()

df.groupby(['Month']).sum().plot(kind='pie', y='Total Sales', autopct='%1.0f%%',
                                 title='Percentage of Sales per Month')
plt.show()


print("Total Sales by Month in descending order")
print()
print(df.groupby('Month')['Total Sales'].max().reset_index().sort_values(['Total Sales'], ascending=False))
