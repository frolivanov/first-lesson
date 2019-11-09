from tkinter import *
root=Tk()
root.title('Книжиенция попытка 2')
root.geometry('600x600')


numbers=Listbox(root, width=40, height=50, selectmode=SINGLE)


def info_from_entrys():
    a=pole_name.get()
    b=pole_surname.get()
    c=pole_number.get()
    info_for_list=a+' '+c+' - '+b
    numbers.insert(0,info_for_list)
    


add_button =Button(root, text='Добавить контакт',background='green',command=info_from_entrys)
del_button =Button(root, text='Удалить контакт', background='red')
edit_button =Button(root, text='Изменить контакт', background='orange')


pole_name =Entry(width=20)
pole_surname =Entry(width=20)
pole_number =Entry(width=20)




label_name =Label(text='Введите имя')
label_surname =Label(text='Введите фамилию ')
label_number =Label(text='Введите номер')

label_name.grid(row=0, column=0)
label_surname.grid(row=1, column=0)
label_number.grid(row=2,column=0)

pole_name.grid(row=0,column=1)
pole_number.grid(row=1, column=1)
pole_surname.grid(row=2,column=1)

numbers.grid(row=10,column=0,)

add_button.grid(row=3,column=1,pady=18)
del_button.grid(row=9, column=1)
edit_button.grid(row=9,column=0)

root.mainloop()