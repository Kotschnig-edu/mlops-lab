import pandas  as pd

DATASET = "./data/raw/data.csv"

df = pd.read_csv(DATASET)
print(df.shape)
print(df.columns)
df.info()
print(df.isnull().sum())
print(df.describe())
print(df["fault_label"].value_counts())  #Classification: Balanced dataset
