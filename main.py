import re
import secrets
import string


"""
Generate a random password with specified constraints.
Args:
    length (int): The length of the password. Default is 16.
    nums (int): Minimum number of numeric characters in the password. Default is 1.
    special_chars (int): Minimum number of special characters in the password. Default is 1.
    uppercase (int): Minimum number of uppercase letters in the password. Default is 1.
    lowercase (int): Minimum number of lowercase letters in the password. Default is 1.
Returns:
    str: The generated password that meets the specified constraints.
"""
def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

if __name__ == '__main__':
    new_password = generate_password()
    print('Generated password:', new_password)