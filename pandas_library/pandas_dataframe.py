import numpy as np

import pandas as pd
# ls = [1,'2','3',4,True,10.5]
# for i in ls:
#     print(f"value is {i}, {type(i)}")
# array_1d = np.array([1.0, 2, 3, 4,'string'])
# #str>float>int>bool
# for i in array_1d:
#     print(f"value is {i}, {type(i)}")
#
# array_2d = np.array([[1, 2, 3], [4, 5, 6]])
# print(array_2d)


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)



data= {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30,22],
        'City': ['New York', 'Los Angeles','KA']}

print("type of data", type(data))

df = pd.DataFrame(data=data)

#print(help(pd.DataFrame))

print("type of df", type(df))
print("list of methods on df", dir(df))
print("df", df)

#print(help(pd.read_csv))

df2 = pd.read_csv('/Users/admin/PycharmProjects/SEPT_AUTOMATION/input_files/Contact_info.csv', sep=',')

print(df2)

df3 = pd.read_excel('/Users/admin/PycharmProjects/SEPT_AUTOMATION/input_files/Master_Test_Template.xlsx')

print(df3)

source= pd.read_parquet('/Users/admin/PycharmProjects/SEPT_AUTOMATION/input_files/userdata1.parquet')

print(source)


import pandasql as ps
print(ps.sqldf("select count(*) from df3 where source_type='csv' and validation_Type like '%count%' "))





