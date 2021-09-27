import pandas as pd
import math
from scipy.stats import norm
import Constant
import BlackScholes 
import numpy as np
import matplotlib.pyplot as plt  

cols=range(0,7)
df = pd.read_excel (r'Test_candidates.xlsx', usecols=cols)

for index, row in df.iterrows():
    a=BlackScholes.Call (float(row["GOOGLE PRICE"]), Constant.KGoogleCall,Constant.r,Constant.t, float(row["GOOGLE VOL"]))
    b=BlackScholes.Put (float(row["GOOGLE PRICE"]), Constant.KGooglePut,Constant.r,Constant.t, float(row["GOOGLE VOL"]))
    c=BlackScholes.Call (float(row["AMAZON PRICE"]), Constant.KAmazon,Constant.r,Constant.t, float(row["AMAZON VOL"]))
    d=BlackScholes.Call (float(row["AMAZON PRICE"]), Constant.KAmazon2,Constant.r,Constant.t, float(row["AMAZON VOL"]))
    e=BlackScholes.Call (float(row["APPLE PRICE"]), Constant.KAppleCall,Constant.r,Constant.t, float(row["APPLE VOL"]))
    f=BlackScholes.Call (float(row["APPLE PRICE"]), Constant.KAppleCallS,Constant.r,Constant.t, float(row["APPLE VOL"]))
    g=BlackScholes.Put (float(row["APPLE PRICE"]), Constant.KApplePut,Constant.r,Constant.t, float(row["APPLE VOL"]))
    df.loc [index, 'Portfolio Value'] = a*Constant.nGoogleCall+b*Constant.nGooglePut+Constant.nGoogle*row["GOOGLE PRICE"]+c*Constant.nAmazonCall+d*Constant.nAmazonCall+Constant.nAmazon*row["AMAZON PRICE"]+Constant.nAppleCall*e+Constant.nAppleCallS*f+g*Constant.nApplePut
    
pctdiffs= df["Portfolio Value"].pct_change().dropna()
pctdiffs.hist()


mean=pctdiffs.mean()
stdev=pctdiffs.std()
conf=0.99
cutoff1=norm.ppf(conf,mean,stdev)
df['VaR']=df['Portfolio Value']*cutoff1
pctdiffs=pctdiffs.sort_values ()
df['VaR Historical']=df['Portfolio Value']*pctdiffs.iloc[pctdiffs.size//100]




print ('1-os užduoties atsakymas')
row=df.loc[df['Date']=='2013.04.19']
print (row['Portfolio Value'])
print ('2-os užduoties atsakymas')
df.iloc[df['Portfolio Value'].rolling(window=2).apply(np.diff).idxmin()]
print (df.iloc[df['Portfolio Value'].rolling(window=2).apply(np.diff).idxmin(),:8])
print ('3-os užduoties atsakymas')
print (cutoff1)
print (df['VaR'])
print ('4-os užduoties atsakymas')
print (pctdiffs.iloc[pctdiffs.size//100])
print (df['VaR Historical'])
