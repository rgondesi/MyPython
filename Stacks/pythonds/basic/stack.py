class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        MaxSize = len(self.items)
        return self.items[MaxSize -1] if MaxSize != 0 else "Empty"

    def size(self):
        return len(self.items)


