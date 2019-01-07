# -*- coding: cp1252 -*- // What is this?
# Problem 1.5
# Write a method to replace all spaces in a string with ‘%20’.

# I doubt if any interviewer would give this question to be solved in python


# Pythonic Way
def replace(string):
    modified_string = string.replace(" ", "%20")
    print modified_string
    return modified_string


replace("Afzal is Salman's big fan")



# Non-Pythonic Way
def replace_np(string):

    to_find = " "
    indices = [i for i, a in enumerate(string) if a == to_find]

    count = 0
    for ind in indices:
        buf_str = string[:ind + count] + "%20" + string[ind + count + 1:]
        count += 2
        string = buf_str

    print buf_str
    return indices

replace_np("Afzal is Salman's big fan")
