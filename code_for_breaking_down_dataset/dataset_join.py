import pandas as pd
import glob
import os

os.chdir('D:\\Study\\UG Thesis\\Datasets\\Output\\output_data\\file 9')
print(os.listdir())

files = [file for file in os.listdir()]
df = pd.concat(map(pd.read_csv(files,low_memory=False), files), ignore_index=True)
print(len(df))