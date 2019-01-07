# Problem 1.1

# Implement an algorithm to determine if a string has all unique characters
# What if you can not use additional data structures?


def check_unique(string):
    char_array = [] # Actually this is a list;
    count = 0
    
    for character in string:
        # Is the character already in that array
        if character in char_array:
            count += 1
            print 'False'
            return False
        else:
            char_array.append(character)

    if count == 0:
        print 'True'
    
    return True

def check_unique_without_DS(string):

    count = 0
    
    for element in string:
        if string.count(element) > 1:
            count += 1
            print 'False'
            return False
        else:
            continue
    if count == 0: print 'True'

    return True

# Testcases
string1 = 'Afzal is a very very fat friend of mine'
string2 = 'Afzal_Unique'

check_unique(string1)
check_unique(string2)

check_unique_without_DS(string1)
check_unique_without_DS(string2)
