import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('csv_files/sales_dataset.csv')


# creation of Total Sales column
df['Total Sales'] = df['Quantity Sold'] * df['Sale Price']

print("Total Sales by Month in descending order")
print()

# create table that uses the total Sales function and adds them based on month
monthly_sales = df.pivot_table(index=['Month'], values=['Total Sales'], aggfunc='sum')

# Sort table by Total Sales amount, largest to smallest
sort_monthly_sales = monthly_sales.sort_values(by=['Total Sales'], ascending=False)
print(sort_monthly_sales)


# write the sorted table to csv file
sort_monthly_sales.to_csv('month_comparisons.csv')


# colours to be used for charts
colours = ['#f0a8ef', '#a8b2f0', '#a8f0ca', '#caa8f0', '#eaf0a8', '#f0a8a8', '#92ada1', '#a092ad', '#966083', '#968360',
           '#4d7a48', '#5a487a']

# Pie Chart for percentages of sales per month
df2 = pd.read_csv('csv_files/month_comparisons.csv')
months = df2["Month"]
totalsales = df2["Total Sales"]
plt.pie(totalsales, labels=months, autopct='%1.f%%', colors=colours)
plt.title("Percentage of Sales each Month")
plt.show()


# Bar chart for total sales per month
plt.bar(df2["Month"], df2["Total Sales"], color=colours)
plt.title("Total Sales per Month", fontsize=16)
plt.xlabel("Month", fontsize=14)
plt.ylabel("Total Sales", fontsize=14)
plt.grid(True)
plt.show()


# closing statements
max_sales = df2['Total Sales'].max()
min_sales = df2['Total Sales'].min()

print()
print(f"The highest amount of money made in sales was £{max_sales} in Feb and the lowest amount was £{min_sales} in Oct.")
