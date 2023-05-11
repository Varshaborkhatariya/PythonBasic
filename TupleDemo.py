t=(1,2.2,3.4,"varsha",11,[10,20,30],"haresh",4,5,6)
print(t)
print(t.count(t))
print(t.index(11))

for i in t:
    print(i)
print(list(t))
print(101 in t)
print(t[5])
t[5].append(40)
print(t[5])
