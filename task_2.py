def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def show_all(contacts):
    if not contacts:
        return "Your phone book is empty."

    contacts_data = ""

    for name, phone in contacts.items():
        contacts_data += f"|{name:^15}|{phone:^25}|\n"

    return contacts_data.rstrip("\n")


def show_phone(args, contacts):
    try:
        name = args[0]
    except IndexError:
        return "Invalid arg. Enter: phone <name>"
    else:
        phone = contacts.get(name)

        if phone:
            return phone
        else:
            return f"A person with name {name} is not in your phone book"


def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid args. Enter: add <name> <phone>"
    else:
        if name in contacts:
            return f"A person with name {name} already exists."

        contacts[name] = phone
        return "Contact added."


def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Invalid args. Enter: change <name> <phone>"
    else:
        if not name in contacts:
            return f"A person with name {name} is not in your phone book"

        contacts[name] = phone
        return "Contact updated."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input(">>> Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            print(show_all(contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
