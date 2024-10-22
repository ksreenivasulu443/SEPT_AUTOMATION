
a = 100
b = 20
e= 31
def out_fun():
    a = 24
    c = 21
    print("e value ", e)
    print("global variables inside of function", globals())
    print("local variables inside of function", locals())
    def inner():
        k=20
        c=22
        print("global variables inside of inner function", globals())
        print("local variables inside of inner function", locals())
    inner()





out_fun()

print("e value",e)