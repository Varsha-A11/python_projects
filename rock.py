import random

computer=random.choice([-1,0,1])
youstr=input("enter ur choice:")
dict={"rock":-1,"paper":0,"scissor":1}
reversedict={-1:"rock",0:"paper",1:"scissor"}
you=dict[youstr]

print(f"you choice: {reversedict[you]}\ncomputer choice: {reversedict[computer]}")

if(computer==you):
    print("its a draw")

else:
    if(computer==-1 and you==1):
        print("you loose")
    elif(computer==-1 and you==0):
        print("you won") 
    elif(computer==1 and you==0):
        print("you loose")  
    elif(computer==1 and you==-1):
        print("you won")  
    elif(computer==0 and you==-1):
        print("you loose")                     
    elif(computer==0 and you==1):
        print("you won")
    else:
        print("something went wrg!!")      
