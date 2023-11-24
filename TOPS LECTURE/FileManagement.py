file=open("tops1.txt","w")
file.write("This is file input/output demo using python.")
file.close()
print("File Written Successfully")

file=open("tops1.txt","r")
print(file.read())
file.close()

file=open("tops1.txt","a")
file.write("\nThis file is now appended.")
file.close()

file=open("tops1.txt","r")
print(file.read())
file.close()

file=open("tops2.txt","w+")
file.write("This is w+ mode using python.")
print(file.tell())
file.seek(10)
print(file.read())
file.close()
