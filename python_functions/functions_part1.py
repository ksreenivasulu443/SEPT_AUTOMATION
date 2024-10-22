def greeting():
    print("Hello, Good morning")
    print("another code line")





def greeting():
    print(f"Hello Guest, Good morning")

greeting()


# greeting_with_name('ETL TESTING') # we are directly providing value without key, positional argument
#
# greeting_with_name(name = 'ETL TESTING')  # name is argument and ETL TESTING is value(name is key), Key word argument
#
def calc(a,b):
    add = a+b
    sub = a-b
    mul = a*b
    # print(" value of a ", a)
    # print(" value of b ", b)
    # print(f" sum of {a} and {b} is " , a+b)
    # print(f" sub of {a} and {b} is ", a - b)
    # print(f" mul of {a} and {b} is ", a * b)
    # print(f" div of {a} and {b} is ", a / b)

    return add, sub , mul , a/b, a**2+b**2  # return is function o/p give to function caller

print(calc(10,20))
#
function_out = calc(12,13)

print(function_out, type(function_out))

add_out = function_out[0]
sub_out = function_out[1]
mul_out = function_out[2]
div_out = function_out[3]

print("add_out", add_out)
print("sub_out", sub_out)
print("mul_out", mul_out)
print("div_out", div_out)
#
# add_out1, sub_out1,mul_out1,div_out1 = calc(12,13)
#
# print("add_out1", add_out1)
# print("sub_out1", sub_out1)
# print("mul_out1", mul_out1)
# print("div_out1", div_out1)

# def read_file(path):
#     df = pd.read_csv(path)
#     df.head()
#
# source = read_file('source path')
# target = read_file('target path')
# def validation(source, target):
#     if source.count() == target.count():
#         print("count is matching")
