import random
import string

print("----- PASSWORD GENERATOR -----")

# User input for password length
length = int(input("Enter desired password length: "))

# Characters to use in password
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_characters = letters + digits + symbols

# Generate password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Display password
print("Generated Password:", password)