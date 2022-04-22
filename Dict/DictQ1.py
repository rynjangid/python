# Write a Python program to combine two dictionary adding values for common keys. d1 = {'a': 100, 'b': 200, 'c':300},d2 = {'a': 300, 'b': 200, 'd':400}
print("\n")
print("Aryan Jangir / 20BCS1671 ")

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

dict={}
for i in d1 :
    if i not in d2 :
        dict[i]=d1[i]
    else :
        dict[i]=(d1[i]+d2[i])
for j in d2 :
    if j not in dict :
        dict[j]=d2[j]

print(dict)
