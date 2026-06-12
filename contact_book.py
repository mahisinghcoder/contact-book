contacts={}

while True:
    print("\n-------contact book-------")
    print("1. Add contact:")
    print("2. Search contact:")
    print("3. Display all contacts:")
    print("4. Exit")

    choice= input("Enter your choice:")
    if choice=="1":
        name=input("Enter contact name:")
        phone=input("Enter contact phone number:")
        contacts[name]=phone
        print("Contact added successfully!")

    elif choice=="2":
        name=input("Enter contact name to search:")
        if name in contacts:
            print(f"Contact found: {name} - {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice=="3":
        if contacts:
            print("All contacts:")
            for name, phone in contacts.items():
                print(f"{name} - {phone}")
        else:
            print("No contacts found.")

    elif choice=="4":
        print("Exiting contact book. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")