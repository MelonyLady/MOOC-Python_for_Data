import csv
import pandas as pd


df = pd.read_csv('sales_dataset.csv')

print(df.to_string())
