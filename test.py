import pandas as pd

df = pd.read_csv("train.csv", nrows=100)

print("haha")
print(df.sentimention.values_count())
