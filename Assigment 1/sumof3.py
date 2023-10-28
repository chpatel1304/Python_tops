x=int(input("Enter X"))
y=int(input("Enter Y"))
z=int(input("Enter Z"))
sum=0
if x == y or y == z or x==z:
    sum = 0
else:
    sum = x + y + z
print("SUM  IS ",sum)
