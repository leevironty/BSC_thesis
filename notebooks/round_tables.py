import pandas as pd
import os

#print(os.getcwd())

table_path = 'tables'

filenames = [f for f in os.listdir(table_path) if os.path.isfile(os.path.join(table_path, f)) and f[-4:] == '.csv']

roundings = {'10-fold_cv': 1, 'AIC': 1, 'DIC': 1, 'WAIC': 1, 'default_cv': 4}

for f in filenames:
  table = pd.read_csv(os.path.join(table_path, f))
  table = table.round(roundings)
  table.to_csv(os.path.join(table_path, 'rounded', f))