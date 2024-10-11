

name = input("enter name:")

#syntax only with if

#if condition:
    #stmts

# we can any number of if blocks in single module file
# if name  == 'sreeni':
#     print(f"Hello {name}, Good morning")
#
# print("This is outside of first if stmt")
#
# age = 19
# if age == 18:
#     print(f"Age is {age}")
#
# print("This is outside of second if stmt")

#syntax if-elif

# if condition1:
    #stmts
# elif condition2:
    #stmts(any working python code)

# if name.lower()  == 'sreeni': #'sreeni' =='sreeni'
#     print(f"Hello {name.capitalize()}, Good morning")
# elif name.lower() == 'sudheer':
#     print(f"Hello {name.capitalize()}, Good morning")

#syntax for if-elif-else

# if condition1:
#     stmts
# elif condition2:
#     stmts
# elif condition3:
#     stmts
# elif condition4:
#     stmts
# else:
#     stmts

if name == 'sreeni':
    print(f"Hello {name} ,Good morning")
elif name == 'sudheer':
    print(f"Hello {name}, Good morning")
elif name == 'hari':
    print(f"Hello {name}, Good morning")
elif name == 'shiva':
    print(f"Hello {name}, Good morning")
else:
    print("Hello Guest, Good morning")

#syntax for if-else

# if condition:
#     stmts
# else:
#     stmts

if name == 'sreeni':
    print(f"Hello {name} ,Good morning")
else:
    print("Hello Guest, Good morning")



# take a number using input method and
# print if num>0 as positive number,
# elif number = 0 print as zero
# else negative number

# take age using input method and
# print if age>=18 as eligible for vote
# else print not eligible and you will be eligible for vote in x years ( x should 18-entered age)

# take marks using input method
# print if marks>=70 as Grade A
# print if marks between 60 and 70 Grade B
# print if marks between 50 and 60 Grdae C
# print if marks between 40 and 50 Grdae D
# else failed