# Day06_PasswordGenerator.py
# Generate a random secure password

import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""
    
    all_chars = letters + digits + special
    
    if not all_chars:
        raise ValueError("No characters available to generate password")
    
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


if __name__ == "__main__":
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    pwd = generate_password(length, use_digits, use_special)
    print(f"\n🔐 Generated Password: {pwd}")
