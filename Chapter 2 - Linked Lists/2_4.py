# coding=utf-8
# Problem 2.4
# You have two numbers represented by a linked list, where each node contains
# a single digit. The digits are stored in reverse order, such that the
# 1’s digit is at the head of the list.
#
# Write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
# Output: 8 -> 0 -> 8

from linked_list import LinkedList

# Algorithm One:
# Step 1: Read the numbers
# Step 2: Make a string from them
# Step 3: Convert them into integers.
# Step 4: Add Them
# Step 5: Store the sum in Linked List format


# Algorithm One:
def add_numbers(head1, head2):
    head_1 = head1
    head_2 = head2

    str1 = ""
    str2 = ""

    # Reading First Number
    while head_1 is not None:
        str1 = str1 + str(head_1.data)
        head_1 = head_1.next

    print str1[::-1]

    # Reading Second Number
    while head_2 is not None:
        str2 = str2 + str(head_2.data)
        head_2 = head_2.next

    print str2[::-1]

    sum_numbers = int(str1[::-1]) + int(str2[::-1])

    print sum_numbers
    return sum_numbers


# Helper Code:

ll_object = LinkedList()
ll_object.append(3)
ll_object.append(1)
ll_object.append(5)

l2_object = LinkedList()
l2_object.append(5)
l2_object.append(9)
l2_object.append(2)

add_numbers(ll_object.head, l2_object.head)
