class Stack:
    """
    Stack Data Structure
    """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __str__(self):
        return str(self.stack)


def main():
    myStack = Stack()
    myStack.push("A")
    myStack.push("B")
    myStack.push("C")
    myStack.push("D")
    print(myStack.peek())


if __name__ == "__main__":
    main()
