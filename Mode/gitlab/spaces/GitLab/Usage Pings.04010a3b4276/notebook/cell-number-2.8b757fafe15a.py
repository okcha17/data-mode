import pandas as pd
import numpy as np

df = datasets[0]
df=df.astype({"MAJOR_VERSION": str})
# print(df["MAJOR_VERSION"].dtypes)

versions = ["7.11","7.12","7.13","7.14","8.0","8.1","8.2","8.3","8.4","8.5","8.6","8.7","8.8","8.9","8.10","8.11","8.12","8.13","8.14","8.15","8.16","8.17","9.0","9.1","9.2","9.3","9.4","9.5","10.0","10.1","10.2","10.3","10.4","10.5","10.6","10.7","10.8","11.0","11.1","11.2","11.3","11.4","11.5","11.6","11.7","11.8"]

# df=df.astype({"MAJOR_VERSION": str})
df=pd.pivot_table(df,index='MONTH',columns='MAJOR_VERSION',values="UUID", aggfunc=np.sum, fill_value=0)

# print(df["UUID"].dtypes)
# df.head(5)
df=df.reindex(columns=versions)
# df.head(5)
df['Total']=df.sum(axis=1)

# print(df.head(5))

df=df.reset_index()

current_release = []
trailing_3 = []
trailing_6 = []
for count,row in enumerate(df.iterrows()):

  curr_month_count = df.iloc[count, count+1]
  three_month_trail = df.iloc[count, max(count-1,1):count+2].sum()
  six_month_trail = df.iloc[count, max(count-4,1):count+2].sum()
  customer_total = df.iloc[count].loc["Total"]
  
  current_release.append(curr_month_count / customer_total)
  trailing_3.append(three_month_trail/customer_total)
  trailing_6.append(six_month_trail/customer_total)

df = pd.concat([df, pd.DataFrame({"Current %":current_release})], axis=1)
df = pd.concat([df, pd.DataFrame({"Trailing 3 Months":trailing_3})], axis=1)
df = pd.concat([df, pd.DataFrame({"Trailing 6 Months":trailing_6})], axis=1)

df.style
# df.plot()