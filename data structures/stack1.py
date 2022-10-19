class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)


stack1 = Stack()
for i in "позавчера":
    stack1.push(i)
string = ""
for i in range(len(stack1.items)):
    string += stack1.pop()
print(string)

stack2 = Stack()
list1 = [1, 2, 3, 4, 5]
list2 = []
for i in list1:
    stack2.push(i)
for i in range(len(stack2.items)):
    list2.append(stack2.pop())
print(list2)