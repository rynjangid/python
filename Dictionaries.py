# Dictionaries

dict={"Aryan":1671,"Vishal":1725,"Prashant":1653}

print(dict)
print(type(dict))
x = dict["Aryan"]
print(x)
print(dict.get("Vishal"))
print(dict.get("Prashant"))
y = dict.keys()
print(y)
print(dict.values())

print(len(dict))

# methods

z = dict.update({"prashant_S":1677})
print(z)
print(dict)

dict.pop("Prashant")
print(dict)

dict.clear()
print(dict)

# user defined

d = {}                       # empty <dict>

r = eval(input("Enter no. of  key paires u want : "))
i = 1
while i <= r:
    a = eval(input(f"Enter key {i}: "))
    b = eval(input(f"Enter value {i}: "))
    d.update({a:b})
    i += 1

print("\n")
print(d)
