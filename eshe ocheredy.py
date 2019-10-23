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
        if self.items.index(item) ==9:
            print ('Проходите на кассу, вас уже ждут')
        elif self.items.index(item) ==8:
            print('Вы второй в очерди, вас скоро пригласят')
        elif self.items.index(item) ==7:
            print('Вы третий в очерди')
        elif self.items.index(item) ==6:
            print('Вы четвертый в очереди')
        elif self.items.index(item) ==5:
            print('Вы в середине очерди, подождите немного')
        elif self.items.index(item) ==4:
            print('Вы в шестой')
        elif self.items.index(item) ==3:
            print('Вы седьмой')
        elif self.items.index(item) ==2:
            print('Вы восьмой')
        elif self.items.index(item) ==1:
            print('Вы девятый')
        elif self.items.index(item) ==0:
            print("Вы десятый")


    def info_of_que(self):
        print(self.items)

        


cards = Cards_que()

print('В очереди сейчас '+ str(cards.size())+ ' человек')

for i in range(1,11):
    cards.enqueque('p-0{}'.format(i))

print('В очереди сейчас '+ str(cards.size())+ ' человек')

print(cards.info_of_que())

print(cards.info_of_item('p-09'))

print('########################')


for i in range(11,16):
    cards.enqueque('p-0{}'.format(i))

print(cards.info_of_que())

if cards.size() ==15:
    cards.dequeque()


print(cards.info_of_que())

