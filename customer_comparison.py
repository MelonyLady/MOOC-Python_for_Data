import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('csv_files/sales_dataset.csv')

df['Total Money Spent'] = df['Quantity Sold'] * df['Sale Price']

print("Total Money Spent by Customer in descending order")
print()
# df.groupby('Customer Name')['Total Money Spent'].max().reset_index().sort_values(['Total Money Spent'], ascending=False)

customer_sales = df.pivot_table(index=['Customer Name'], values=['Total Money Spent'], aggfunc='sum')


sort_customer_sales = customer_sales.sort_values(by=['Total Money Spent'], ascending=False)
print(sort_customer_sales)

sort_customer_sales.to_csv('csv_files/customer_sales.csv')

df2 = pd.read_csv('csv_files/customer_sales.csv')

colours = ['#f0a8ef', '#a8b2f0', '#a8f0ca', '#caa8f0', '#eaf0a8', '#f0a8a8', '#92ada1', '#a092ad', '#966083', '#968360',
           '#4d7a48', '#5a487a']

plt.bar(df2["Customer Name"], df2["Total Money Spent"], color=colours)
plt.title("Total Customer Spending", fontsize=16)
plt.xlabel("Customer", fontsize=14)
plt.ylabel("Total Amount Spent", fontsize=14)
plt.grid(True)
plt.show()

