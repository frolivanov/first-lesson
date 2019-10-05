class Price():


    def __init__(self, name, QR, cena):
        self.__name = name
        self.__QR = QR
        self.__cena = cena


    def set_QR(self, QR):
        if QR in range(8,16):
            self.__QR = QR
        else:
            print('Недопустимый формат')


    def set_cena(self, cena):
        if cena in range(1,10000):
            self.__cena = cena
        else:
            print('Недопустимый формат')


    def set_name(self,name):
        if len(name)>15:
            print('Недопустимый формат')
        else:
            self.__name = name


    def get_name(self):
        return self.__name


    def get_cena(self):
        return self.__cena

    
    def get_QR(self):
        return self.__QR


    def display_info(self):
        print('Название ', self.__name, "Цена ", self.__cena, "Штрих-код ",self.__QR )


Cennik = Price('Печенье', '8800553535', '360')
Cennik_1 = Price('Печенfdsfefreferferferfdfsdfsdfsdье', '880055353555555555555', '100000000')
Cennik.display_info()
Cennik_1.display_info()
Cennik_1.set_cena(999999)
Cennik_1.display_info()





