from tkinter import *

clicks = 0

def click_button():
    global clicks
    clicks +=1
    btn.config(text='Clicks {}'.format(clicks))

root = Tk()
root.title('GUI на Python')
root.geometry("400x400")