def parse_input(user_input: str):
    parts = user_input.split()
    if not parts:
        return "", []
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, *args


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:      # Kоли контакту з таким ім'ям немає
            return "Contact not found."
        except ValueError:     # Обробка помилки аргументів
            return "Give me name and phone, please."
        except IndexError:       # Помилка, коли команда phone викликана без імені
            return "Enter user name."
    return inner


@input_error
def add_contact(args, contacts: dict) -> str:   # Якщо args має не рівно 2 елементи – буде ValueError
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts: dict) -> str:    # ValueError, якщо аргументів не 2
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts: dict) -> str:    # Якщо користувач ввів просто "phone" без імені – IndexError
    name = args[0]   
    return contacts[name]     # Якщо такого імені немає у словнику – KeyError


@input_error
def show_all(contacts: dict) -> str:
    if not contacts:
        return "No contacts found."
    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")

        command, *args = parse_input(user_input)

        if not command:                # Коли порожній ввід = тільки пробіли
            print("Invalid command.")
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":        # очікуємо: add <name> <phone>
            print(add_contact(args, contacts))

        elif command == "change":     # очікуємо: change <name> <phone>
            print(change_contact(args, contacts))

        elif command == "phone":      # очікуємо: phone <name>
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
