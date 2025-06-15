#Shamini
#Task-5
#Contact Book

contacts = []  # list to store contacts as dictionaries

def add_contact():
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✔ Contact added!")

def view_contacts():
    if not contacts:
        print(" No contacts found.")
    else:
        print("\nName\t\tPhone")
        for c in contacts:
            print(f"{c['name']}\t\t{c['phone']}")

def search_contact():
    term = input("Enter name or phone to search: ")
    found = False
    for c in contacts:
        if term.lower() in c["name"].lower() or term in c["phone"]:
            print(f"\nName: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
            found = True
    if not found:
        print("⚠ No records found.")

def update_contact():
    term = input("Enter name or phone of contact to update: ")
    for c in contacts:
        if term.lower() in c["name"].lower() or term in c["phone"]:
            print("Leave blank to keep current value.")
            c["name"] = input(f"New name (current: {c['name']}): ") or c["name"]
            c["phone"] = input(f"New phone (current: {c['phone']}): ") or c["phone"]
            c["email"] = input(f"New email (current: {c['email']}): ") or c["email"]
            c["address"] = input(f"New address (current: {c['address']}): ") or c["address"]
            print("✔ Contact updated!")
            return
    print("⚠ No matching contact found.")

def delete_contact():
    term = input("Enter name or phone of contact to delete: ")
    for i, c in enumerate(contacts):
        if term.lower() in c["name"].lower() or term in c["phone"]:
            confirm = input(f"Delete {c['name']}? (y/n): ")
            if confirm.lower() == 'y':
                contacts.pop(i)
                print(" Contact deleted!")
            else:
                print("Deletion cancelled.")
            return
    print("⚠ No matching contact found.")

def main():
    while True:
        print("\n===== Contact Book =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print(" Invalid choice. Please select 1-6.")

if __name__ == "__main__":
    main()
