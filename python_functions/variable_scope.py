from math import pi
a = 10 # Global variable # scope is entire module file
b = 20 # Glocal variable
print( "Global space", globals())


def outer_fun():
    #a = 11 # local variable
    c = 20 # Global variable
    #b = 23

    print("a value from outer_fun fun", a)
    print("b value from outer_fun fun", b)
    print("c value from outer_fun fun", c)

    def inner_fun():
        #a=12
        #pi=3.14
        # global d
        d=200
        print("a value from inner fun", a)
        print("b value from inner fun", b)
        print("b value from inner fun", pi)
    inner_fun()
    #print("d value ", d)



outer_fun()
#
# print("a value from inner fun", a)
# print("b value from inner fun", b)
# print("c value from inner fun", c)

print( "Global space", globals())



