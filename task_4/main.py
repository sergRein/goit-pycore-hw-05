from address_book import show_menu, show_all_records, add_contact, change_contact, show_phone

def parse_input(user_input):
    parts = user_input.split() #split all input args
    cmd = parts[0].strip().lower() if parts else "" #separate comand from other args
    args = parts[1:] if len(parts) > 1 else [] #lets use list for not command args
    return cmd, args


def main():
    print("Welcome to the assistant bot")
    show_menu() #show available options
    address_book = {} #init address book
    while True:
        user_input = input("Enter a command: ") #get user input
        command, args = parse_input(user_input) 
        if command in ['close','exit']:
            print("Good bye!")
            break
        elif command == 'help':
            show_menu()
        elif command == 'all':
            show_all_records(address_book)
        elif command == 'add':
            add_contact(address_book, args)
        elif command == 'change':
            change_contact(address_book, args)
        elif command == 'phone':
            show_phone(address_book, args)
        else:
            print("Invalid command. Type `help` for available commands")




if __name__ == '__main__':
    main()