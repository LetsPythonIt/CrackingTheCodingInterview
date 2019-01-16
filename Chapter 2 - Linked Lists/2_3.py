# coding=utf-8
from linked_list import LinkedList

# Problem 2.3
# Implement an algorithm to delete a node in the middle of a single linked list,
# given only access to that node.
#
# EXAMPLE:
# Input: the node ‘c’ from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a->b->d->e


# Book's Algorithm: Copy data from next node to middle node and delete the next node.
def delete_middle(node_c):
    node_d = node_c.next
    data_in_d = node_d.data
    node_c.data = data_in_d
    node_c.next = node_d.next
    return


# Helper Code
ll_object = LinkedList()
ll_object.append(1)
ll_object.append(11)
ll_object.append(100)
ll_object.append(1111)
ll_object.append(11111)

temp = ll_object.head
first = temp.next
second = first.next

ll_object.print_linked_list()

ll_object.simple_print()
delete_middle(second)
print '\n'
ll_object.simple_print()
