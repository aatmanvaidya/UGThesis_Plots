import pandas as pd
import numpy as np

df = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\breakingDatasetForNewConversion\\tweets_retweetsFile.csv", engine='python') 
# print(df.shape)
dfs = np.array_split(df, 10)

for index, df in enumerate(dfs):
    df.to_csv(f'tweets_retweetsFile_Part{index+1}.csv',index = False)

# print(dfs) 