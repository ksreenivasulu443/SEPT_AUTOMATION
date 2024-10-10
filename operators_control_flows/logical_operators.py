# a=10.4
# b=20
# c=0
# d=-30
#
# print("a value is",a, bool(a))
# print("b value is",b, bool(b))
# print("c value is",c, bool(c))
# print("d value is",d, bool(d))
# print(" bool(None)", bool(None))
# print(" bool('')", bool(' '))
#
# # bool(value) # if value = 0 then o/p false else o/p True
#
# # logical operators and
#
# print(" a and b", a and b) # if both are true o/p will be right side value
#
# # a and b
# #
# # bool(a) and bool(b)
# # True and True = right side (b)
#
# print(" b and a", b and a)
# print(" a and c", a and c)
# print(" c and d", c and d)
# print(" None and '' ", None and ' ')
#
# a = 40
# b = 20
# c = 30
#
# if a>b and b>c : # 40>20 (True) and 40>30 (True)
#     print("a is greater")


# a = 5
# b = 2
# print("bool(a)", bool(a)) # True
# print("bool(b)", bool(b)) # True
# print("a and b", a and b) # True and True
# print("a or b", a or b)
# print(" not a", not a) # not bool(a)
# #
# c = 0
# d = 2
# print("bool(c)", bool(c)) # False
# print("bool(d)", bool(d)) # True
# print("c and d", c and d) #False and True
# print("c or d", c or d) #False or True
# print(" not c", not c)

age = int(input("enter person age:"))
citizen = input("enter person citizen(lower case e.g. indian):")

if age>=18 and citizen == 'indian': # 17>=18 (False) or indian==indian(True) ==> True
    print("eligible for vote")
else:
    print("not eligible for vote")








#
# a = 9
# b = 3
#
# # Using 'and' condition
# if a % 3 == 0 and b % 3 == 0:
#     print("Both 'a' and 'b' are divisible by 3.")
# else:
#     print("At least one of them is not divisible by 3.")
