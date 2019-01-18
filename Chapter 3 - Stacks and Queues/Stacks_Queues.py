# Stacks and Queues Class

# Stack Class
# Functions : 1) Pop()
#             2) Push()
#             3) Length()
#             4) Top()


class Stacks:
    def __init__(self):
        self.array = []

    def push(self, data):
        self.array.append(data)

    def top(self):
        return self.array[-1]

    def length(self):
        return len(self.array)

    def pop(self):
        # Generally pop returns the element that is popped and
        # modifies the stack without returning it.
        popped = self.array[-1]
        self.array = self.array[:-1]    # Removing last added element
        return popped

    def print_stack(self):
        print self.array[:]
        return


# Queue Class
# Functions : 1) Dequeue()
#             2) enqueue()
#             3) Length()
#             4) front_rear()


class Queues:
    def __init__(self):
        self.array = []

    def enqueue(self, data):
        # Add an element at the back
        self.array.append(data)
        return

    def dequeue(self):
        # Leaving the first added element
        dequeued = self.array[-1]
        self.array = self.array[1:]
        return dequeued

    def que_front_rear(self, argument):
        if argument == 'front':
            return self.array[0]
        if argument == 'rear':
            return self.array[-1]

    def length(self):
        return len(self.array)

    def print_queue(self):
        print self.array[:]
        return


# Helper Code:
# stacker = Stacks()
# print(stacker.length())
#
# stacker.push(2)
# stacker.push(4)
# stacker.print_stack()
# print(stacker.length())
# stacker.pop()
# stacker.print_stack()
# print(stacker.length())
#
# print 'Queue Begins'
#
# queuer = Queues()
# print(queuer.length())
# queuer.enqueue(2)
# queuer.enqueue(3)
# queuer.enqueue(4)
#
# queuer.print_queue()
# queuer.dequeue()
#
# print(queuer.que_front_rear('front'))

