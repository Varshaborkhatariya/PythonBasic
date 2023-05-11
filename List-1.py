import random

#print(random.randint(100,99))
#print(random.choice([1,2,"varsha","haresh",2,3,4,]))

l=[]
lucky=[]

for i in range(1,101):
    l.append(i)

print(l)

for i in range(10):
    num=random.choice(l)
    lucky.append(num)
    l.remove(num)

print(lucky)
    
    

