rent= int(input("Enter flat number ="))
food= int(input("Enter the food ordered amount ="))
electricity_charge=int(input("Enter the electricity charge ="))
charge_per_unit=int(input("Enter the charge per unit ="))
person=int(input("Enter the number of persons ="))

electricity_bill=electricity_charge* charge_per_unit

pay=(rent+food+electricity_bill)//person

print("each person has to pay :",pay)