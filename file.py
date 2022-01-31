import numpy as np
import pandas as pd
from datetime import date

today=date.today()
df=pd.read_csv('Zerodha.csv')
df=pd.DataFrame(df)
df=df.iloc[3:,1]
df.dropna(inplace=True)


gapup=pd.read_csv("gapup.csv")
gapdown=pd.read_csv("gapdown.csv")
gapup=pd.DataFrame(gapup)
gapdown=pd.DataFrame(gapdown)

todayDate=today.strftime("%d-%m-%Y")
gapup=gapup.loc[gapup['date']==todayDate]
gapdown=gapdown.loc[gapdown['date']==todayDate]

# print(gapup)
# print(df)
upList=list(np.intersect1d(gapup["symbol"], df))
downList=list(np.intersect1d(gapdown["symbol"], df))

print(upList)
print(downList)

file1 = open("finalShortList.txt", "w")  
file1.write("Gap up Stocks:"+str(upList)+"\n\n")
file1.write("Gap down Stocks:"+str(downList)+"\n")
file1.close()