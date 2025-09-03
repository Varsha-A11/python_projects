contacts={}

print('contact book app')
while True:
    print('1.create contact')
    print('2.update contact')
    print('3.view contact')
    print('4.delete contact')
    print('5.search contact')
    print('6.count contact')
    print('7.exit')

    choice=input("enter ur choice:")

    if choice=='1':
        name=input("enter name:")
        if name in contacts:
            print(f"{name} is already in contacts")
        else:
            age=input("enter age:")
            email=input("enter gmail:")
            phone_num=input("enter moblie num:")
            contacts[name]={'age':int(age),'email':email,'phone_num':phone_num}
            print(f'contact {name} has been created succesfully')

    elif choice=='3':
        name=input("enter name:")
        if name in contacts:
            cont=contacts[name]
            print(f'Name:{name} age:{age} email:{email} phone number:{phone_num}')
        else:
            print(f'{name} not in ur contacts')

    elif choice=='2':
        name=input("enter name:")
        if name in contacts:
            age=input("enter updatedage:")
            email=input("enter updated gmail:")
            phone_num=input("enterupdated moblie num:")
            contacts[name]={'age':int(age),'email':email,'phone_num':phone_num}
            print(f'contact {name} has been updated succesfully')
        else:
            print("contact not found")

    elif choice=='4':
        name=input("enter name:")
        if name in contacts:
            del contacts[name]
            print(f'contact {name} has been deleted sucsessfully')
        else:
            print("contact not found")

    elif choice=='5':
        search_name=input("enter name u wanna search:")
        found=False
        for name,contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f'found- name:{name} age:{age} email:{email}')
                found=True
        if not found:
            print(f'{search_name} not found in contacts name')

    elif choice=='6':
        print(f'total contacts {len(contacts)}')

    elif choice=='7':
        print("closing program ")
        break
    
    else:
        print("invaild input")

