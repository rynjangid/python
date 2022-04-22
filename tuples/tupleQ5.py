def check_in_tuples(colors, c):
    result = any(c in tu for tu in colors)
    if(result==True):
        print("The element is present:")
    else:
        print("The element is not present:")
f=[]
l=int(input("Enter the length of list::"))
for i in range(l):
    s=[]
    x=input("Enter the element 1::")
    y=input("Enter the element 2::")
    s.append(y)
    s.append(x)
    z=tuple(s)
    f.append(z)
t=tuple(f)
c=input("Enter the element to search::")
print(check_in_tuples(t,c))
