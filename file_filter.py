import os
import pandas as pd
import regex as re

path='../副本2020年度招考简章.xls'

dataframe=pd.ExcelFile(path)

pattern={'政治面貌':'中共党员','学历':'硕士','专业':'行政管理','基层工作最低年限':'无限制','备注':'六级|6级'}
pattern={'专业':'行政管理'}

def fun(row):
    row=row[1]
    if str(row['部门代码'])=='119104':
        print(row)
    find = True
    for key in pattern:
        if not re.search(re.compile(pattern[key]), str(row[key])):
            find = False
            break
        else:
            pass
    if find:
        print(row[key])
    return find

for i in dataframe.sheet_names:
    print('{}-------------------------------------'.format(i))
    sheet=pd.read_excel(path, sheet_name=i)
    indexs=list(map(fun,sheet.iterrows()))
    file_name='result_{}.xls'.format(i)
    res=sheet[indexs]
    res.to_excel(file_name,index=False,encoding='gbk')






