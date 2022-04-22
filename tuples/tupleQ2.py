def Remove(f):
    p=l-1
    for i in range(p):
        if(f[i]==('','')):
           f.pop(i)
           p=p-1
    print("After deletion",f)
f=[]
l=int(input("Enter the length of tuple::"))
for i in range(l):
    s=[]
    x=input("Enter the element 1::")
    y=input("Enter the element 2::")
    s.append(y)
    s.append(x)
    z=tuple(s)
    f.append(z)
print("before deletion",f)
Remove(f)
