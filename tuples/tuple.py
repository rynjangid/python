# tuples and its methods

Books = ('DSA','Python','DBMS','COA')

print(type(Books))
x = print(len(Books))

# indexing

print(Books[1])
print(Books[1:2])
print(Books[0:])
print(Books[-1])
print(Books[-3:-1])
print(Books[-1::-1])

# looping
print('--------------------------------')

i=0
while i<4:
    print(Books[i])
    i += 1

print('--------------------------------')
for i in Books:
    print(i)

