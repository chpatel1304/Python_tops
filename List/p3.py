import random
l=[]
lucky=[]
for i in range (1,101):
    l.append(i)
#print(l)

for i in range (1,11):
    a=random.choice(l)
    lucky.append(a)
    l.remove(a)

print(lucky)
print("---------------------------------------------")
print(l)
