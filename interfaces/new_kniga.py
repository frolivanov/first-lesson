from tkinter import *
import pandas as pd
from tkinter import filedialog as fd
root=Tk()
root.title('Книжиенция попытка 2')
root.geometry('800x600')

names = []
surnames = []
phones = []
mails = []

img = PhotoImage(file = 'C:/Users/Ученик/Desktop/ledyaev ivan/interfaces/a.png')

numbers=Listbox(root, width=40, height=40, selectmode=SINGLE)


def isert_photo():
    file_name = fd.askopenfilename()
    f = open(file_name)
    s = f.read()
    a = s
    f.close()

# def extract_Photo():
#     file_name = fd.asksavefilename(filetypes=(('JPEG files','.jpeg'),('PNG files','.png'),('GIF files', '.gif') ))
#     f


def check():
    print(names)
    print(surnames)
    print(phones)
    print(mails)

def okno():
    if numbers.curselection() == 0:
        change=label_no_text.config(text='выделите контанкт',fg='red')
    else:
        win = Toplevel(root, relief = SUNKEN)
        win.title('Информация о контакте')
        win.geometry ('320x125')
        win.resizable(False, False)
        win.grab_set()
        win.focus_set()

        index=numbers.curselection()[0]
   
        window_name = Label(win, text = 'Имя: ')
        window_surname = Label(win, text = 'Фамилия: ')
        window_number = Label(win, text = 'Номер: ')
        window_mail = Label(win, text = 'Почта: ')
        window_photo = Button(win, image = img, width = 60, height = 60)
        ent_name = Label (win, text = names[index])
        ent_surname = Label(win, text = surnames[index])
        ent_number = Label(win, text = phones[index])
        ent_mail = Label(win, text = mails[index])
        label_pusto = Label(win, text = ' ',width = 20)

        window_name.grid(row = 0, column = 0)
        window_surname.grid(row = 1, column = 0)
        window_number.grid(row = 2, column = 0)
        window_mail.grid(row=3, column =  0)
        ent_name.grid(row = 0, column = 1)
        ent_surname.grid(row = 1, column = 1)
        ent_number.grid(row = 2, column = 1)
        ent_mail.grid(row = 3, column = 1)
        label_pusto.grid(row =4, column = 1, columnspan=6,rowspan = 6)
        window_photo.grid(row= 1, column = 7)


    # ent_name.insert(0,names[index])
    # ent_surname.insert(0,surnames[index])
    # ent_number.insert(0,phones[index])
    # ent_mail.insert(0,mails[index])


def change_contact():
    a=pole_name.get()
    b=pole_surname.get()
    c=pole_number.get()
    d=pole_mail.get()
    index=numbers.curselection()[0]
    
    if a=="" or b=="" or c=="" or d=="":
        change=label_no_text.config(text='Все поля должны быть заполнены!',fg='red')

    else:
        numbers.delete(index)
        names.pop(index)
        surnames.pop(index)
        phones.pop(index)
        mails.pop(index)
        names.insert(index,a)
        surnames.insert(index,b)
        phones.insert(index,c)
        mails.insert(index,d)
        new_info= a +' '+c +' - '+b
        numbers.insert(index,new_info)


    pole_name.delete(0,len(a))
    pole_surname.delete(0,len(b))
    pole_number.delete(0,len(c))
    pole_mail.delete(0,len(d))


def delete_contact():
    index=numbers.curselection()[0]
    numbers.delete(index)
    names.pop(index)
    surnames.pop(index)
    phones.pop(index)
    mails.pop(index)


def add_contact():
    a=pole_name.get()
    b=pole_surname.get()
    c=pole_number.get()
    d=pole_mail.get()
    if a=="" or b=="" or c=="" or d=="":
        change=label_no_text.config(text='Все поля должны быть заполнены!',fg='red')

    else:
        info_for_list=a+" "+c+" - "+b
        numbers.insert(0,info_for_list)
        names.insert(0,a)
        surnames.insert(0,b)
        phones.insert(0,c)
        mails.insert(0,d)


    pole_name.delete(0,len(a))
    pole_surname.delete(0,len(b))
    pole_number.delete(0,len(c))
    pole_mail.delete(0,len(d))



add_button =Button(root, text='Добавить контакт',background='green',command=add_contact)
del_button =Button(root, text='Удалить контакт', background='red', command=delete_contact)
edit_button =Button(root, text='Изменить контакт', background='orange', command=change_contact)
show_info = Button(root, text = 'доп. информация',command = okno)

pole_name =Entry(width=20)
pole_surname =Entry(width=20)
pole_number =Entry(width=20)
pole_mail = Entry(width = 20)

label_no_text =Label()
label_name =Label(text='Введите имя')
label_surname =Label(text='Введите фамилию ')
label_number =Label(text='Введите номер')
label_mail = Label(text='Введите почту')


label_name.grid(row=0, column=0)
label_surname.grid(row=1, column=0)
label_number.grid(row=2,column=0)
label_no_text.grid(row=1, column=3)
label_mail.grid(row = 3, column = 0)

pole_name.grid(row=0,column=1)
pole_number.grid(row=1, column=1)
pole_surname.grid(row=2,column=1)
pole_mail.grid(row=3, column = 1)

numbers.grid(row=6,column=0,pady=20)

add_button.grid(row=3,column=2)
del_button.grid(row=3, column=3)
edit_button.grid(row=3,column=4)
show_info.grid(row = 4, column = 1)

root.mainloop()