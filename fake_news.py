# step 1 - import the random module
import random
# 2- create a list of subjects
Subjects=[
    "SRK",
    "Mumbai Cat",
    "A monkey",
    "Auto rickshaw from Delhi",
    "Taj Mahal",
    "A street dog",
    "Virat Kohli",
    "India Gate",
    "Dr.S.Jaishankar"
]
actions=[
    "lauches",
    "cancels",
    "dances ",
    "eats",
    "declares a war",
    "orders",
    "celebrates"
]
places_or_things=[
    "at red fort",
    "in mumbai local tarin",
    "plate of dosa",
    "inside parliament",
    "at ganga ghat",
    "during IPL match",
    "India gate"
]
# start the headline generating loop
while True:
    Subject=random.choice(Subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    headline= f"Breaking news:{Subject} {action} {place_or_thing}"
    print("\n"+headline)
    user_ip=input("do u want another headline?(yes/no): ").strip().lower()
    if user_ip=="no":
        break

# goodbye msg
print("\nThanks for using fake news headline generator. Have a fun day!")

