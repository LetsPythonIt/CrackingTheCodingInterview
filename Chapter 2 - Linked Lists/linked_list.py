# Linked List Implementation in Python
# Reference: GeeksForGeeks.org


# Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Linked List Implementation
class LinkedList:
    # Constructor: Forms a Linked List Object
    def __init__(self):
        self.head = None

    # Prints out your linked list
    def print_linked_list(self):
        temp = self.head
        if temp is None:
            print 'Nothing to Print; Linked List is empty'
        while temp is not None:
            print '*'
            print 'Data: ', temp.data
            print 'Current Address: ', temp
            temp = temp.next
            print 'Next Address: ', temp

    # Adding the element at end of the node
    def append(self, data):
        new_node = Node(data)

        # If the linked list is empty, then make the new node as the head
        if self.head is None:
            self.head = new_node
            return

        last = self.head

        # If linked list is not empty, go till the last element
        while last.next is not None:  # When this condition is false, the last points to End(Null)
            last = last.next
        last.next = new_node
        return

    # Adding the element in the front of the linked_list
    def push(self, data):
        # It should be relatively easy than appending function
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        return

    # Adding the element after a given index
    def add_after(self, index, data):
        # Assuming that index exists

        # Adding the node
        new_node = Node(data)

        # Setting the correct index
        count = 0
        temp = self.head
        while count != index:
            temp = temp.next
            count += 1

        new_node.next = temp.next
        temp.next = new_node
        return


# Helper Code
if __name__ == '__main__':
    # MANUAL
    # Start with an empty list
    linked_list = LinkedList()

    # Manual Insertion of Data
    linked_list.head = Node(42)
    second = Node('is the answer')
    third = Node('to every question')

    # Manual Insertion of Pointers
    linked_list.head.next = second
    second.next = third
    # linked_list.print_linked_list()

    # USING FUNCTION
    # Start with an empty list
    linked_list_2 = LinkedList()

    # Insertion using push function
    linked_list_2.append('Thakur')
    linked_list_2.append('loves')
    linked_list_2.append('Python.')

    # printing the linked lists
    # linked_list.print_linked_list()
    # linked_list_2.print_linked_list()

    # Adding element in front
    linked_list_2.push('Sarvesh')
    linked_list_2.add_after(2, 'What?')
    linked_list_2.add_after(3, 'Answer!')
    linked_list_2.print_linked_list()
