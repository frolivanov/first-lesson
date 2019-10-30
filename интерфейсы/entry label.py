from tkinter import *

root =Tk()
root.title('Тестовая программа')
root.geometry('1280x720')

def change_label():
    ent=pole1.get()
    labl=label_1.config(text=ent)

def change_label_1():
    ent=pole2.get()
    labl=l2.config(text=ent)


pole1 =Entry(width=25)
pole2 =Entry(width=25)

bt1=Button(command=change_label)
bt2=Button(command=change_label_1)
label_1=Label(text='Тут должно быть то, что введут в поле')
l2=Label(text='Тут должно быть то, что введут в поле')


pole1.grid(row=0,column=0)
pole2.grid(row=0, column=1)
bt1.grid(row=1, column=0)
bt2.grid(row=1, column=1)
label_1.grid(row=2,column=0)
l2.grid(row=2,column=1)



root.mainloop()