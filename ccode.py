import random
import string

def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    """
    Generates a random password of the given length with the specified character types.
    
    Parameters:
    length (int): The length of the password to generate.
    uppercase (bool): Whether to include uppercase letters in the password.
    lowercase (bool): Whether to include lowercase letters in the password.
    digits (bool): Whether to include digits in the password.
    symbols (bool): Whether to include symbols in the password.
    
    Returns:
    str: The generated password.
    """
    # create a list of characters to use in the password
    characters = []
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation
    
    # generate the password using random.choices
    password = ''.join(random.choices(characters, k=length))
    
    return password

# prompt the user for the password length
length = int(input("Enter the length of the password: "))

# prompt the user for the character types to include
uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
digits = input("Include digits? (y/n): ").lower() == 'y'
symbols = input("Include symbols? (y/n): ").lower() == 'y'

# generate the password
password = generate_password(length, uppercase, lowercase, digits, symbols)

# print the password
print(f"Your random password is: {password}")
