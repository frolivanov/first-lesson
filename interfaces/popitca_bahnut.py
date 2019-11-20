from tkinter import *
import tkinter.messagebox as mb
import pandas as pd
root=Tk()
root.title('Книженция попытка 2')
root.geometry('800x600')


all_info = pd.DataFrame ({

    'names' : [],
    'surnames' : [],
    'phones' : [],
    'mails' : []

})

numbers=Listbox(root, width=40, height=40, selectmode=SINGLE)

def okno():
    if len(str(numbers.curselection()[0])) == 0:
        # label_no_text.config(text='РІС‹РґРµР»РёС‚Рµ РєРѕРЅС‚Р°РЅРєС‚',fg='red')
        mb.showerror('Ошибочка', 'Выберите контакт, чтобы узнать подробную информацию')
    else:
        win = Toplevel(root, relief = SUNKEN)
        win.title('Информация о контакте')
        win.geometry ('320x100')
        win.resizable(False, False)
        win.grab_set()
        win.focus_set()

        index=numbers.curselection()[0]
   
        window_name = Label(win, text = ' Имя: ')
        window_surname = Label(win, text = 'Фамилия: ')
        window_number = Label(win, text = 'Номер: ')
        window_mail = Label(win, text = 'Почта: ')
        window_photo = Label(win, text = 'Ы')
        ent_name = Label (win, text = all_info.names[index])
        ent_surname = Label(win, text = all_info.surnames[index])
        ent_number = Label(win, text = all_info.phones[index])
        ent_mail = Label(win, text = all_info.mails[index])

        window_name.grid(row = 0, column = 0)
        window_surname.grid(row = 1, column = 0)
        window_number.grid(row = 2, column = 0)
        window_mail.grid(row=3, column =  0)
        ent_name.grid(row = 0, column = 1)
        ent_surname.grid(row = 1, column = 1)
        ent_number.grid(row = 2, column = 1)
        ent_mail.grid(row = 3, column = 1)
        label_no_text.config(text = ' ')
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
    answer = mb.askyesno('Вопрсик', 'Вы уверенны, что хотите изменить контакт? Прошлые данные исчезнуть безвозврантно')
    if answer ==True:
        if a=="" or b=="" or c=="" or d=="":
            # label_no_text.config(text='Все поля должны быть заполены',fg='red')
            mb.showerror('Ошибочка вышла', 'Все поля должны быть заполнены')
        else:
            numbers.delete(index)
            all_info.names.pop(index)
            all_info.surnames.pop(index)
            all_info.phones.pop(index)
            all_info.mails.pop(index)
            all_info.names.insert(index,a)
            all_info.surnames.insert(index,b)
            all_info.phones.insert(index,c)
            all_info.mails.insert(index,d)
            new_info= a +' '+c +' - '+b
            numbers.insert(index,new_info)
            label_no_text.config(text = ' ')

    pole_name.delete(0,len(a))
    pole_surname.delete(0,len(b))
    pole_number.delete(0,len(c))
    pole_mail.delete(0,len(d))


def delete_contact():
    answer = mb.askyesno('Вопросик', 'Вы уверенны, что хотите удалить контатк безвозвратно?')
    if answer == True:
        index=numbers.curselection()[0]
        numbers.delete(index)
        all_info.names.pop(index)
        all_info.surnames.pop(index)
        all_info.phones.pop(index)
        all_info.mails.pop(index)


def add_contact():
    a=pole_name.get()
    b=pole_surname.get()
    c=pole_number.get()
    d=pole_mail.get()
    if a=="" or b=="" or c=="" or d=="":
        # label_no_text.config(text='Р’СЃРµ РїРѕР»СЏ РґРѕР»Р¶РЅС‹ Р±С‹С‚СЊ Р·Р°РїРѕР»РЅРµРЅС‹!',fg='red')
        mb.showerror('Ошибочка вышла', 'Все поля должны быть заполнены')
    else:
        info_for_list=a+" "+c+" - "+b
        numbers.insert(0,info_for_list)
        all_info.names.insert(0,a)
        all_info.surnames.insert(0,b)
        all_info.phones.insert(0,c)
        all_info.mails.insert(0,d)
        label_no_text.config(text = ' ')


    pole_name.delete(0,len(a))
    pole_surname.delete(0,len(b))
    pole_number.delete(0,len(c))
    pole_mail.delete(0,len(d))



add_button =Button(root, text='Добавить контакт‚',background='green',command=add_contact)
del_button =Button(root, text='Удалить контакт‚', background='red', command=delete_contact)
edit_button =Button(root, text='Изменить контакт', background='orange', command=change_contact)
show_info = Button(root, text = 'Показать информацию',command = okno)

pole_name =Entry(width=20)
pole_surname =Entry(width=20)
pole_number =Entry(width=20)
pole_mail = Entry(width = 20)

label_no_text =Label()
label_name =Label(text='Имя')
label_surname =Label(text='Фамилия')
label_number =Label(text='Номер телефона')
label_mail = Label(text='Эл. почта')


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


def check():
    print(all_info.head())
test_button = Button(text = 'test', command = check)
test_button.grid(row=10, column = 10)

root.mainloop()
#tkinter.messagebox