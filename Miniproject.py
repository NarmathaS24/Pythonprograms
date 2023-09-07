import os
import datetime

def signup():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    with open("passwords.txt", "a") as f:
        f.write(username + ":" + password + "\n")
    os.mkdir(username)
    print("Account created successfully")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("passwords.txt", "r") as f:
        found = False
        for line in f:
            if line.strip() == username + ":" + password:
                found = True
                break
        if not found:
            print("No user found")
            return
    while True:
        choice = input("Choose an option:\n1. Read your entries\n2. Make an entry\n3. Exit\n")
        if choice == "1":
            entries = [f for f in os.listdir(username) if os.path.isfile(os.path.join(username, f))]
            if not entries:
                print("No entries found")
            else:
                print("Choose an entry to read:")
                for i, entry in enumerate(entries):
                    print(str(i+1) + ". " + entry)
                choice = input()
                try:
                    index = int(choice) - 1
                    with open(os.path.join(username, entries[index]), "r") as f:
                        print(f.read())
                except (ValueError, IndexError):
                    print("Invalid choice")
        elif choice == "2":
            entry = ""
            print("Write your entry (press Enter three times to finish):")
            while True:
                line = input()
                if line == "" and entry.endswith("\n\n"):
                    break
                entry += line + "\n"
            filename = datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
            with open(os.path.join(username, filename), "w") as f:
                f.write(entry)
            print("Entry saved successfully")
        elif choice == "3":
            break
        else:
            print("Invalid choice")

while True:
    choice = input("Choose an option:\n1. Log in\n2. Sign up\n")
    if choice == "1":
        login()
    elif choice == "2":
        signup()
    else:
        break
