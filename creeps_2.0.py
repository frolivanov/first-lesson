class Creep():                                           #Создаем родительский класс, от которого будем наследоваться 
    
    def __init__(self, hp, walk, weapon):
        self.hp = hp
        self.walk = walk
        self.weapon = weapon

    def display_info(self):
        print(self.hp, self.walk, self.weapon)

Melee =Creep('500', '270', 'sword')                     #При создании объекта мы присваем переменной значение класса


class Range(Creep):                                     #Наследуемся от класса в скобках указываем от какого

    def __init__(self, hp, walk, weapon, mana):         #Сперва переписывваем старые конструкторы + добавляем новые
        Creep.__init__(self, hp, walk, weapon)          #Теперь переписываем только старые конструкторы с названием класса, в которым они были созданы
        self.mana = mana



    def freeze(self):
        print('Вы замороженны')



    def info(self):
        print(self.walk, self.hp, self.weapon, self.mana)


fff = Range('100 ', '270 ', 'magic stick ','100 ')

Melee.display_info()
fff.info()
fff.freeze()


