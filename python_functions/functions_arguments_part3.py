# def calc(a,b):
#     return a+b
#
#
#
# def calc(a,b,c):
#     return a+b+c
#
#
# def calc(a,b,c,d):
#     return a+b+c+d
#
# #print(calc(10,20)) # 30 or error
#  # error
# #print(calc(10,20,30))
# print(calc(10,20,30,50)) #


def calc(*args): # *args variable length arguments(inplace args we can use any valid identifier)
    print("args", args)
    print("args type", type(args))
    sum=0
    for i in args:
        sum = sum+i
    return sum

    return sum(args)

print("sum of args", calc(10,20,40,4,5,6,6,7,7,8,8,9,9,9,9,11))

calc(1, 2, 40, 60,901,100,200)

def calc2(**etlargs): # kwargs keyword variable length arguments, (inplace kwargsargs we can use any valid identifier)
    print("kwargs", etlargs, type(etlargs))
    sum=0
    for value in etlargs.values():
        sum = sum+value
    print("sum of kwargs", sum)

calc2(a=10,b=20)

calc2(k=20, l=40, m=5)
#
calc2(k=20, l=40, m=5, n=1, p=2)

calc2(k=20, l=40, m=5, n=1, p=2,t=60)


def calc(a):  # *args variable length arguments(inplace args we can use any valid identifier)
    return a+10
    return a+5
    return a+1

print(calc(3))
