d = {1:'sreeni', 2:'Rahul', 3: 'Nikhil'}

print("d is",d)
print("keys", d.keys())
print("values", d.values())
print("items", d.items())

for i in d.keys():
    print("key is", i)

for j in d.values():
    print("value is", j)

for k in d:
    print(k)

for x,y in d.items():
    print(f"k is {x} and value is {y}")

r = range(1,3)
l = [1,2]
t = (1,2)
print("size of r", r.__sizeof__())
print("size of l",l.__sizeof__())
print("size of t",t.__sizeof__())

