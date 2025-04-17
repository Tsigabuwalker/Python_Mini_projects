master_pwd = input("What is the master password? ")

def view():
    try:
        with open("passwords.txt", 'r') as f:
            passwords = f.readlines()
            if passwords:
                print("Your saved passwords:")
                for line in passwords:
                    account, pwd = line.strip().split(':')
                    print(f"Account: {account}, Password: {pwd}")
            else:
                print("No passwords saved.")
    except FileNotFoundError:
        print("No passwords file found.")

def add():
    name = input("Add account name: ")
    pwd = input("Enter your password: ")
    with open("passwords.txt", 'a') as f:
        f.write(f"{name}:{pwd}\n")
    print("Password added.")

while True:
    mode = input("Would you like to add a new password or view existing ones? (add, view), press q to quit: ")
    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")