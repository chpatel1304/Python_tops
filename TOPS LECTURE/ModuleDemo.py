import UDF

while True:

    print("*********************************************************")
    print("1. Max Of Two")
    print("2. Max Of Three")
    print("3. Odd Even")
    print("4. Pattern")
    print("5. Prime")
    print("6. Exit")
    print("*********************************************************")
    choice=int(input("Enter Your Choice : "))

    if choice==1:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        UDF.maxoftwo(a,b)
        print("*********************************************************")
    
    elif choice==2:
        a=int(input("Enter Value : "))
        b=int(input("Enter Value : "))
        c=int(input("Enter Value : "))
        UDF.maxOfthree(a,b,c)
        print("*********************************************************")

    elif choice==3:
        a=int(input("Enter Value : "))
        UDF.oddeven(a)
        print("*********************************************************")

    elif choice==4:
        a=int(input("Enter Number Of Rows : "))
        UDF.pattern(a)
        print("*********************************************************")

    elif choice==5:
        a=int(input("Enter Value : "))
        UDF.prime(a)
        print("*********************************************************")
    elif choice==6:
        print("Thank You For Using Our Services")
        print("*********************************************************")
        break
    else:
        print("Invalid Choice. Please try Again.")
        print("*********************************************************")
        
        
        
