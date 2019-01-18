# Problem 3.2
# How would you design a stack which, in addition to push and pop,
# also has a function min which returns the minimum element?
# Push, pop and min should all operate in O(1) time.


class Stacks:
    def __init__(self):
        self.array = []
        self.minimum = 999999999999999   # Crude

    # BigO(1)
    def push(self, data):
        if data < self.minimum:
            self.minimum = data
        self.array.append(data)

    # BigO(N)
    def pop(self):
        # Generally pop returns the element that is popped and
        # modifies the stack without returning it.
        popped = self.array[-1]
        self.array = self.array[:-1]    # Removing last added element # BigO(n)
        return popped

    # BigO(1)
    def pop_o_1(self):
        popped = self.array[-1]
        del self.array[-1]
        return popped

    # BigO(N)
    def min_in_stack(self):
        minimum = min(self.array)   # BigO(n)
        return minimum

    # BigO(1)
    def min_in_stack_o_1(self):
        return self.minimum

    def print_stack(self):
        print self.array[:]
        return

    def top(self):
        return self.array[-1]

    def length(self):
        return len(self.array)


# Helper Code:
stacker = Stacks()
stacker.push(2)
stacker.push(4)
stacker.push(24)
stacker.push(49)
stacker.push(2)
stacker.push(4)
stacker.push(2)
stacker.push(-4)
stacker.push(-4)

stacker.print_stack()

print(stacker.min_in_stack())
print(stacker.min_in_stack_o_1())
