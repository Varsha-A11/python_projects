student_grades={}

def add_student(name,grade):
    student_grades[name]=grade
    print(f'added {name} with {grade}')

def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f'{name} with updated grade {grade}') 
    else:
        print(f'{name} not found') 

def del_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f'{name} has been removed')
    else:
        print(f'{name} not found') 

def display_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f'{name}:{grade}')
    else:
        print("no students")

print('student grade management')
def main():
    while True:
        print('1-add,2-update,3-delete, 4-view, 5-exit ')

        choice=int(input("enter ur choice:"))
        if choice==1:
            name=input("enter name:")
            grade=int(input("enter grade:"))
            add_student(name,grade)
        
        elif choice==2:
            name=input("enter name:")
            grade=int(input("enter grade:"))
            update_student(name,grade)
        
        elif choice==3:
            name=input("enter name:")
            del_student(name)

        elif choice==4:
            display_student()

        elif choice==5:
            print("closing program")
            break

        else:
            print("oops! somthing went wrg")

main()