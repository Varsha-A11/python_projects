import os

def create_file(filename):
    try:
        with open(filename,'x') as f:
            print(f'{filename} has been createed successfully')
    except FileExistsError:
        print(f'{filename} already exists')
    except Exception as e:
        print(f'an error occured')

def view_files():
    files=os.listdir()
    if not files:
        print("no files found")
    else:
        print("files in dir")
        for f in files:
            print(f)

def del_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully')
    except FileNotFoundError:
        print(f'{filename} not found')
    except Exception as e:
        print("an error occured",e)

def read_file(filename):
    try:
        with open(filename,'r') as f:
            content =f.read()
            print(f'content of file {filename}: {content}')
    except FileNotFoundError:
        print(f'{filename} not found')
    except Exception as e:
        print("an error occured")

def edit_file(filename):
    try:
        with open(filename,'a') as f:
            content=input("enter data u wanna add:")
            f.write(content+'\n')
            print(f'content to {filename} successfully')
    except FileNotFoundError:
        print(f'{filename} not found')
    except Exception as e:
        print("an error occured")

def main():
    while True:
        print("--- file management app---")
        print('1. create_file ')
        print('2. view all file ')
        print('3.delete file ')
        print('4. read file')
        print('5. edit file  ')
        print('6. exit ')

        choice=int(input("enter ur choice:"))

        if choice==1:
            filename=input("enter filename:")
            create_file(filename)

        elif choice==2:
            view_files()
        
        elif choice==3:
            filename=input("enter filename:")
            del_file(filename)

        elif choice==4:
            filename=input("enter filename:")
            read_file(filename)

        elif choice==5:
            filename=input("enter filename:")
            edit_file(filename)

        elif choice==6:
            print("closing program...")
            break

        else:
            print("something went wrg")

if __name__=="__main__":
    main()