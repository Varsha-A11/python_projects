History_file="history.txt"

def show_history():
    with open('history.txt','r') as file:
        lines=file.readlines()
        if len(lines)==0:
            print("No history Found!")
        else:
            for line in reversed(lines):
                print(line.strip())
def clear_history():
    with open('history.txt','w') as file:
        print("history cleared!")
def save_to_history(equation,result):
    with open('history.txt','a') as file:
        file.write(equation+"="+str(result)+"\n")

def calulate(user_ip):
    parts=user_ip.split()
    if len(parts)!=3:
        print("invaild input, use format num operator num eg: 8 + 8 ")
        return
    
    num1=float(parts[0])
    oper=parts[1]
    num2=float(parts[2])

    if oper=="+":
        result=num1+num2
    elif oper=="-":
        result=num1-num2
    elif oper=="*":
        result=num1*num2
    elif oper=="/":
        try:
            result=num1/num2
        except ZeroDivisionError as e:
            print("can't divide",e)
            return
    else:
        print("Invaild operation ")
        return
    
    if int(result)==result:
        result=int(result)

    print("Result:",result)
    save_to_history(user_ip,result)
    
def main():
    print("----simple calulator (type history,clear or exit):")
    while True:
        user_ip=input("enter calulation (+,-,*,/) or command(histroy,clear,exit): ")
        if user_ip=="exit":
            print("goodbye")
            break
        elif user_ip=='history':
            show_history()
        elif user_ip=="clear": 
            clear_history()
        else:
            calulate(user_ip)

main() 