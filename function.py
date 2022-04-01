# functions and its types

def read():                                      # decl. and def. with no return and no argument
    print("Aryan function aata h? ")
    print("haan bilkul! ")

read()                                           # calling function

print("\n")
def func2(x,y):                                  # 2 parameters are passed 
    c = x+y
    print(c)

func2(2,5)

print("\n")
def func3(*arg):                                # limitless arguments can be passed
    print(arg)
    print(sum(arg))

func3(20,30,40)


print("\n")
def func4(x):                                   # single argument is passed with return value
    return x*5

print(func4(4))

print("\n")
def func5(name,age=22):                         # Default value assignment in arguments
    print(name)
    print(age)

func5("Ankita", 20)
func5("Aryan")

print("\n")
def func6(st3,st1,st2,st5,st4):                 # Assignment through keyword in argument 
    print(f"{st2} and {st5} are fabulous in playing Table Tennis." )

func6(st1="Tony",st2="Sujal",st3="Aryan",st4="Ruchir",st5="Prashant")


