print("This program is made by aryan")
print("With the help of this program we are able to learn the concept of modular approch")
def aryan():
    print("Which supper power I will use")
    print("1-Healing")
    print("2-Fly")
    print("3-Time-travel")
    x=int(input("enter the choice:"))
    if(x==1):
          print("1-I will heal my friend")
          print(heal())
          print("Healing energy is lost")
          print("Now I am left with time travel and Fly powers")
    elif(x==2):
        print("1-I will use my flying power")
        print(fly())
        print("Now I am left with time-travel power")
    elif(x==3):
          print("Accident happned")
          print(notsave())
    else:
        print("invalid move!")
    z=input("Do you want to countinue : ")
    if(z=="yes"):
        aryan()
    else:
        print("thanks")
def heal():
    return("I am able to heal the friend")
def fly():
    return("I can fly and take him to hospital")
def notsave():
    return("Accident haapend and he died as I dont have any useful power left")
aryan()
