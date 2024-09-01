import os
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Success", "Key generated and saved as 'secret.key'.")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file():
    file_name = filedialog.askopenfilename(title="Select a file to encrypt")
    if file_name:
        key = load_key()
        fernet = Fernet(key)

        with open(file_name, "rb") as file:
            file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)

        with open(file_name, "wb") as file:
            file.write(encrypted_data)

        messagebox.showinfo("Success", f"{file_name} has been encrypted.")

def decrypt_file():
    file_name = filedialog.askopenfilename(title="Select a file to decrypt")
    if file_name:
        key = load_key()
        fernet = Fernet(key)

        with open(file_name, "rb") as file:
            encrypted_data = file.read()

        decrypted_data = fernet.decrypt(encrypted_data)

        with open(file_name, "wb") as file:
            file.write(decrypted_data)

        messagebox.showinfo("Success", f"{file_name} has been decrypted.")

def create_ui():
    root = tk.Tk()
    root.title("File Encryptor/Decryptor")

    label = tk.Label(root, text="File Encryptor/Decryptor", font=("Arial", 16))
    label.pack(pady=10)

    generate_key_button = tk.Button(root, text="Generate Key", command=generate_key)
    generate_key_button.pack(pady=5)

    encrypt_file_button = tk.Button(root, text="Encrypt File", command=encrypt_file)
    encrypt_file_button.pack(pady=5)

    decrypt_file_button = tk.Button(root, text="Decrypt File", command=decrypt_file)
    decrypt_file_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.quit)
    exit_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
