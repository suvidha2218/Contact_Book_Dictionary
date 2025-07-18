#contact book using lists and dictionaries
contacts=[]

#add contact
def add_contact():
    name=input("Enter name:")
    phone=input("Enter phone number:")
    email=input("Enter email:")
    contacts.append({"name":name,"phone":phone,"email":email})
    print("contact added successfully!")
#display contact
def display_contacts():
    if not contacts:
        print("no contact found.")
        return
    for contact in contacts:
        print(f"Name:{contact['name']},Phone:{contact['phone']},Email:{contact['email']}")

#search contact
def search_contact():
    name=input("Enter name to serach:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            print(f"Name:{contact['name']},Phone:{contact['phone']},Email:{contact['email']}")
            return
    print("contact not found.")
#delect contact
def delete_contact():
    name=input("enter name to delete:")
    for contact in contacts:
        if contact["name"].lower()==name.lower():
            contacts.remove(contact)
            print("contact deleted successfully")
            return
    print("contact not found.")

#main menu
def main():
    while True:
        print("\n1.add contact\n2.display contacts\n3.serach contact\n4.delete contact\n5.exits")
        choice=input("enter choice:")
        if choice=='1':
            add_contact()
        elif choice=='2':
            display_contacts()
        elif choice=='3':
            search_contact
        elif choice=='4':
           delete_contact()
        elif choice=='5':
            print("goodbye!")
            break
        else:
            print("invaild check,try again")
main()