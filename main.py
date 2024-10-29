from ydata_profiling import ProfileReport

import pandas as pd

import pandasql as ps


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

df = pd.read_csv('/Users/admin/PycharmProjects/SEPT_AUTOMATION/files/Contact_info.csv')

# print("contact info data df")
# print(df)
# Result = ProfileReport(df)
# Result.to_file("profile_report.html")


# df = pd.DataFrame(
# {"a" : [4, 5, 6],
# "b" : [7, 8, 9],
# "c" : [10, 11, 12]},
# index = [1, 2, 3])
#
# print(df)
#
#
# df = pd.DataFrame(
# [[4, 7, 10],
# [5, 8, 11],
# [6, 9, 12]],
# columns=['a', 'b', 'c'])
#
# print(df)
#
# print(df.head(1))
# print(df.tail(2))
#
# print(df.columns)
# print(df.dtypes)
# print("count",df['a'].count())
#
# df = pd.read_csv('/Users/admin/PycharmProjects/SEPT_AUTOMATION/files/Contact_info.csv')
#
# print(df.head(10))
#
# df1 = pd.DataFrame({
#     'ID': [1, 2, 3, 4],
#     'Name': ['Alice', 'Bob', 'Charlie', 'David']
# })
#
# df2 = pd.DataFrame({
#     'ID': [3, 4, 5, 6],
#     'Age': [25, 30, 35, 40]
# })
#
# print(df1)
# print(df2)
#
# # Merging DataFrames on the 'ID' column
# merged_df = pd.merge(df1, df2, on='ID', how='inner')  # Inner join
# print("Inner Merge Result:")
# print(merged_df)
#
# # Left join
# merged_df_left = pd.merge(df1, df2, on='ID', how='left')
# print("\nLeft Merge Result:")
# print(merged_df_left)
#
# # Right join
# merged_df_right = pd.merge(df1, df2, on='ID', how='right')
# print("\nRight Merge Result:")
# print(merged_df_right)
#
# # Outer join
# merged_df_outer = pd.merge(df1, df2, on='ID', how='outer')
# print("\nOuter Merge Result:")
# print(merged_df_outer)
#
#
# print("concat axis=0")
# concat_df_cols_0 = pd.concat([df1, df2], axis=0)
# print(concat_df_cols_0)
# print("concat axis=1")
# concat_df_cols_1 = pd.concat([df1, df2], axis=1)
# print(concat_df_cols_1)
#
# print(ps.sqldf("""select * from df1
#                 union
#                 select * from df2"""))


df = pd.read_csv("/Users/admin/PycharmProjects/SEPT_AUTOMATION/files/Contact_info.csv")

print(df.head())

print(df.tail(5))

# print(help(pd.read_csv))

df2 = pd.read_excel("/Users/admin/PycharmProjects/SEPT_AUTOMATION/files/Master_Test_Template.xlsx")

print(df2.head())

df3 = pd.read_parquet("/Users/admin/PycharmProjects/SEPT_AUTOMATION/files/userdata1.parquet")
print(df3.head(4))

# print("describe")
#
# print(df3.describe())
#
# print(df.sample(10))
#
# print(df.sample(frac=0.2))
#
# print(df.query("Surname == 'Patel' | Given_name == 'test' "))
#
# print(df3.nlargest(5,'salary'))
# print(df3.nsmallest(5,'salary'))
#
# print(df.filter(['gender']))

print(df.iloc[1:7, 2:4])

print(df.loc[1:7, 'Given_name':'City'])

df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'ID': [3, 4, 5, 6],
    'Age': [25, 30, 35, 40]
})

print(pd.concat([df1,df2]))

print(pd.concat([df1,df2], axis=1))

merged_df = pd.merge(df1, df2, how='outer', on='ID')

print(merged_df)

import pandasql as ps

print(ps.sqldf("select count(1) from df1 where name='Alice'"))






