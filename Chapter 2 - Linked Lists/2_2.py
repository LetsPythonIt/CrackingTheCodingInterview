from linked_list import LinkedList

# Problem 2.2
# Implement an algorithm to find the nth to last element of a singly linked list.

# Algorithm:
# Step 1: find the length of the linked list
# Step 2: Print out the element at (length - n)th index.

# Solution:
# Step 1::: Finding Length


def find_length(head):
    temp = head
    length = 1  # Because for the last element, length variable won't update as while loops collapse.

    while temp.next is not None:
        length += 1
        temp = temp.next
    return length
def find_nth_to_last(head, n):
    temp = head
    index = 0
    length = find_length(head)
    while index != length - n:
        temp = temp.next
        index += 1
    # temp = temp.next
    return temp.data


# Helper Code
ll_object = LinkedList()
ll_object.append(1)
ll_object.append(11)
ll_object.append(111)
ll_object.append(1111)
ll_object.append(11111)

print (find_length(ll_object.head))
print (find_nth_to_last(ll_object.head, 4))
