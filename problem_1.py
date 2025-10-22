# **Level 3 Questions**
# 1. Write a function to split a given string on hyphens (-) and display each substring on a new line.
# You must:
# - Solve it using an inbuilt function (split()).
# - Solve it without using any inbuilt split functions — by using loops and conditions.
# Given:
# sentence = "Emma-is-a-data-scientist"
# Expected Output:
# Emma
# is
# a
# data
# scientist
def split_string_inbuilt(sentence):
    substrings = sentence.split('-')
    for substring in substrings:
        print(substring)       
split_string_inbuilt("Emma-is-a-data-scientist")
       
       
        
def split_string_manual(sentence):
    current_substring = ""
    for char in sentence:
        if char == '-':
            print(current_substring)
            current_substring = ""
        else:
            current_substring += char
    print(current_substring)  # Print the last substring
split_string_manual("Emma-is-a-data-scientist")

 