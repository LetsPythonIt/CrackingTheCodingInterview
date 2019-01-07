# -*- coding: cp1252 -*- # No clue why this came up :/
# Problem 1.2

# Write code to reverse a C-Style String.
#(C-String means that “abcd” is represented as five characters, including the null character.)


def reverse_in_c(string):

    # Python Style of Reversing a string
    Reverse_String_Python = string[::-1] # This contains the Null Character in the beggining

    # Removing Null character from beginning and adding Null character at end
    Reverse_String_C = Reverse_String_Python[1:] + '\0'

    print Reverse_String_C

    return Reverse_String_C




C_String1 = 'Afzal weighs 100 Kilos\0'
C_String2 = 'aBcD\0'


reverse_in_c(C_String1)
reverse_in_c(C_String2)
