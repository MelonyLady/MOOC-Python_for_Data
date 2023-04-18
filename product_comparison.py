import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('csv_files/sales_dataset.csv')


# creation of Total Sales column
df['Total Sales'] = df['Quantity Sold'] * df['Sale Price']


#  create a table  to find the Total Sales for each product sorted from highest to lowest
product_sales = df.groupby('Product Name')['Total Sales'].max().reset_index().sort_values(['Total Sales'], ascending=False)

# write to csv file
product_sales.to_csv('csv_files/product_sales.csv')


# bar chart for Total Product Sales
plt.bar(df['Product Name'], df['Total Sales'])
plt.title('Total Product Sales', fontsize=14)
plt.xlabel('Product Name', fontsize=14)
plt.xticks(rotation=90, horizontalalignment="center")
plt.ylabel('Total Sales (£)', fontsize=14)
plt.grid(True)
plt.show()


# create a table  to find the average sale price for each category sorted from highest to lowest
avg_sale_price = df.groupby('Category')['Sale Price'].mean().reset_index().sort_values(['Sale Price'], ascending=False)

# write to csv file
avg_sale_price.to_csv('csv_files/avg_sale_prices.csv')

# bar chart for average sale price
df2 = pd.read_csv('csv_files/avg_sale_prices.csv')
colours = ['#f0a8ef', '#a8b2f0', '#a8f0ca', '#caa8f0', '#eaf0a8', '#f0a8a8', '#92ada1', '#a092ad', '#966083', '#968360',
           '#4d7a48', '#5a487a']

plt.bar(df2["Category"], df2["Sale Price"], color=colours)
plt.title("Average Sale Price Across Category of Product", fontsize=16)
plt.xlabel("Product Category", fontsize=14)
plt.ylabel("Average Price (£)", fontsize=14)
plt.grid(True)
plt.show()


print("Total Sales by Product in descending order")
print()
print(product_sales)
print()
print()
print('Average Sale Price per Category')
print()
print(avg_sale_price)
