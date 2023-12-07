import json

def create_new_user(users):
    username = input("Enter your new username: ")

    while True:
        password = input("Create your password: ")
        if len(password) < 8 or password[0].isdigit() or ' ' in password:
            print("Invalid password. Please try again.")
        else:
            confirm_password = input("Re-enter your password to confirm: ")
            if password == confirm_password:
                users[username] = password
                print("New user created successfully!")
                break
            else:
                print("Passwords do not match. Please try again.")

    return users

def existing_user_login(users):
    username = input("Enter your username: ")
    if username in users:
        attempts = 3
        while attempts > 0:
            password = input("Enter your password: ")
            if users[username] == password:
                print("Welcome back! Login successful.")
                return True
            else:
                attempts -= 1
                print(f"Incorrect password. {attempts} attempts remaining.")

        print("You are locked out.")
        return False
    else:
        print("Username not found.")
        return False

def main_menu():
    users = load_users()
    
    while True:
        print("\nMenu:")
        print("1. New user")
        print("2. Existing user")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            users = create_new_user(users)
            save_users(users)
        elif choice == '2':
            if existing_user_login(users):
                break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def load_users():
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_users(users):
    with open("users.json", "w") as file:
        json.dump(users, file, indent=4)

main_menu()
