print("Swapping Two Numbers Without Temp varibale")
a=int(input("Enter A :"))
b=int(input("Enter B :"))
print("Orignal A :",a)
print("Orignal B :",b)
a=a+b
b=a-b
a=a-b
print("Swapped A :",a)
print("Swapped B :",b)
print("Swapping Two Numbers With Temp varibale")
c=int(input("Enter C :"))
d=int(input("Enter D :"))
print("Orignal C :",c)
print("Orignal D :",d)
temp=d
d=c
c=temp
print("Swapped C :",c)
print("Swapped D :",d)
