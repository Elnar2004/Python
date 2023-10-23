from tkinter import*
window=Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')
spin= Spinbox(window, from_=0, to=100, width=5)
spin.grid(column=0, row=0)
window.mainloop()