#sequence types/collection types : str, list, tuple, dict, range #df, array, series



# 1 is odd
# 2  is even
# ..
# 5 is odd

# number = int(input("Enter number:"))
# if number % 2 ==0:
#     print(f"number {number} is even")
# else:
#     print(f"number {number} is odd")

ls = [11, 17, 19, 16, 27, 31, 44, 99, 104]

#syntax

# for item in collect_type/sequence:
#     stmts

for item in ls:
    #print("item value is", item)
    if item % 2 == 0:
        print(f"item value {item} is even number")
    else:
        print(f"item value {item} is odd number")

ages = (18,19,13,21,101,2)

for i in ages:
    if i>=18:
        print(f"Age is {i} eligible for vote")
    else:
        print(f"Age is {i} not eligible for vote")


string = 'ETL Automation'

for j in string:
    #print("Character is", j)
    if j.lower() in ('a','e','i','o','u'):
        print(f"{j} is vowel")
    else:
        print(f"{j} is not vowel")


