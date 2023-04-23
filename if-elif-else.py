rno=int(input("Enter Student Roll Number:"))
sname=(input("Enter  Student Name:"))
s1=int(input("Enter Marks of  Subject1:"))
s2=int(input("Enter Marks of  Subject2:"))
s3=int(input("Enter Marks Of  subject3:"))

total=s1+s2+s3
per=total/3

print("Studest Name:",sname)             
print("Roll No:",rno)
print("Total:",total)
print("Percentage:",per)

if per>=70:
    print("Disritinction")
elif per>=60:
    print("First Class")
elif per>=50:
    print("Second Class")
elif per>=40:
    print("Pass Class")
else:
    print("fail")



         
