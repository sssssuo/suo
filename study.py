import pandas as pd

df = pd.read_csv("./data_analysis/aug_train.csv")

mvalue = df["gender"].isnull()
sumOfValue = mvalue.sum()
print(sumOfValue)