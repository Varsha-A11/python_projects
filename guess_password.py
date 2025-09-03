import random

easy_words=["apple","train","tiger","money","india"]
medium_words=["python","bottle","monkey","planet","laptop"]
hard_words=["elephant","diamond","umbrella","computer","mountain"]

print("Welcome to the password guessing")
print("choice a difficulty level (easy,medium,hard)")
level=input("enter difficulty level:").lower()
if level=="easy":
    secret=random.choice(easy_words)
elif level=="medium":
    secret=random.choice(medium_words)
elif level=="hard":
    secret=random.choice(hard_words)
else:
    print("invalid choice. Default to easy level")
    secret=random.choice(easy_words)

attempts=0
print("Guess the secret password")
while True:
    guess=input("enter your guess:").lower()
    attempts+=1
    if guess==secret:
        print(f"congrats u guessed in {attempts} attempts")
        break

    hint=""

    for i  in range(len(secret)):
        if i<len(guess) and guess[i]==secret[i]:
            hint+=guess[i]
        else:
            hint+="_"

    print("Hint:",hint)
print("game over")