import random
class Ochered:
    def __init__(self):
        self.arr = []
        self.num = int(input("Напишите 1 чтобы взять талон по пенсии, 2 за карту,3 за (я забыл )"))
        self.en = ['A','B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','V','X','Y','Z']
        #self.num = int(input("Напишите 1 чтобы взять талон по пенсии, 2 за карту,3 за (я забыл )"))
        self.humans = int(input("Людей в очереди?"))
    def is_empty(self):
        return self.arr == []

    def new(self,item):
        self.arr.insert(0,item)

    def init_arr(self):
        for i in range(0,self.humans):            
            self.arr.insert(0,random.choice(self.en)+chr(random.randint(0,23)))
        return self.arr
    def new(self):
        self.arr.insert(0,random.choice(self.en)+chr(random.randint(0,342891)))
        self.arr.pop()
    #def check(self,item):
     #   print(self.arr[len(self.arr)-int(item)]," Ваше место в очереди -  ",len(self.arr)-int(item),"Ваш индекс - ",item)
    def nazvanie(self):
        return self.arr

    def delete(self,item):
        self.arr.pop(item)

@@ -17,25 +28,29 @@ def end(self):
    def size(self):
        return len(self.arr) 

class Wibor(Ochered):
# class Wibor(Ochered):

#     #def __init__(self):
#     #    Ochered.__init__(self)

#     def check(self):
#         if self.num == 1:
#             self.new(1)
#             print("Вы в очереди за пенсию под номером " , " " , self.end() )   
#         if self.num == 2:
#             print("Вы в очереди за картой под номером " , " " , self.end())
#             self.new(1)
#         if self.num == 3:
#            self.new(1)
#            print("Вы в очереди за (Я забыл) под номером " + " " + self.end())

    #def __init__(self):
    #    Ochered.__init__(self)

    def check(self):
        if self.num == 1:
            self.new(1)
            print("Вы в очереди за пенсию под номером " , " " , self.end() )   
        if self.num == 2:
            print("Вы в очереди за картой под номером " , " " , self.end())
            self.new(1)
        if self.num == 3:
           self.new(1)
           print("Вы в очереди за (Я забыл) под номером " + " " + self.end())
a= Ochered()
print(a.init_arr())
a.new()
print(a.nazvanie())


a = Wibor()
a.check()
    