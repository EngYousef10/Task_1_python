import random
import string

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters")
    
    # Define character sets
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure at least one character from each category
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest with random characters from all categories
    all_chars = uppercase + lowercase + digits + special_chars
    password.extend(random.choice(all_chars) for _ in range(length - 4))
    
    # Shuffle the password
    random.shuffle(password)
    
    return ''.join(password)

def password_generator():
    try:
        length = int(input("Enter the desired password length (minimum 8): "))
        if length < 8:
            print("Password length set to minimum 8 characters")
            length = 8
        
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
    except ValueError:
        print("Please enter a valid number")

# Run the password generator
password_generator()