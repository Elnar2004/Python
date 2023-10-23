from tkinter import*
from tkinter.ttk import Progressbar
from tkinter import ttk
window=Tk()
window.title("Добро пожаловать в приложение")
window.geometry('400x250')
style=ttk.Style()
style.theme_use('default')
bar=Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
bar['value']=70
bar.grid(column=0, row=0)
window.mainloop()