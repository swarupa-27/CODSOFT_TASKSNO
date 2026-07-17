import random
import string

print("===== Password Generator =====")

# Get password length from user
length = int(input("Enter the desired password length: "))

# Characters to use in password
characters = (
    string.ascii_letters +      # A-Z, a-z
    string.digits +             # 0-9
    string.punctuation          # Special characters
)

# Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Display password
print("\nGenerated Password:")
print(password)