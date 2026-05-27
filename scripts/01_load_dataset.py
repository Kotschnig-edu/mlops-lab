import pandas as pd
from globals import ORIGIN_DATASET as DATASET

data = pd.read_csv(DATASET)

print(data.head())
print(data.shape)
