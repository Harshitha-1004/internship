import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

# Add new contact
def add_contact(contacts):
    print("\n📝 Add New Contact")
    name = input("Name: ").strip()
    phone = input("Phone Number: ").strip()
    email = input("Email: ").strip()
    address = input("Address: ").strip()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print(f"✅ Contact '{name}' added successfully.")

# View contact list (only names and phones)
def view_contacts(contacts):
    print("\n📒 Contact List")
    if not contacts:
        print("No contacts saved yet.")
        return
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

# Search by name or phone
def search_contact(contacts):
    print("\n🔍 Search Contact")
    keyword = input("Enter name or phone: ").strip().lower()
    found = [c for c in contacts if keyword in c["name"].lower() or keyword in c["phone"]]
    if not found:
        print("❌ No contact found.")
        return
    for c in found:
        print(f"\nName: {c['name']}")
        print(f"Phone: {c['phone']}")
        print(f"Email: {c['email']}")
        print(f"Address: {c['address']}")

# Update a contact
def update_contact(contacts):
    print("\n✏️ Update Contact")
    search_name = input("Enter name of the contact to update: ").strip().lower()
    for c in contacts:
        if c["name"].lower() == search_name:
            print(f"Editing contact: {c['name']}")
            c["phone"] = input(f"New Phone ({c['phone']}): ").strip() or c["phone"]
            c["email"] = input(f"New Email ({c['email']}): ").strip() or c["email"]
            c["address"] = input(f"New Address ({c['address']}): ").strip() or c["address"]
            print("✅ Contact updated.")
            return
    print("❌ Contact not found.")

# Delete a contact
def delete_contact(contacts):
    print("\n🗑️ Delete Contact")
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for i, c in enumerate(contacts):
        if c["name"].lower() == name:
            del contacts[i]
            print(f"✅ Contact '{c['name']}' deleted.")
            return
    print("❌ Contact not found.")

# Main menu interface
def main():
    contacts = load_contacts()
    while True:
        print("\n📘 CONTACT BOOK MENU")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Save and Exit")

        choice = input("Select an option (1-6): ").strip()
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("📁 Contacts saved. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
