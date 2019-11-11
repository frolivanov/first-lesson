from tkinter import *
import csv
root=Tk()
root.title('Книжиенция попытка 2')
root.geometry('600x600')


numbers=Listbox(root, width=40, height=50, selectmode=SINGLE)
filename='0000.csv'


def change_contact():
    a=pole_name.get()
    b=pole_surname.get()
    c=pole_number.get()

    index=numbers.curselection()[0]
    
    if a=="" or b=="" or c=="":
        change=label_no_text.config(text='Все поля должны быть заполнены!',fg='red')

    else:
        numbers.delete(index)
        new_info= a +' '+c +' - '+b
        numbers.insert(index,new_info)

    pole_name.delete(0,len(a))
    pole_surname.delete(0,len(b))
    pole_number.delete(0,len(c))



def delete_contact():
    index=numbers.curselection()[0]
    numbers.delete(index)


def add_contact():
    a=pole_name.get()
    b=pole_surname.get()
    c=pole_number.get()
    if a=="" or b=="" or c=="":
        change=label_no_text.config(text='Все поля должны быть заполнены!',fg='red')

    else:
        info_for_list=a+" "+c+" - "+b
        numbers.insert(0,info_for_list)
        
        listforcsv = []
        listforcsv.insert(0,info_for_list)
        
        with open(filename, "a",newline="") as file:
            writer = csv.writer(file)
            writer.writerow(listforcsv)



    pole_name.delete(0,len(a))
    pole_surname.delete(0,len(b))
    pole_number.delete(0,len(c))



add_button =Button(root, text='Добавить контакт',background='green',command=add_contact)
del_button =Button(root, text='Удалить контакт', background='red', command=delete_contact)
edit_button =Button(root, text='Изменить контакт', background='orange', command=change_contact)



pole_name =Entry(width=20)
pole_surname =Entry(width=20)
pole_number =Entry(width=20)


label_no_text =Label()
label_name =Label(text='Введите имя')
label_surname =Label(text='Введите фамилию ')
label_number =Label(text='Введите номер')


label_name.grid(row=0, column=0)
label_surname.grid(row=1, column=0)
label_number.grid(row=2,column=0)
label_no_text.grid(row=1, column=3)


pole_name.grid(row=0,column=1)
pole_number.grid(row=1, column=1)
pole_surname.grid(row=2,column=1)


numbers.grid(row=10,column=0,)


add_button.grid(row=3,column=1,pady=18)
del_button.grid(row=9, column=1)
edit_button.grid(row=9,column=0)


root.mainloop()