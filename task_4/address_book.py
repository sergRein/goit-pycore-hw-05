from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError: 
            print("No such user")
        except IndexError: 
            print("Contact not found")
        except ValueError:
            print("Give me name and phone please.")

    return inner


def show_menu(): #print menu with available options
    MENU = """
    Commands for use:
        help -- show available commands
        all -- show all phones in address book
        add [name] [phone] -- add new record
        change [name] [phone] -- change phone number for user with name [name]
        phone [name] -- show phone for user with name [name]
        close or bye -- exit from program
    """
    print(MENU)


def show_all_records(address_book):
    if not address_book: #if empty
        print("Address book is empty, add some records first")
        return

    for name, phone in address_book.items():
        print(f"{name}: {phone}")

@input_error
def add_contact(address_book, args):
    if len(args) != 2:
        raise ValueError

    name, phone = args
    if name in address_book: #if name already in book
        print(f"Phone for user {name} already in book? if you want to change number use `change [name] [phone] command`")
        raise KeyError
    else:
        address_book[name] = phone
        print("Contact added")

@input_error
def change_contact(address_book, args):
    if len(args) != 2:
        raise ValueError
    
    name, phone = args
    if name in address_book:
        address_book[name] = phone
        print("Contact changed")
    else:
        raise KeyError

@input_error
def show_phone(address_book, args):
    if len(args) != 1:
        raise ValueError
    
    name = args[0]
    if name in address_book:
        print(f"{name} phone is {address_book[name]}")
    else:
        raise IndexError