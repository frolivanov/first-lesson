

class Hero():

    
    def __init__(self, mid, bot, top, damage, gold, move, bagpack, attack):
        self.mid = True
        self.bot = False
        self.top = False
        self.move = move
        self.gold = gold
        self.attack = 64
        self.bagpack = ["Null talisman", "Hand of midas", "Ring of Basilis", "Aghanim scepter"]
    def stat(self):
        if self.mid == True:
            print("Тебе следует идти на мид")
        elif self.bot == True:
            print("Иди фармить, на нижнюю линию")
        else:
            print("Ваш герой офллейнер, вам нужно страдать")


Hero.stat




