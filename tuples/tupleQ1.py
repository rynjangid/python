def tup(f):
    print("The original list is : " , str(f))
    u=int(input("Enter the number which you want to insert::"))
    o=input("Enter the string which you want to insert::")
    repl_rec = (str(o), u)
    f.pop(l-1)
    f.insert(l-1,repl_rec)
    print("After the removing the element from tuple",f)
f=[]
l=int(input("Enter the length of tuple::"))
for i in range(l):
    s=[]
    x=int(input("Enter the number::"))
    y=input("Enter the string::")
    s.append(y)
    s.append(x)
    z=tuple(s)
    f.append(z)

tup(f)
