import random
import string

def generate_password(length):
    """Generate a random password of the specified length."""
    if length < 8:
        print("Password length should be at least 8 characters for better security.")
        return None

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    while True:
        # Prompt user for password length
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 1:
                print("Length must be a positive integer.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        # Generate and display the password
        password = generate_password(length)
        if password:
            print(f"Generated Password: {password}")
            break

if __name__ == "__main__":
    main()
