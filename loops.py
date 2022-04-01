# While Loop

# print table of a given number

a = eval(input("Enter the no. of which u want table : "))

i = 1
while i <= 10:
    print(f"{a} * {i}", end=" = ")
    print(a*i)
    i += 1

# print prime no. till asked

b = eval(input("Enter the no. till u want to print prime no.s : "))

j = 2
while j <= b:
    if (((j % 2) == 0) & (j == 2)) or (((j % 3) == 0) & (j == 3)) or ((j % 5 == 0) & (j == 5)):
        print(j)
    if ((j % 2)==1) and ((j%3)!=0) and ((j%5)!=0):
        print(j)        
    j += 1

