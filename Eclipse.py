import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("\n[+] Key generated and saved as 'secret.key'.\n")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(file_name, "wb") as file:
        file.write(encrypted_data)

    print(f"\n[+] {file_name} has been encrypted.\n")

def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(file_name, "wb") as file:
        file.write(decrypted_data)

    print(f"\n[+] {file_name} has been decrypted.\n")

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = """"                                             
▓█████  ▄████▄   ██▓     ██▓ ██▓███    ██████ ▓█████ 
▓█   ▀ ▒██▀ ▀█  ▓██▒    ▓██▒▓██░  ██▒▒██    ▒ ▓█   ▀ 
▒███   ▒▓█    ▄ ▒██░    ▒██▒▓██░ ██▓▒░ ▓██▄   ▒███   
▒▓█  ▄ ▒▓▓▄ ▄██▒▒██░    ░██░▒██▄█▓▒ ▒  ▒   ██▒▒▓█  ▄ 
░▒████▒▒ ▓███▀ ░░██████▒░██░▒██▒ ░  ░▒██████▒▒░▒████▒
░░ ▒░ ░░ ░▒ ▒  ░░ ▒░▓  ░░▓  ▒▓▒░ ░  ░▒ ▒▓▒ ▒ ░░░ ▒░ ░
 ░ ░  ░  ░  ▒   ░ ░ ▒  ░ ▒ ░░▒ ░     ░ ░▒  ░ ░ ░ ░  ░
   ░   ░          ░ ░    ▒ ░░░       ░  ░  ░     ░   
   ░  ░░ ░          ░  ░ ░                 ░     ░  ░
       ░                                                 """
    print(banner)
    print("    [+] Simple File Encryption/Decryption Tool [+]\n")
    print("       1) Generate Key")
    print("       2) Encrypt File")
    print("       3) Decrypt File")
    print("       4) Exit\n")
    print("======================================================\n")

def main():
    print_banner()

    while True:
        choice = input(">> Select an option: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            file_name = input(">> Enter the file name to encrypt: ")
            if os.path.exists(file_name):
                encrypt_file(file_name)
            else:
                print(f"\n[!] File '{file_name}' does not exist.\n")
        elif choice == "3":
            file_name = input(">> Enter the file name to decrypt: ")
            if os.path.exists(file_name):
                decrypt_file(file_name)
            else:
                print(f"\n[!] File '{file_name}' does not exist.\n")
        elif choice == "4":
            print("\n[+] Exiting... Goodbye!\n")
            break
        else:
            print("\n[!] Invalid option. Please choose again.\n")

if __name__ == "__main__":
    main()
