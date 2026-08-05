while True:
    print("===== Contact Manager =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    try:
        number = int(input("choose a number from menu: "))
    except ValueError:
        print("please enter a number. ")
        continue

    if number == 1 :
        name = input("Name: ")
        phone_number = input("Phone number: ")
        with open ("contact.txt", "a") as f:
            f.write(f"{name},{phone_number}\n")
        
    elif number == 2:
        try:
            with open ("contact.txt") as f:
                content = f.read()
        except FileNotFoundError:
            print("File Not Foun. ")
            continue

        if content == "":
            print("No contacts found. ")
            continue
        else:
            print(content)
        
    elif number == 3:
        break
    else:
        print("please select a number from menu")