def maxoftwo(a,b):
    if a>b:
        print(a," Is Max")
    else:
        print(b," Is Max")


def maxOfthree(a,b,c):
    if a>b:
        if a>c :
            print("A is Max")
        else:
            print("C is Max")
    elif b>c:
        print("B is Max")
    else:
        print("C is Max")

def oddeven(a):
    if a%2==0:
        print(a,"Is Even")
    else:
        print(a,"Is Odd")

def pattern(n):
    for i in range(1,n):
        print(" "*(9-i)," *"*i)
    for i in range(n-1,0,-1):
        print(" "*(9-i)," *"*i)


def prime(num):
    if num==1:
        print(num," is not prime or composite number")
    elif num%2!=0:
        for i in range (3,int(num/2)+1,2):
            if num%i==0:
                print(num," Not a Prime Number")
                break
        else:
            print(num," Is A Prime Number ")
    else:
        print(num," Not A Prime Number")

