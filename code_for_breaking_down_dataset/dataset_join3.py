import pandas as pd
import glob
import os

path = "D:\\Study\\UG Thesis\\Datasets\\Output\\output_data\\file 10" 
all_files = glob.glob(os.path.join(path , "data_inputFile_Part2File10*_out.csv"))
# print(all_files)

li = []

for filename in all_files:
    df = pd.read_csv(filename, low_memory=False, lineterminator='\n')
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)
print(len(frame))
frame.to_csv('D:\\Study\\UG Thesis\\Datasets\\Output\\file10.csv', index=False)