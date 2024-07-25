a = int(input("Enter the value of a :"))
print(type(a))
for i in range(a):
    if i==3:
        continue
    print(i,end='')