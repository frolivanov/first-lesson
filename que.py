import random


class Cards_que():



    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueque(self,item):
        self.items.insert(0,item)

    def dequeque(self):
        return self.items.pop()


    def size(self):
        return len(self.items)

    def info_of_item(self, item):
        if item in self.items:
            print(self.items.index(item))


cards = Cards_que()


class Pensii_que():


    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueque(self,item):
        self.items.insert(0,item)

    def dequeque(self):
        return self.items.pop()


    def size(self):
        return len(self.items)

    
    def info_of_item(self, item):
        if item in self.items:
            print(self.items.index(item))



Pensia = Pensii_que()



class Vkladi_que():


    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueque(self,item):
        self.items.insert(0,item)

    def dequeque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def info_of_item(self, item):
        if item in self.items:
            print(self.items.index(item))

Vklads = Vkladi_que()


print(cards.is_empty())


print(Pensia.is_empty())


print(Vklads.is_empty())


print(cards.size())


# where = input('Вам куда?')

# kreditandcards = ['Завести карту', 'Взять кредит', 'перевыпустить карту']

# if where in kreditandcards:
#     Cards.enqueque('Ледяев Иван')
#     # item.enqueque('Владимр Жириновский')

#     print(Cards.info_of_item('Ледяев Иван'))

for i in range(0,10):                
    cards.enqueque('p-0{}'.format(random.randint(0,10)))


 print(Cards.size())


# Cards.enqueque('c-1')

# Cards.enqueque('c-2')
# Cards.enqueque('c-3')
# Cards.enqueque('c-4')
# Cards.enqueque('c-5')
# Cards.enqueque('c-5')

#print(cards.size())