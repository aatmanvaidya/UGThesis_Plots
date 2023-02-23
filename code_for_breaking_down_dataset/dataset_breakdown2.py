import pandas as pd
import numpy as np

df = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Dataset Breakdown2\\File 1\\data_inputFile_Part2File1_2.csv") 

print(df.head())
print(len(df))

dfs = np.array_split(df, 5)

for index, df in enumerate(dfs):
    df.to_csv(f'data_inputFile_Part3File1_Segment2_{index+1}.csv',index = False)

