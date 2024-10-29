import numpy as np

import pandas as pd


# from operators_control_flows.comparison_operators import target_count

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




#
#
# def read_file(file_path):
#         if file_path.endswith('.parquet'):
#                 df = pd.read_parquet(file_path)
#         elif file_path.endswith('.csv'):
#                 df = pd.read_csv(file_path)
#         else:
#                 print("Invalid format")
#         return df
#
# source = read_file("/Users/admin/PycharmProjects/SEPT_AUTOMATION/input_files/userdata1_t.parquet")
# target = read_file("/Users/admin/PycharmProjects/SEPT_AUTOMATION/input_files/Contact_info.csv")
#
# print("source and target ")
# print(source.head(1))
# print(target.head(1))
#
# test_cases = pd.read_excel("/Users/admin/PycharmProjects/SEPT_AUTOMATION/test_cases.xlsx")
#
# def count_check(source, target):
#         source_count = source.shape[0]
#         target_count = target.shape[0]
#         if source_count == target_count:
#                 print("counnt is matching")
#         else:
#                 print("count is not matching")
#
# def data_compare(source, target):
#         pass
#
# for row, val in test_cases.iterrows():
#         print(val['source'], val['target'], val['key_column'])
#         source = read_file(val['source'])
#         target = read_file(val['target'])
#         key_column = val['key_column']
#         count_check(source, target)
#
#
#
#
#
#
#

