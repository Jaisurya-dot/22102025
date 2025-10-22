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

def is_strong_password(password):
    special_characters = "!@#$%^&*"
    count = 0   
    for i in password:
        if i in special_characters:
            count+=1
    if len(password) >=8 and count >=1:
        print('Password is strong')
    else:
        print('Password is not strong')

is_strong_password('my@password')
is_strong_password('python123')