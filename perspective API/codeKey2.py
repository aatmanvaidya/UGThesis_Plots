from perspective import PerspectiveAPI
import time
import pandas as pd
import sys

p = PerspectiveAPI("AIzaSyCVNhnq1FodfLNIlPO-p08zB06f1pJ_Gjo")
df = pd.read_csv("D:\\Study\\UG Thesis\\Code Trys\\out1.csv") 
# print(df.head(10)) 
print(time.ctime())

for index, row in df.iterrows():
    try:
        text=row["tweet_text"]
        result = p.score(text, tests=["TOXICITY", "SEVERE_TOXICITY"])
        df.loc[index, "Toxicity"]=result["TOXICITY"]
        df.loc[index, "Severe Toxicity"]=result["SEVERE_TOXICITY"]
        time.sleep(1)
    except:
        pass

print("\n" + time.ctime())

df.to_csv("key2_out.csv", index=False)