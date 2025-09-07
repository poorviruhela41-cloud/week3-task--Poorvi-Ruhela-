import json
import os
import base64

DATA_FILE = "passwords.json"


# ---------- Helper Functions ----------
def encode_password(password):
    """Encode password using Base64"""
    return base64.b64encode(password.encode()).decode()


def decode_password(encoded_password):
    """Decode Base64 password"""
    return base64.b64decode(encoded_password.encode()).decode()


def load_data():
    """Load existing password data from JSON"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}


def save_data(data):
    """Save password data to JSON"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


# ---------- Core Functions ----------
def add_entry(website, username, password):
    data = load_data()
    encoded_pass = encode_password(password)
    data[website] = {"username": username, "password": encoded_pass}
    save_data(data)
    print(f"✅ Entry for '{website}' added successfully!")


def view_entries():
    data = load_data()
    if not data:
        print("⚠ No saved entries.")
    else:
        print("\n🔐 Stored Passwords:")
        for site, creds in data.items():
            decoded_pass = decode_password(creds["password"])
            print(f"- {site} | {creds['username']} | {decoded_pass}")


# ---------- Menu ----------
def main():
    while True:
        print("\n===== Simple Password Manager =====")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            site = input("Enter website: ")
            user = input("Enter username: ")
            pwd = input("Enter password: ")
            add_entry(site, user, pwd)

        elif choice == "2":
            view_entries()

        elif choice == "3":
            print("👋 Exiting Password Manager. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")


if __name__ == "__main__":
    main()