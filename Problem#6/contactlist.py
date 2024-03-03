def process_user_contacts(user_input):
    user_contacts = {}
    
    tokens = user_input.split(',')

    for i in range(0, len(tokens), 2):
        name = tokens[i].strip()  
        phone_number = tokens[i + 1].strip()  
        user_contacts[name] = phone_number

    contact_name = input("Enter the contact name: ")

    if contact_name in user_contacts:
        # Output contact's phone number
        print(user_contacts[contact_name])
    else:
        print("Contact not found.")
if __name__ == '__main__':
    user_input = input("Enter word pairs (name, phone number): ")
    process_user_contacts(user_input)