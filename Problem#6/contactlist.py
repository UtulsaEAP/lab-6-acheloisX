def process_user_contacts(user_input):
    user_contacts = {}
    
    tokens = user_input.split(',')

    if len(tokens) % 2 != 0:
        print("Invalid input. Each name should be followed by a phone number.")
        return

    for i in range(0, len(tokens), 2):
        name = tokens[i].strip()  
        phone_number = tokens[i + 1].strip()  
        user_contacts[name] = phone_number

    contact_name = input("Enter the contact name: ")

    if contact_name in user_contacts:
        print(user_contacts[contact_name])
    else:
        print("Contact not found.")
