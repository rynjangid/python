def mutiple_tuple(nums):
    temp = list(nums)
    product = 1
    for x in temp:
        product *= x
    return product
f=[]
l=int(input("Enter the length of list::"))
for i in range(l):
    x=int(input("Enter the element 1::") )
    f.append(x)
t=tuple(f)
print(mutiple_tuple(t))
