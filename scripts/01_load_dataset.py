import pandas  as pd

DATASET = "./data/raw/data.csv"

data = pd.read_csv(DATASET)

print(data.head())
print(data.shape)
