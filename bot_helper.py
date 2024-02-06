import os 
list_contact=list()


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args



def show_all():
    print(list_contact)

def change_contact(*args):
    update=False                    
    for name in list_contact:
        iteam=name["Name"]
        if iteam==args[0]:
            update=True
            name["Number"]=args[1]
            print("Contact updated.")
    if update==False:
        print("Немає такого контакта")


def show_phone(*args):
    update=False
    for name in list_contact:
        iteam=name["Name"]
        if iteam==args[0]:
            print(name)
    if update==False:
        print("Немає такого, перевірте та спробуйте ще раз")

def main():
    os.system('cls')
    
    print("Welcome to the assistant bot!")
    
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command=="add":
            total_list={"Name":args[0],"Number":args[1]}
            list_contact.append(total_list)
            print("Contact added.")
        
        elif command=="change":     
            change_contact(*args)
                    
        elif command=="phone":
            show_phone(*args)

        elif command=="all":
            show_all()
        elif command in ["cls","clear"]:
            os.system('cls')
        else:
            print("Invalid command.")


            


if __name__ == "__main__":
    main()