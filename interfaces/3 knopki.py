from tkinter import *
root =Tk()


but1 = Button(root, text='Кнопка1')
but2 = Button(root, text='Кнопка2')
but3 = Button(root, text='Кнопка3')

r = ['linux','python', 'Tk', 'Tkinter']
lis = Listbox(root, selectmode = SINGLE, height=4)
for i in r:
    lis.insert(END,i)

but1.grid(row=0, column =0, padx = 20)
but2.grid(row=1, column =1, padx = 20)
but3.grid(row=2, column =2, padx = 20)

root.title('3 knopki')
root.mainloop()