import numpy as np
import pandas as pd
import re


    
# 导入原数据 将csv文件读入并转化为数据框形式
df1 = pd.read_csv('./data/test.tsv', sep='\t',encoding='UTF-8', dtype={
    "title": str,"content": str, "lab": str, "label": str})
df2 = pd.read_csv('./output/predict.csv', encoding='UTF-8', dtype={
    "content": str, "number": str, "label": str})

n = df1.shape[0] #共有n条数据
print(n)

t1 = df1['label']
t2 = df2['label']
ls = pd.DataFrame({"title": [],"content": [], "number": [], "label": []})

for i in range(0,n):
    if t1[i]!=t2[i]:
        s = pd.Series({'content':df1['content'][i], 'number':df1['number'][i], 'label':t2[i]})
        ls=ls.append(s,ignore_index=True)
        

print (len(ls)) 

ls.to_csv('/Users/vin/Desktop/compare1.csv')

# 识别数字后的数据



