import re

com_exit = ("exit" or "close")
def parse_input(our_command):
    cmd, *args = our_command.split()
    cmd = cmd.strip().lower()
    return cmd, *args
def add_numbers(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "contacts added"
def changed_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "contact changed"
    else:
        return "contact doesnt exist"
def show_phone(args, contacts):
    if args[0] in contacts:
        print(f"The phone number for {args[0]}: {contacts[args[0]]}")
    else:
        print("Contact not found.")
def show_all(contacts):
    print(contacts)
def main():
    contacts = {}
    print("Hello, its ur personal Helper")
    while True:                
        our_command = input("Enter a command: ").strip().lower()
        command, *args = parse_input(our_command)
        if command == com_exit:
            print("bye")
            break
        elif command == "hello":
            print("How i can help you: ")
        elif command == "add":
            print(add_numbers(args, contacts))
        elif command == "change":
            print(changed_contact(args, contacts))
        elif command == "find":
            show_phone(args, contacts)
        elif command == "all":
            show_all(contacts)                        
if __name__ == "__main__":
    main()             