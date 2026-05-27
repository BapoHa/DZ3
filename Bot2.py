def input_error(func):
   
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Введіть ім'я та номер телефону."
        except KeyError:
            return "Введіть ім'я користувача."
        except IndexError:
            return "Введіть аргумент для команди."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):    # add new contact to the book
    name, phone = args              # ValueError if args does not contain exactly 2 elements
    contacts[name] = phone
    return "Контакт додано."


@input_error
def change_contact(args, contacts): # change phone number of existing contact
    name, phone = args              # ValueError if args does not contain exactly 2 elements
    if name not in contacts:
        return "Контакт не знайдено."
    contacts[name] = phone
    return "Контакт оновлено."


@input_error
def show_phone(args, contacts):     #return phone number of contact by name
    name = args[0]                  # IndexError if args is empty
    if name not in contacts:
        return "Контакт не знайдено."
    return contacts[name]


@input_error
def show_all(contacts):             # return all contacts in the book
    if not contacts:
        return "Контакти не знайдено."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def show_help():                    # return list of available commands
    commands = [
        "hello / hi                     - привітання",
        "add <ім'я> <телефон>           - додати контакт",
        "change <ім'я> <телефон>        - змінити номер контакту",
        "phone <ім'я>                   - показати номер контакту",
        "all                            - показати всі контакти",
        "help                           - список команд",
        "close / exit / bye             - завершити роботу",
    ]
    return "Доступні команди:\n" + "\n".join(commands)


def main():
    contacts = {}
    print("Ласкаво просимо до бота-помічника! Введіть команду 'help' для перегляду доступних команд.")

    while True:
        user_input = input("Введіть команду: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "bye"]:
            print("Допобачення!")
            break
        elif command in ["hello", "hi"]:
            print("Привіт! Як я можу допомогти?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(show_help())
        else:
            print("Невідома команда.")


if __name__ == "__main__":
    main()
