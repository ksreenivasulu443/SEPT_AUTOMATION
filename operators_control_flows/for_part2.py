# list, tuple, string , dict, range

# range(stop): Generates numbers from 0 to stop-1.
# range(start, stop): Generates numbers from start to stop-1.
# range(start, stop, step): Generates numbers from start to stop-1 with a step of step.


a = range(10)

print("value of a", a, type(a), id(a))

for i in range(10):
    print("i value is",i)

for j in range(1,10):
    print("J value is",j)

for k in range(2,20,2):
    print("K value is", k)

for l in range(0,501,2):
    print(l)

# calculate sum n numbers ( 10 )
# calculate sum square of numbers

number = int(input("enter number: "))
even_sum = 0
odd_sum =0
for i in range(number):
    if i % 2 ==0:
        even_sum +=i # sum = sum+i
    else:
        odd_sum +=i

print(f"Even numbers sum", even_sum)
print(f"odd numbers sum", odd_sum)

list_cols =['Col1 ',' col2 ' ,'col3 ']

list_upper = []

for col in list_cols:
    list_upper.append(col.upper().strip())

print("upper converted cols list", list_upper)


