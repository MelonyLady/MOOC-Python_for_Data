import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_dataset.csv')

df['Total Sales'] = df['Quantity Sold'] * df['Sale Price']


# plt.bar(df['Month'], df['Total Sales'])
# plt.title('Total Sales per Month', fontsize=14)
# plt.xlabel('Month', fontsize=14)
# plt.xticks(rotation=30, horizontalalignment="center")
# plt.ylabel('Total Sales', fontsize=14)
# plt.grid(True)
# plt.show()
#
# df.groupby(['Month']).sum().plot(kind='pie', y='Total Sales', autopct='%1.0f%%',
#                                  title='Percentage of Sales per Month')
# plt.show()


print("Total Sales by Month in descending order")
print()


monthly_sales = df.pivot_table(index=['Month'], values=['Total Sales'], aggfunc='sum')
print(monthly_sales.sort_values(by=['Total Sales'], ascending=False))


