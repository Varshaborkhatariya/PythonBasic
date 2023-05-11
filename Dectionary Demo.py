d={123:"Varsha",345:"Haresh",780:"Reena",689:"Viraj"}

print(d)
print(d[780])
print(d.get(345))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(780))
print(d)
print(d.popitem())
print(d)
d1={1:"Priya",2:"Myuri"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
