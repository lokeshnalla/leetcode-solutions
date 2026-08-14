class MinStack:

    def __init__(self):
        # Normal stack
        self.stack = []

        # Stack that keeps track of minimum values
        self.minStack = []

    def push(self, val: int) -> None:

        # Add value to normal stack
        self.stack.append(val)

        # If minStack is empty, current value is the minimum
        if not self.minStack:
            self.minStack.append(val)

        # Otherwise, store the smaller of:
        # current value and previous minimum
        else:
            self.minStack.append(
                min(val, self.minStack[-1])
            )

    def pop(self) -> None:

        # Remove from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:

        # Return top of normal stack
        return self.stack[-1]

    def getMin(self) -> int:

        # Top of minStack is always the current minimum
        return self.minStack[-1]