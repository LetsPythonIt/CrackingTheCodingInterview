# Problem 1.4
# Write a method to decide if two strings are anagrams or not.


def anagram_or_not(string_1, string_2):

    count = 0
    for character in string_1:
        if character not in string_2:
            value_1 = False
        else:
            if string_2.count(character) != string_1.count(character):
                value_1 = False
            else:
                value_1 = True

    for character in string_2:
        if character not in string_2:
            value_2 = False
        else:
            if string_2.count(character) != string_1.count(character):
                value_2 = False
            else:
                value_2 = True

    if (value_1 and value_2) == True:
        print 'Yes they are anagrams'
    else:
        print 'No they are not anagrams'


    
# Testcases:
string_1 = 'silent'
string_2 = 'listen'

anagram_or_not(string_1, string_2)

string_1 = 'silents'
string_2 = 'listen'

anagram_or_not(string_1, string_2)
