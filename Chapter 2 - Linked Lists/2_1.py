# Problem 2.1 Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?


from linked_list import LinkedList

ll_object = LinkedList()


# Algorithm
# Step 1: Finding the index which are having duplicates.
# Step 2: For every duplicate run loop and connect the previous node to node just after the next node.

# Step 1: Finding the Indexes which are having the duplicates
def find_duplicates(head):
    # I can make a more simplified version
    container = []
    temp = head

    while temp.next is not None:
        if temp.data in container:
            container.append('duplicate')
        else:
            container.append(temp.data)
        temp = temp.next
    # Last Element
    if temp.data in container:
        container.append('duplicate')
    else:
        container.append(temp.data)

    # Return duplicate element index
    index = 0
    indexes = []
    for element in container:
        if element == 'duplicate':
            indexes.append(index)
        index += 1

    # print '\n'
    # print indexes
    return indexes


def remove_duplicates(head):
    # Step 2: Connect the previous node to node just after the next node.
    indexes = find_duplicates(head)
    for x in range(len(indexes)):
        index = find_duplicates(head)
        ind = index[0]
        position = 0
        temp = head
        while position != ind-1:
            temp = temp.next
            position += 1
        culprit = temp.next
        after_culprit = culprit.next
        temp.next = after_culprit
        print '\n', after_culprit

    return


# Helper Code
ll_object.append(1)
ll_object.append(2)
ll_object.append(3)
ll_object.append(4)
ll_object.append(4)
ll_object.append(4)
ll_object.append(1)
ll_object.append(42)

print 'original'
ll_object.simple_print()
remove_duplicates(ll_object.head)
print '\n'
print 'modification'
ll_object.simple_print()
