# Problem 2.2
# Implement an algorithm to find the nth to last element of a singly linked list.

from Python_Linked_List import *

my_linked_list = linked_list()


def get_nth_from_last(index):
    length = my_linked_list.length()
    element = my_linked_list.get(length - 1 - index)
    return element


# Forming Linked-List
my_linked_list.append(1)
my_linked_list.append(24635)
my_linked_list.append(332)
my_linked_list.append(43)
my_linked_list.append(34)
my_linked_list.append(10)
my_linked_list.append(24)
my_linked_list.append(33)
my_linked_list.append(4345)
my_linked_list.append(344)
my_linked_list.display()

print(get_nth_from_last(3))
