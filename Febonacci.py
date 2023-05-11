n=int(input("Enter Number:"))
n1,n2=0,1

for i in range(2,n+1):
    print(n1)
    n=n1+n2
    n1=n2
    n2=n+n
    
