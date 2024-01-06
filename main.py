from password_generator import generate_password
from encryption import generate_key, encrypt_message, decrypt_message
import os

# File to store encrypted passwords
PASSWORD_FILE = 'passwords.txt'

def save_password(service, encrypted_password):
    with open(PASSWORD_FILE, 'a') as file:
        file.write(f'{service}:{encrypted_password.decode()}\n')

def get_password(service):
    if not os.path.exists(PASSWORD_FILE):
        return None
    with open(PASSWORD_FILE, 'r') as file:
        for line in file:
            stored_service, stored_encrypted_password = line.strip().split(':')
            if stored_service == service:
                return stored_encrypted_password
    return None

def main_menu():
    print("\nWelcome to the Password Manager")
    print("1. Generate a new password")
    print("2. Store a new password")
    print("3. Retrieve a stored password")
    print("4. Exit")
    return input("Choose an option: ")

def main():
    key = generate_key()  # In a real application, use a persistent and secure key

    while True:
        choice = main_menu()

        if choice == '1':
            length = int(input("Enter the desired length of the password: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")

        elif choice == '2':
            service = input("Enter the name of the service: ")
            password = input("Enter the password to store: ")
            encrypted_password = encrypt_message(password, key)
            save_password(service, encrypted_password)
            print("Password stored successfully.")

        elif choice == '3':
            service = input("Enter the name of the service: ")
            stored_encrypted_password = get_password(service)
            if stored_encrypted_password:
                password = decrypt_message(stored_encrypted_password.encode(), key)
                print(f"Password for {service}: {password}")
            else:
                print("No password found for this service.")

        elif choice == '4':
            print("Exiting Password Manager.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
