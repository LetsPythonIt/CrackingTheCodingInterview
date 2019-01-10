# coding=utf-8
# Problem 1.8

# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using
# only one call to isSubstring (i.e., “waterbottle” is a rotation of “erbottlewat”)

# Implemented Book's Solution

def is_substring(string_1, string_2):
    if string_1 in string_2:
        return True
    else:
        return False


def is_rotation(string_1, string_2):
    if len(string_1) != len(string_2):
        return False
    else:
        string_1 = string_1 + string_1
        if string_2 in string_1:
            return True
        else:
            return False

print(is_rotation('erbottlewat', 'waterbottle'))
print(is_rotation('komodo', 'dokomo'))
print(is_rotation('dog','god')) # They are just anagrams!
