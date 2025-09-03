# d={"s":1,"v":2}
# print(d["s"])              // it's 1  ~  _.[key]=value
import random

computer=random.choice([-1,0,1])
youstr=input("Choose :")
youdict={"Snake":1,"Water":-1,"Gun":0}
reversedict={1:"Snake",-1:"Water",0:"Gun"}
you=youdict[youstr]

#{youstr} or {reversedict[you]}

print(f"You chocie {reversedict[you]} \nComputer chocie {reversedict[computer]}")
if(computer==you):
    print("Oops!, Its a draw")
else:
    if(computer==-1 and you==1): 
        print("Hey! You won")
    elif(computer==-1 and you==0):
        print("Ayoo! You  loose")
    elif(computer==1 and you==0):
        print("Ayoo! You  loose")
    elif(computer==1 and you==-1):
        print("Hey! You won")
    elif(computer==0 and you==1):
        print("Ayoo! You  loose")
    elif(computer==0 and you==-1):
        print("Hey! You won")
    else:
        print("Something went wrong")  

    # if((computer-you)==-1 or (computer-you)==2 ):
    #     print("Ayoo! You loose")
    # else:
    #     print("Hey! You win ")         
