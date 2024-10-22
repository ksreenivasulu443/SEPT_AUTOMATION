def count_check(source_count, target_count):
    print("source count is", source_count)
    print("target count is", target_count)
    if source_count == target_count:
        print("count is matching")
    else:
        print("count is not matching and difference is", abs(source_count-target_count))

#10,20 positional arguments
# count_check(10,20) #
# count_check(20,18)
# count_check(18,18)

# # keyword arguments
# #here we are passsing values with keys source_count,target_count
# count_check(source_count=20, target_count=19)
# count_check(target_count=19,source_count=20)
#
# def count_check_default(source_count, target_count, key_col='COL'):
#     print("source count is", source_count)
#     print("target count is", target_count)
#     print("key col is", key_col)
#     if source_count == target_count:
#         print("count is matching")
#     else:
#         print("count is not matching and difference is", abs(source_count-target_count))
#
# count_check_default(source_count=10,target_count=20)
# count_check_default(10,target_count=20,key_col='NAME')

def count_check(source_count, target_count):
    print("source count is", source_count)
    print("target count is", target_count)
    if source_count == target_count:
        print("count is matching")
    else:
        print("count is not matching and difference is", abs(source_count-target_count))


# if we want to pass positional argument you can pass but it should be before your keyword arguments
#count_check(source_count=10,20) # incorrect here positional arguments coming after keyword argument
#count_check(10,target_count=20)

def calc(a,b,c):
    return a,b,c

# if we want to pass positional argument you can pass but it should be before your keyword arguments
# once keyword argument started then all other arguments should be keyword
# if you are providing a value to argument using position argument and make sure you are not providing value to same argument using keyword or default
# keep default argument at end of your all arguments
def calc2(a,b,c=0, d=0):
    print("a value",a)
    print("b value", b)
    print("c value", c)
    print("d value",d)


calc2(a=10,b=20)
calc2(a=10,b=20,d=50)
calc2(a=10,b=20,d=50,c=40)
calc2(10,20,50,d=40)

