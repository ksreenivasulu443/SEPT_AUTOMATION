


def f(arg1, arg2, arg3=4, arg4=8):
    print(arg1, arg2, arg3, arg4)

#f(3,2)# 3,2 positional arguments
#f(10,20,30,40) # 10,20,30,40 positional keywords
#f(25,50,arg4=100)# 25,50 are pos args, arg4 = keyword arg(originally default arg)
#f(arg4=2,arg1=3,arg2=4) # arg4,1,2 keyword arguments
#f() f() missing 2 required positional arguments: 'arg1' and 'arg2'
#f(arg3=10,arg4=20,30,40) #positional argument follows keyword argument
#f(4,5,arg2=6) #f() got multiple values for argument 'arg2'
#f(4,5,arg3=5,arg5=6) #f() got an unexpected keyword argument 'arg5'
#f(4,5,5,arg3=2) #f() got multiple values for argument 'arg3'


def calc(*a):
    print(sum(a))


def calc2(**a):
    print(a)

calc2(a=10,b=20)

add = lambda a,b: a+b

print(add(5,10))