print("\nAryan Jangir \n20BCS1671")
print("\n")
print("Ask user to give input the list which is initially empty & use all the list methods on it.\n")
print("---------- The Program is as Follows----------\n")

# user_list = ["Red","Green","White","Black","Pink","Yellow"]
# print("The given list is:-")
# print(user_list)

# print("After removing 1st, 5th and 6th positioned colors i.e. 0th, 4th and 5th indices data")
# print("We have...")

# user_list.pop(0)
# user_list.pop(3)
# user_list.pop(3)

# print(user_list)

'''---------------------------Code Second------------------------------------'''

empty_list = []
i = 1
while i < 5 :
    x=input()
    empty_list.append(x)
    i += 1

# empty_list.append("Aryan") 
# empty_list.append("Jangir") 
# empty_list.append("CSE") 
# empty_list.append("1671") 

print('hi')

empty_list.pop(2)                    # deleting data from position 3
print(empty_list)
empty_list.insert(2,"BE-CSE")        # Adding data at position 3
print(empty_list)
empty_list.remove("Jangir")          # deleting data by data_name
print(empty_list)
print(empty_list.index("Aryan"))     # gives data index by providing data



empty_list_2 = []

empty_list_2.append("Study_by") 
empty_list_2.append("Puneet_Sir") 

empty_list.extend(empty_list_2)

print(empty_list)

empty_list.clear()
print(empty_list)

i = 1
while i < 4 :
    empty_list.append(input(i))
    i += 1

print(empty_list)

empty_list.sort()
print(empty_list)



