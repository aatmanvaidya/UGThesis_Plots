import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import seaborn as sns

df = pd.read_csv("D:\\Study\\UG Thesis\\Datasets\\ReibeiroDataset\\tweetsConvereted2017_toxicPerspectiveScore.csv")
# Parse the dates in the NewDateFormat column and extract the week number
df["week"] = df["NewDateFormat"].apply(lambda x: datetime.strptime(x, "%Y-%m-%d %H:%M:%S").strftime("%U"))
# df['week'] = df[['week']].astype(int)
groupDf = df[['screen_name', 'Toxicity', 'Severe Toxicity', 'qt_flag', 'rt_flag', 'week']]
groupDf2 = groupDf[(groupDf['qt_flag'] == False) & (groupDf['rt_flag'] == False)]

unique_values = df['week'].unique()

def avgToxicity(weekIn):
    weekDf = groupDf2[groupDf2['week'] == weekIn]
    return weekDf['Toxicity'].mean()

for i in unique_values:
    print(avgToxicity(i))