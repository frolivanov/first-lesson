class Person():

    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname

    def info(self):
        print('Вас зовут'+ self.name + self.lastname)

Human = Person("Tom", "Gufovsky")
Human.info()