import pandas as pd
import numpy as np

df = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Dataset Breakdown\\data_inputFile10.csv") 

print(df.head())
print(len(df))

dfs = np.array_split(df, 10)

for index, df in enumerate(dfs):
    df.to_csv(f'data_inputFile_Part2File10_{index+1}.csv',index = False)

