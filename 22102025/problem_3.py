# 3. Write a Python program to count the number of consonants in a given string.
# Input:
# Hello World
# Output:
# Number of consonants: 7

def count_consonants(input_string):
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for char in input_string:
        if char in consonants:
            count += 1
    return count



x = count_consonants('Hello World')
print(x)




# 4.  Write a Python program to remove all spaces from a given string.
# Input:
# Python is awesome
# Output:
# Pythonisawesome
# 5. Write a Python program that asks the user to enter a password and checks if it is strong. A password is considered strong if:
# It has at least 8 characters and  atleast one special character (!@#$%^&*).
# Print whether the password is strong or not.
# Input:
# Password: my@password
# Output:
# Password is strong
# Input:
# Password: python123
# Output:
# Password is not strong