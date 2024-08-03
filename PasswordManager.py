import os
import json
import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import random
import string

# Function to generate a key and save it into a file
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to load the key from the current directory named `key.key`
def load_key():
    return open("key.key", "rb").read()

# Generate and load key
if not os.path.exists("key.key"):
    generate_key()
key = load_key()
cipher_suite = Fernet(key)

# Function to encrypt a password
def encrypt_password(password):
    encrypted_password = cipher_suite.encrypt(password.encode())
    return encrypted_password

# Function to decrypt a password
def decrypt_password(encrypted_password):
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode()
    return decrypted_password

# Function to add a password
def add_password(service, password):
    encrypted_password = encrypt_password(password)
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
    passwords[service] = encrypted_password.decode()
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

# Function to get a password
def get_password(service):
    with open("passwords.json", "r") as file:
        passwords = json.load(file)
    encrypted_password = passwords.get(service)
    if encrypted_password:
        return decrypt_password(encrypted_password.encode())
    else:
        return None

# Initialize the passwords file
if not os.path.exists("passwords.json"):
    with open("passwords.json", "w") as file:
        json.dump({}, file)

# Function to generate a random password
def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Create the main application window
class PasswordManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Manager")
        self.geometry("400x350")

        # Show password variable
        self.show_password = tk.BooleanVar()

        # Service Label and Entry
        self.service_label = tk.Label(self, text="Service:")
        self.service_label.pack(pady=5)
        self.service_entry = tk.Entry(self)
        self.service_entry.pack(pady=5)

        # Password Label and Entry
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        # Show Password Button
        self.show_password_button = tk.Checkbutton(self, text="Show Password", variable=self.show_password, command=self.toggle_password)
        self.show_password_button.pack(pady=5)

        # Add Password Button
        self.add_button = tk.Button(self, text="Add Password", command=self.add_password)
        self.add_button.pack(pady=5)

        # Generate Password Button
        self.generate_button = tk.Button(self, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=5)

        # Get Password Button
        self.get_button = tk.Button(self, text="Get Password", command=self.get_password)
        self.get_button.pack(pady=5)

    def toggle_password(self):
        if self.show_password.get():
            self.password_entry.config(show="")
        else:
            self.password_entry.config(show="*")

    def add_password(self):
        service = self.service_entry.get()
        password = self.password_entry.get()
        if service and password:
            add_password(service, password)
            messagebox.showinfo("Success", "Password added successfully!")
            self.service_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter both service and password.")

    def generate_password(self):
        service = self.service_entry.get()
        if service:
            password = generate_random_password()
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
            add_password(service, password)
            messagebox.showinfo("Generated Password", f"Generated password for {service}: {password}")
        else:
            messagebox.showwarning("Input Error", "Please enter the service name.")

    def get_password(self):
        service = self.service_entry.get()
        if service:
            password = get_password(service)
            if password:
                self.password_entry.delete(0, tk.END)
                self.password_entry.insert(0, password)
                messagebox.showinfo("Password Retrieved", f"The password for {service} is {password}")
            else:
                messagebox.showwarning("Not Found", "Service not found.")
        else:
            messagebox.showwarning("Input Error", "Please enter the service name.")

# Run the application
if __name__ == "__main__":
    app = PasswordManagerApp()
    app.mainloop()
