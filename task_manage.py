def task():
    tasks=[]
    print("---welcome to task management app ---")

    total_tasks=int(input("enter numbers of tasks:"))
    for i in range(1,total_tasks+1):
        tasks_name=input(f'enter tasks {i}:')
        tasks.append(tasks_name)

    print("todays tasks are :",tasks)

    while True:
        oper= int(input("enter which u operation u want 1-add,2-update,3-delete,4-view,5-exit :"))
        if oper==1:
            add=input("enter the task u wanna add:")
            tasks.append(add)
            print(f'{add} has been added')

        elif oper==2:
            update_val=input("enter the task u wanna update:")
            if update_val in tasks:
                up=input("enter new task:")
                ind=tasks.index(update_val)
                tasks[ind]=up  
                print(f'{up} has been updated') 

        elif oper==3:
            del_val=input("enter task u wanna delete:")
            if del_val in tasks:
                ind=tasks.index(del_val)
                del tasks[ind]
                print(f'{del_val} has been deleted')
        
        elif oper==4:
            print(f'total tasks :{tasks}')

        elif oper==5:
            print("closing the tasks ")
            break

        else:
            print("opps! something went wrg!!")

task()            