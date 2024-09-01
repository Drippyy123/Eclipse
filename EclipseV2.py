import os
from tkinter import Tk, Label, Button, Text, END
from cryptography.fernet import Fernet

# ASCII art banner
BANNER = r"""
███████╗ ██████╗██╗     ██╗██████╗ ███████╗███████╗   ██╗   ██╗███████╗██╗
██╔════╝██╔════╝██║     ██║██╔══██╗██╔════╝██╔════╝   ██║   ██║██╔════╝██║
███████╗██║     ██║     ██║██████╔╝█████╗  ███████╗   ██║   ██║███████╗██║
╚════██║██║     ██║     ██║██╔══██╗██╔══╝  ╚════██║   ╚██╗ ██╔╝╚════██║╚═╝
███████║╚██████╗███████╗██║██║  ██║███████╗███████║    ╚████╔╝ ███████║██╗
╚══════╝ ╚═════╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝     ╚═══╝  ╚══════╝╚═╝
"""

# Main application class
class FileEncryptorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ECLIPSE File Encryptor/Decryptor")
        
        # Display banner
        self.banner_label = Label(root, text=BANNER, font=("Consolas", 14), fg="magenta")
        self.banner_label.pack(pady=5)

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Generate key button
        self.gen_key_button = Button(self.root, text="Generate Key", command=self.generate_key)
        self.gen_key_button.pack(pady=5)

        # Encrypt file button
        self.enc_file_button = Button(self.root, text="Encrypt File", command=self.encrypt_file)
        self.enc_file_button.pack(pady=5)

        # Decrypt file button
        self.dec_file_button = Button(self.root, text="Decrypt File", command=self.decrypt_file)
        self.dec_file_button.pack(pady=5)

        # Status display
        self.status_text = Text(self.root, height=8, width=50)
        self.status_text.pack(pady=5)
        self.status_text.insert(END, "[+] ECLIPSE V2 ready.\n")

    def generate_key(self):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(key)
        self.update_status("[+] Key generated and saved as 'secret.key'.\n")

    def load_key(self):
        try:
            return open("secret.key", "rb").read()
        except FileNotFoundError:
            self.update_status("[!] Error: 'secret.key' not found.\n")
            return None

    def encrypt_file(self):
        file_name = "testfile.txt"  # Replace with actual file selection logic
        if os.path.exists(file_name):
            key = self.load_key()
            if key:
                fernet = Fernet(key)
                with open(file_name, "rb") as file:
                    file_data = file.read()
                encrypted_data = fernet.encrypt(file_data)
                with open(file_name, "wb") as file:
                    file.write(encrypted_data)
                self.update_status(f"[+] {file_name} has been encrypted.\n")
        else:
            self.update_status(f"[!] Error: File '{file_name}' does not exist.\n")

    def decrypt_file(self):
        file_name = "testfile.txt"  # Replace with actual file selection logic
        if os.path.exists(file_name):
            key = self.load_key()
            if key:
                fernet = Fernet(key)
                with open(file_name, "rb") as file:
                    encrypted_data = file.read()
                decrypted_data = fernet.decrypt(encrypted_data)
                with open(file_name, "wb") as file:
                    file.write(decrypted_data)
                self.update_status(f"[+] {file_name} has been decrypted.\n")
        else:
            self.update_status(f"[!] Error: File '{file_name}' does not exist.\n")

    def update_status(self, message):
        self.status_text.insert(END, message)
        self.status_text.see(END)


if __name__ == "__main__":
    root = Tk()
    app = FileEncryptorApp(root)
    root.mainloop()
