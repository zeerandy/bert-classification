#查看bert测试成果

import pandas as pd
import numpy as np
import json


url='/Users/vin/Desktop/test_results.tsv'
test='/Users/vin/Desktop/test.tsv'

df = pd.read_csv(url, encoding='utf-8',sep='\t')
df2 = pd.read_csv(test, encoding='utf-8',sep='\t', dtype={
    "content": str, "number": str,"label": int})
ls=pd.DataFrame({"content": [], "test": [], "label": []})

n = df.shape[0] #共有n条数据

#分别求行最大值及最大值所在索引
print(np.argmax(np.array(df),axis=1))
#exit()
#行最大值
df['max_value']=df.max(axis=1)
#行最大值索引0~6
df['max_index']=np.argmax(np.array(df),axis=1)

t1 = df['max_index']
t2 = df2['label']

for i in range(0,n):
    t1[i]=int(t1[i])+1
    if t1[i]!=t2[i]:
        s = pd.Series({'content':df2['content'][i], 'test':t1[i], 'label':t2[i]})
        ls=ls.append(s,ignore_index=True)

ls.to_csv('/Users/vin/Desktop/testcompare.tsv',sep='\t',index=None)

print (len(ls),n) 
