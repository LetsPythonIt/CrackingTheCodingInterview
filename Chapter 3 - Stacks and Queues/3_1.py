# Problem 3.1
# Use a single array to implement 3 stacks.


class ThreeStacks:
    def __init__(self, size):
        # Assumption: Size of each array is same
        self.size = size
        self.array = [None]*3*self.size

    def push(self, which_stack, element):
        # @which_stack: Adds the element in the corresponding stack
        if which_stack == 'first':
            starting_index = 0
            ending_index = self.size - 1
        if which_stack == 'second':
            starting_index = self.size
            ending_index = 2*self.size - 1
        if which_stack == 'third':
            starting_index = 2*self.size
            ending_index = 3*self.size - 1

        # Finding the correct index to add the element
        for index in range(starting_index, ending_index + 1):
            push_index = None
            if self.array[index] is None:
                push_index = index
                break

        if push_index is None:
            print 'No space left to push new element %d in %s Stack' % (element, which_stack)
        else:
            self.array[push_index] = element
        return

    def print_stack(self, which_stack):
        if which_stack == 'first':
            top = self.size - 1
            bottom = 0
        if which_stack == 'second':
            top = 2*self.size - 1
            bottom = self.size
        if which_stack == 'third':
            top = 3*self.size - 1
            bottom = 2*self.size
        if which_stack == 'all':
            top = 3*self.size - 1
            bottom = 0
        print self.array[bottom:top+1]

        return






# Helper Code
stacker = ThreeStacks(4)
stacker.push('first', 242)
stacker.push('first', 22)
stacker.push('first', 42)
stacker.push('first', 252)
stacker.push('first', 222)

stacker.push('second', 2)
stacker.push('second', 22)
stacker.push('second', 222)
stacker.push('second', 2222)
stacker.push('second', 22222)

stacker.push('third', 102)
stacker.push('third', 1002)
stacker.push('third', 10002)
stacker.push('third', 100002)
stacker.push('third', 1000002)
stacker.print_stack('first')
stacker.print_stack('second')
stacker.print_stack('third')
stacker.print_stack('all')
