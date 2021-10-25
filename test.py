import pandas as pd

df = pd.read_csv("train.csv", nrows=100)

print(df.head())
print(df.sentimention.values_count())
