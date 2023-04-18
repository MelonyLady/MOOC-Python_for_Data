import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_dataset.csv')

df['Total Sales'] = df['Quantity Sold'] * df['Sale Price']

print("Total Sales by Month in descending order")
print()
monthly_sales = df.pivot_table(index=['Month'], values=['Total Sales'], aggfunc='sum')
sort_monthly_sales = monthly_sales.sort_values(by=['Total Sales'], ascending=False)


sort_monthly_sales.to_csv('month_comparisons.csv')

df2 = pd.read_csv('month_comparisons.csv')
months = df2["Month"]
totalsales = df2["Total Sales"]
plt.pie(totalsales, labels=months,
        autopct='%1.f%%',)
plt.title("Percentage of Sales each Month")
plt.show()
