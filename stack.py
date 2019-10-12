class Stack:

    
    def __init__(self):
        self.items =[]
       
       
    def is_empty(self):
        return self.items == []


    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()


    def peek(self):
        last = len(self.items) - 1 #показываем последний элемент массива Т.Е. длина - 1
        return self.items[last]

    def size(self):
        return len(self.items)


bank = input('сколько огурцов ')
Stac = Stack()

for i in range(0, int(bank)):
    Stac.push(i)

print(Stac.size())
