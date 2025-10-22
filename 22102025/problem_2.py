# 2. Write a Python program to reverse a given string in two ways:
# - Using an inbuilt function or slicing
# - Without using any inbuilt functions/Slicing
# Given:
# str1 = "Python"
# Expected Output:
# nohtyP


def reverse_string_inbuilt(str1):
    reversed_str = str1[::-1]
    print(reversed_str)

def reverse_string_manual(str1):
    reversed_str = ""
    for char in str1:
        reversed_str = char + reversed_str
    print(reversed_str)

reverse_string_inbuilt('Python')
reverse_string_manual('Python')















 