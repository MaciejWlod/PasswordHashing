from argon2 import PasswordHasher

# Initialize the password hasher
ph = PasswordHasher()

# Dictionary to store usernames and hashed passwords
# Dictionary = Key = Username : Value = Hashed Password
users = {}


# This function creates a new users.
# It checks if a username is already in the database.
# And Stores hashed password

def createUser():
    username = input("Enter Username ")
    if username in users:
        print("This Username is taken ")
        return
    password = input("What is your password? ")
    hashed = ph.hash(password)
    users[username] = hashed


#This function allows you to login if your account is already stored in the database.
def logIn():
    input1 = input("Do you have a accound? Yes or No\n")
    if input1.lower() == "no":
        createUser()
    elif input1.lower() == "yes":
        username = input("Enter Username ")
        if username not in users:
            print("Wrong Username")
            logIn()
        else:
            password = input("Enter Password ")
            hashpassword = users[username]
            if ph.verify(hashpassword, password):
                print("Password is correct. Access granted!\n")
            else:
                print("Incorrect password. Access denied.\n")


# You have the option to return to Main Menu or Delete your account
    print("1. Delete account")
    print("2. Go back to the Main Menu")
    choice = input("Select an option (1-2): ")
    if choice == "1":
        users.pop(username)
        print("your account deleted successfully !")
        return
    if choice == "2":
        return
   
# Prints current state of the Database
def showDatabase():
    print(users)


# Main Function that allows multiply diffrent choices
def main():
    while True:
        print("1. Create new user")
        print("2. Login")
        print("3. Show Me The Database")
        print("4. Exit")
        choice = input("Select an option (1-4): ")

        if choice == '1':
            createUser()
        elif choice == '2':
            logIn()
        elif choice == '3':
            showDatabase()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()




       

