# Source: https://www.youtube.com/watch?v=JlMyYuY1aXU

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # Any node added to the list will by-default point to None(Null).


class linked_list:

    def __init__(self):
        self.head = node()  # self.head is an object of class node.

    def append(self, data):
        new_node = node(data)  # Initializing node class with input data
        cur_pointer = self.head
        while cur_pointer.next is not None:  # Using is not for this statement is better than !=
            cur_pointer = cur_pointer.next
        cur_pointer.next = new_node

    def display(self):
        elements = []
        cur_pointer = self.head
        while cur_pointer.next is not None:
            cur_pointer = cur_pointer.next
            elements.append(cur_pointer.data)
        print elements

    def length(self):
        cur_pointer = self.head
        count = 0
        while cur_pointer.next is not None:
            count += 1
            cur_pointer = cur_pointer.next
        # print 'There are %d elements in the linked list.' % count
        return count

    def get(self, index):
        if index >= self.length():
            print 'Error: Index given does not exists'
            return None
        cur_pointer = self.head
        cur_index = 0

        while True:
            cur_pointer = cur_pointer.next
            if cur_index == index:
                print cur_pointer.data
                return cur_pointer.data
            cur_index += 1

    def erase(self,index):
        if index >= self.length():
            print 'Error: Index given does not exists'
            return

        cur_pointer = self.head
        cur_index = 0

        while True:
            last_pointer = cur_pointer
            cur_pointer = cur_pointer.next

            if cur_index == index:
                last_pointer.next = cur_pointer.next
                return
            cur_index += 1



# Test-Code.
my_list = linked_list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()
print(my_list.length())

my_list.erase(3)

my_list.display()
print(my_list.length())

my_list.get(0)
