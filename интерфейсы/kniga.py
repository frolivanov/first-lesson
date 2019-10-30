from tkinter import *

root =Tk()
root.title('Телефонная книженция')
root.geometry('1280x720')

numbers=[]


def new_window():
    win =Toplevel(root)
    win.grab_set()
    win.focus_set()
    win.wait_window()
    win.title('Создание контакта')
    win.minsize(width=600, height=400)


add_button =Button(root, text='Добавить контакт',background='brown')
del_button =Button(root, text='Удалить контакт')
edit_button =Button(root, text='Изменить контакт')


name=Label(text='Имя')
surname=Label(text='Фамилия')
number=Label(text='Мобильный номер')
keyword=Label(text='Ключевое слово')


add_button.grid(row=0, column=0, padx=100, pady=0)
del_button.grid(row=4, column=4, padx=75, pady=30)
edit_button.grid(row=4, column=5)
name.grid(row=1, column=4)
surname.grid(row=1, column=5)
number.grid(row=2, column=4, pady=20)
keyword.grid(row=3,column=4)

add_button.bind('<Button-1>',new_window)

root.mainloop()