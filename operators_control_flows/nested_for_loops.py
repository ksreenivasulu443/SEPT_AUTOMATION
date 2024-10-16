# for i in range(4): #0 to 3
#     for j in range(5,8): # 5-7
#         for k in range(10,13):#10-12
#             print(f"i value is {i} and j value is {j}  and k value is {k}")

# 2*1=2
# 2*2=4
#
#
# 2*10=20

# for i in range(1,21):
#     for j in range(1,11):
#         print(f"{i}*{j}=",i*j)


d = {1:'sreeni', 2:'Rahul', 3: 'Nikhil'}

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key,value in d.items():
    print(key,value)

r = range(1,6)
l =[1,2,3,4,5]
t = (1,2,3,4,5)
print(r.__sizeof__())
print(l.__sizeof__())
print(t.__sizeof__())


for i in range(1,10):
    if i == 5:
        continue
    print(i)

#Sum of All Elements in a List
#Find the Largest Number in a List
#Count the Number of Vowels in a String
#Print the Fibonacci Series up to n Terms







#
# num = 10
#
# while num>=0:
#     print(num)
#     num = num-1
#
# number = 0
#
# while number<=10:
#     print(number)
#     number = number+1


