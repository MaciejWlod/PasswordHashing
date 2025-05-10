from argon2 import PasswordHasher

# Initialize the password hasher
ph = PasswordHasher()

# Dictionary to store usernames and hashed passwords
users = {}

def createUser():
    username = input("Enter Username ")
    if username in users:
        print("This Username is taken ")
        return
    password = input("What is your password? ")
    hashed = ph.hash(password)
    users[username] = hashed

def logIn():
    input1 = input("Do you have a accound? Yes or No\n")
    if input1 == "No":
        createUser()
    else:
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

def showDatabase():
    print(users)

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




       

