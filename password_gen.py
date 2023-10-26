import random
import string

# Define the character sets for different security levels
easy_chars = string.ascii_letters 
moderate_chars = string.ascii_letters + string.digits
hard_chars = string.ascii_letters + string.digits + string.punctuation

# Set the password length
password_length = int(input("Enter the length of the password: "))

# Get the desired level of security from the user
difficulty = input("Choose a level of security: easy, moderate, or hard? ").lower()

# Function to generate a random password
def generate_password(password_length, char_set):
    return ''.join(random.choice(char_set) for _ in range(password_length))

# Check the difficulty level and select the corresponding character set
if difficulty == 'easy':
    random_password = generate_password(password_length, easy_chars)
elif difficulty == 'moderate':
    random_password = generate_password(password_length, moderate_chars)
elif difficulty == 'hard':
    random_password = generate_password(password_length, hard_chars)
else:
    print("Invalid security level. Please choose 'easy', 'moderate', or 'hard'.")

# Print the generated password
if random_password:
    print("Random Password:", random_password)
