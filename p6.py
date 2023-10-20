sname=input("Enter Student Name : ")
sro=int(input("Enter Student's Roll Number "))
s1=int(input("Enter Subject 1 Marks : "))
s2=int(input("Enter Subject 2 Marks : "))
s3=int(input("Enter Subject 3 Marks : "))

total=s1+s2+s3
per=total/3

print("Student Details !")
print("Name :",sname)
print("Roll Number :",sro)
print("Total : ",total)
print("Percentage :",per)

if per>=70:
    print("Distinction Class")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Third Class")
else:
    print("Fail")
            
