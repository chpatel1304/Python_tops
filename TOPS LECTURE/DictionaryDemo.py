d={109:"Ekal",98:"Chirag",877:"Hamza",654:"Aksh"}

print(d)
print(d.get(877))
print(d[98])
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(877))
print(d)
print(d.popitem())
print(d)
d1={111:"Aksh",222:"Hamza",333:"Rahul",444:"Helly"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
