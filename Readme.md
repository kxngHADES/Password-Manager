# Password Manager

This Password Manager application is a simple tool to securely store, retrieve, and generate passwords for different services. It utilizes encryption to keep your passwords safe.

## Features

- **Add Password:** Save encrypted passwords for various services.
- **Get Password:** Retrieve and decrypt passwords for a specified service.
- **Generate Password:** Automatically create strong random passwords.
- **Show/Hide Password:** Toggle the visibility of the password input.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `cryptography` library

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/kxngHADES/Password-Manager.git
   cd password-manager
   ```

2. **Install the required package:**

   You can install the `cryptography` library using pip:

   ```bash
   pip install cryptography
   ```

## Usage

1. **Run the application:**

   Execute the script using Python:

   ```bash
   python password_manager.py
   ```

2. **Main Features:**

   - **Add a Password:**
     - Enter the service name and password, then click "Add Password" to save it.

   - **Generate a Password:**
     - Enter the service name and click "Generate Password" to create and save a new password automatically.

   - **Get a Password:**
     - Enter the service name and click "Get Password" to retrieve the stored password.

3. **Show/Hide Password:**
   - Use the "Show Password" checkbox to toggle password visibility in the password entry field.

## Security

- **Encryption:** Passwords are encrypted using the Fernet symmetric encryption from the `cryptography` library.
- **Key Management:** A unique key is generated and stored in `key.key` to encrypt and decrypt passwords. Ensure this file is kept safe and secure.
- **Password Storage:** Passwords are stored in an encrypted form in the `passwords.json` file.

## File Structure

- `password_manager.py`: Main application script.
- `key.key`: Encryption key file.
- `passwords.json`: File storing encrypted passwords.

## Notes

- Ensure that the `key.key` file is not shared or lost, as it is necessary for decrypting your passwords.
- It is recommended to back up both `key.key` and `passwords.json` to avoid data loss.

## License

This project is open source and available under the MIT License.
