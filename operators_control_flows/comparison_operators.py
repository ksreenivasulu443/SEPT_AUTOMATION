
a = 10
b = 10.4

print("type of a", type(a))
print("type of b", type(b))

print("a==b", a==b)
print("a!=b", a!=b)
print("a>=b", a>=b)
print("a>b", a>b)
print("a<=b", a<=b)
print("a<b", a<b)

#syntax
# if condition:
#     stmt
# else:
#     stmts

age = int(input("Enter age value: "))  # input function automatically converts value to string type

print("age value", age)
print("type of age", type(age))

if age>=18: # 17.0>=18 --.False
    print("person is eligible for vote")
    print("this is dummy line")

else:
    print("person is not eligible for vote")

source_count = int(input("Enter source count: "))

target_count = int(input("Enter target count: "))

if source_count ==  target_count: # 10 == 10
    print("count is matching")
    print("TC o/p is pass")


else:
    print("count is not matching")
    print("TC o/p is fail")




