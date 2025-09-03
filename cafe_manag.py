menu={
    'pizza':199,
    'pasta':80,
    'burger':60,
    'salad':70,
    'coffee':50
}

print("---welcome to python cafe---")
print("menu:")
for food,price in menu.items():
    print(f'{food}:{price}')

order_total=0

item1=input("enter item u wannna order:")
if item1 in menu:
    order_total+=menu[item1]
    print(f' ur {item1} has been added to order')
else:
    print(f'{item1} is not yet avaliable')

while True:
    another_item=input("do u wanna  order another item? (yes/no):").lower()
    if another_item=='yes':
        item2=input("enter name of second item:")
        if item2 in menu:
            order_total+=menu[item2]
            print(f'{item2} has been added to order')
        else:
            print(f"{item2} not yet avaliable")
    elif another_item=='no':
        print(f'thank you for your order! total amount to pay :{order_total}')
        break
    else:
        print("please enter yes or no")