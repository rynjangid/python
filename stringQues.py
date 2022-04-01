

'''
x=input("enter the String: ")
l=len(x)
mid=int(l/2)
rev=-1
for i in range(mid):
    if(x[i]==x[rev]):
        rev=rev-1
    else:
        print("This string is Not palindrome")
        break
else:
    print("This string is palindrome")

---------------------------------------------------------------

str1 = input('Input sentence 1st : ')
str2 = input('Input sentence 2nd : ')

str1List = str1.split()
str2List = str2.split()
print(str1List)
print(str2List)
uncommonWords = ''
for words in str1List:
    if words not in str2List:
        uncommonWords = uncommonWords+" "+words
for words in str2List:
   if words not in str1List:
        uncommonWords = uncommonWords+" "+words
print("All uncommon words from both the sentence are: ", uncommonWords)

----------------------------------------------------------------

str1=input("Enter The String: ")
length = len(str1)
if length > 2:
    if str1[-3:] == 'ing':
        str1 += 'ly'
    else:
        str1 += 'ing'

print(str1)

'''

#svar=("m name is khan and i am not a terreist & proud to be an indian")
#print(svar.find("name"))

# list_svar=['my', 'name', 'is', 'khan', ',', 'i', 'am', 'not', 'a', 'terreist', ',', 'proud', 'to', 'be', 'an', 'indian']
# print((" ").join(list_svar))

# a=25
# b=2

# print(10 or "Ashu")
# print(10 and "Ashu")
# print(0 & 10)
# print("Ashu" and 10)
# print(a**b)

# print(not 0)

# print(eval("2+2/2"))
# print("2+2/2")

list = ["aryan", 123, 12.234,"bhai", False ]
print(list)

list.insert(1,"raja")
print(list)         