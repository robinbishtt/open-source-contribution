import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    uppercase = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    digits = string.digits  # 0123456789
    symbols = string.punctuation  # !@#$%^&*()_+-=[]{}|;:,.<>?

    # Combine all characters
    all_characters = lowercase + uppercase + digits + symbols

    # Ensure at least one character from each category
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the password characters
    random.shuffle(password)

    # Join the characters into a string
    return ''.join(password)

def main():
    print("Random Password Generator")
    try:
        length = int(input("Enter password length (minimum 8): "))
        if length < 8:
            print("Password length must be at least 8 characters!")
            return
        
        # Generate and display password
        password = generate_password(length)
        print(f"Generated Password: {password}")
        
        # Ask if user wants another password
        again = input("Generate another password? (yes/no): ").lower()
        if again == 'yes':
            main()
        else:
            print("Goodbye!")
            
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
