class Cards_que():


    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueque(self):
        self.items.insert(0,item)

    def dequeque(self):
        return self.items.pop()


    def size(self):
        return len(self.items)


Cards = Cards_que()


class Pensii_que():


    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueque(self):
        self.items.insert(0,item)

    def dequeque(self):
        return self.items.pop()


    def size(self):
        return len(self.items)



Pensia = Pensii_que()



class Vkladi_que():


    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueque(self):
        self.items.insert(0,item)

    def dequeque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


Vklads = Vkladi_que()


print(Cards.is_empty())


print(Pensia.is_empty())


print(Vklads.is_empty)


where = input('Вам куда?')

kreditandcards = ['Завести карту', 'Взять кредит', 'перевыпустить карту']

if where in kreditandcards:
    item = Cards()
    print (item.size())
