import pandas as pd
import numpy as np

df = pd.read_csv("D:\\Study\\UG Thesis\\Code\\code_for_breaking_down_dataset\\temp.csv") 
print(df.shape)
dfs = np.array_split(df, 3)

for index, df in enumerate(dfs):
    df.to_csv(f'tweets_retweetsFile_Part{index+1}.csv',index = False)

# print(dfs) 