# Problem 1.3

# Design an algorithm and write code to remove the duplicate characters in a string
# without using any additional buffer.

# NOTE: One or two additional variables are fine. An extra copy of the array is not.

# FOLLOW UP
# Write the test cases for this method.


def remove_duplicates(string):
    print 'Original String: %s'%string

    for character in string:
        buffer_string_1 = string[:]
        if string.count(character) == 1:
            continue# 'Jaisa chal raha hai waisa chalne dijiye'
        else:
            index = string.find(character,0) # Noting the first occurance of the character

            # Removing all occurance of the character
            buffer_string_1 = buffer_string_1.replace(character,"")

            # Because Python Strings are Immutable.
            # Adding the character at its unique index.
            string = buffer_string_1[:index] + character + buffer_string_1[index:]

    print 'Modified String: %s'%string

    return string


# Testcases
remove_duplicates('aaa')
remove_duplicates('abcdabcdefghefgh')
remove_duplicates('aabwfrbccddabcd')
remove_duplicates('afzalam')
