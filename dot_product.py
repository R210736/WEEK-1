l=[]
m=[]
s=0
n=int(input("enter the length of vector:"))
for i in range(n):
	a=int(input("enter any number:"))
	b=int(input("enter any numbera:"))
	l.append(a)
	m.append(b)
print("list l=",l)
print("list m=",m)
for i in range(n):
	s=s+l[i]*m[i]
print(s)