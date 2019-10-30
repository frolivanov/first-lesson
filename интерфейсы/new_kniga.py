from tkinter import *
root=Tk()
root.title('Книжиенция попытка 2')


add_button =Button(root, text='Добавить контакт',background='green')
del_button =Button(root, text='Удалить контакт')
edit_button =Button(root, text='Изменить контакт')



pole_name =Entry(width=20)
pole_surname =Entry(width=20)
pole_number =Entry(width=20)


label_name =Label(text='Введите имя')
label_surname =Label(text='Введите фамилию ')
label_namber =Label(text='Введите номер')


grid.