import pandas as pd


dados = pd.read_csv('Coffe_sales.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

print(dados)