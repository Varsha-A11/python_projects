import random
n=random.randint(1,100)
a=-1
guess=0
print("Game: Guess the Perfrct number!!")
while(a!=n):
    guess+=1
    a=int(input("guess the number:"))
    if(a>n):
        print(f"guess number lower than {a}")
    else:
        print(f"guess number higher than {a}")

print(f'you have guessed correct number {n} in {guess} attmepts')