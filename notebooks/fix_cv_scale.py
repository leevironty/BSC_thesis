import pandas as pd
import pathlib

for fname in pathlib.Path(__file__).resolve().parents[1].joinpath('tables/rounded').iterdir():
  df = pd.read_csv(fname, index_col='model_name').drop(columns='Unnamed: 0')
  df['10-fold_cv'] = df['10-fold_cv'] * -2 
  df.to_csv(str(fname)[:-4] + '_fixed.csv')
