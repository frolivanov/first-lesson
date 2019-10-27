from tkinter import *

root =Tk()
root.title('Телефонная книженция')
root.geometry('1280x720')

numbers=[]

def add_number(self):
    global numbers
    chisla=input('Введите номер телефона начиная с +7')
    self.numbers.insert(0,chisla)

def vivod():
   global numbers
   print(numbers)
    

add_button =Button(root, text='Добавить контакт',background='brown')
del_button =Button(root, text='Удалить контакт')
edit_button =Button(root, text='Изменить контакт')

add_button.grid(row=0, column=0, padx=100, pady=0)
del_button.grid(row=2, column=4, padx=75, pady=300)
edit_button.grid(row=2, column=5)

root.mainloop()