import pandas as pd

df1 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file1.csv")
df2 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file2.csv")  
df3 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file3.csv")
df4 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file4.csv")
df5 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file5.csv")
df6 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file6.csv")
df7 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file7.csv")
df8 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file8.csv")
df9 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file9.csv")
df10 = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\Output\\file10.csv")

dfOut = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10])
print(len(dfOut))
dfOut.to_csv('D:\\Study\\UG Thesis\\Datasets\\\Output\\file1-10.csv', index=False) 


