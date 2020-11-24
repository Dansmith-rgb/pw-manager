import db
from cryptography.fernet import Fernet

#key = Fernet.generate_key()
#encryption_type = Fernet(key)

# welcome message function
def welcome():
    print("Hello and welcome to this password manager.")
    print("To get certain things please press these keys:")
    print("g = Get a password")
    print("c = Create a new password for app")
    print("l = Look at the first 50 rows of your data.")
    print("d = Delete a row of data")
    print("q = quit the program. All your data will be saved.")

# Calling welcome function.
welcome()

run = True

# Main loop
while run:
    func = input("")
    if func == "c":
        # Creating password username and email- creating record
        print("What app would you like to create a password for?")
        app = input("App name: ")
        print("What would you like the password to be?")
        global password
        global encryption_type
        password = bytes(input("Password:"), encoding='utf-8')
        key = Fernet.generate_key()
        encryption_type = Fernet(key)
        encrypted_message = encryption_type.encrypt(password)
        print("What is your username?")
        username = input("Username: ") 
        db.create_record(app,encrypted_message,username)
        print("You are back at the home part. Try calling a function.")
        #decrypted_message = encryption_type.decrypt(encrypted_message)
        #print(decrypted_message)
    elif func == "g":
        # Getting the password
        print("What app would you like the password for?")
        get_pw = input("")
        db.app_name_lookup(get_pw)
        #decrypted_message = encryption_type.decrypt(password)
        print("You are back at the home part. Try calling a function.")
    elif func == "l":
        # Showing the first 50 rows in the table/-- showing the first 50 records in the table.
        print("Here are the first 50 lines of your data. You will only see however much data you put in up to 50 rows. The rest is stored aswell.")
        db.look_at_table()
        print("You are back at the home part. Try calling a function.")

    elif func == "d":
        # Deleting the specified row of data from the table
        print("Which row of data would you like to delete. Specify the number. Look at the table if you are unsure what is on that row")
        delete = input("")
        db.delete_one(delete)
        print("You are back at the home part. Try calling a function.")

    elif func == "q":
        # Quitting the program
        print("Quitting program")
        break