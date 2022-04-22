# Write a Python program to find the highest 3 values of corresponding keys in a dictionary.

print("\n")
print("Aryan Jangir / 20BCS1671 ")
r = eval(input("Enter no. key-pair value:-"))
Dict = {}
List1 = []
List2 = []

i = 1
while i <= r:
    a = eval(input(f"Enter key{i} key: "))
    b = eval(input(f"Enter key{i} value: "))
    List1.append(a)
    List2.append(b)
    Dict.update({a:b})
    i += 1

print("Entered Dictionary is :\n")
print(Dict)

List2.sort()
List2.reverse()

print(List2)

print("Key" , ":", "Value")

print(List1[4],":",List2[0])
print(List1[5],":",List2[1])
print(List1[1],":",List2[2])

