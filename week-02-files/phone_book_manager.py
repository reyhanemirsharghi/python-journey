contacts = {}
while True:
    print("===== Phone Book =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. View All Contacts")
    print("4.Exit")

    try:
        action = int(input("Please enter a number from menu: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if action == 1:
        name = input("name: ")
        phone = input("phone: ")
        if name not in contacts:
            contacts[name] = phone
        else:
            print("This contact already exists.")
    elif action == 2:
        name = input("Name: ")
        if name in contacts:
            print(contacts.get(name))
        else:
            print("Contact not found.")
    elif action == 3:
        if not contacts :
            print("No contacts found.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
    elif action == 4:
        break
    else:
        print("Please select a number from menu.")