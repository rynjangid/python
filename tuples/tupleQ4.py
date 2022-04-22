f=[]
l=int(input("Enter the length of list::"))
for i in range(l):
    x=int(input(f"Enter the element {i}::") )
    f.append(x)
t=tuple(f)
q=str(t)
print("The original string is : " + q)
res = tuple(int(num) for num in q.replace('(', '')
 .replace(')', '').replace('...', '').split(', '))
print("The tuple after conversion is : " + str(res))
