# ls = [11, 18, 19, 16, 27]
#
# for item in ls:
#     if item % 2 == 0:
#         print(f"item value {item} is even number")
#     else:
#         print(f"item value {item} is odd number")
#
# print("this is out side of for loop")

number = int(input("enter number:"))
print("type of number", type(number))

if number == 0:
    print("entered number is Zero")
elif number == 1:
    print("entered number is one")
elif number == 2:
    print("entered number is two")
elif number == 3:
    print("entered number is three")
elif number == 4:
    print("entered number is four")
elif number == 5:
    print("entered number is five")
elif number == 6:
    print("entered number is six")
elif number == 7:
    print("entered number is seven")
elif number == 8:
    print("entered number is eight")
elif number == 9:
    print("entered number is nine")
elif number == 10:
    print("entered number is ten")
else:
    print("entered number is not between 0 and 10, please retry")


number = 0

while number<=10:
    print(number)
    number = number-1
