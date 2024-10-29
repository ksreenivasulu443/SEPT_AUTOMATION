import pandas as pd
from ydata_profiling import ProfileReport

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

df = pd.read_parquet('/Users/admin/PycharmProjects/SEPT_AUTOMATION/input_files/userdata1.parquet')

#df2 = pd.read_csv('/Users/admin/PycharmProjects/SEPT_AUTOMATION/input_files/Contact_info.csv', sep=',')

# print("*"*50)
# print("top n records")
# print(df.head(30))
# print("*"*50)
# print("bottom n records")
# print(df.tail())
# print("*"*50)
# print("print df")
# print(df)
# print("*"*50)
# print("sample n records")
# print(df.sample(10))
# print("*"*50)
# print("sample with fraction ")
# print(df.sample(frac=0.7))

print("*"*50)
print("df shape")
print(df.shape)
print("number of rows", df.shape[0] )
print("number of columns", df.shape[1])

print("*"*50)
print("df describe")
print(df.dtypes)
print(df.describe())

print(df)

print("*"*50)
print("df df.query")
print(df.query(" first_name == 'Amanda' | salary>= 118824 "))

print("*"*50)
print("df nlargest")
print(df.nlargest(5,'salary'))
print(df.nsmallest(5,'salary'))


print("*"*50)
print("df single column")
print(df[['ip_address','id','first_name']])

print("*"*50)
print("df iloc ")
print(df.iloc[4:6, 1:])

print(df.loc[4:6, 'cc':'salary'])




Result = ProfileReport(df)
Result.to_file("profile_report.html")




