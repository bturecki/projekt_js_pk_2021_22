import tkinter as tk
from tkcalendar import DateEntry

class DateSelectionView():
    def __init__(self, master):
        self.__window = master
        self.__window.wm_iconbitmap('Resources/IkonaParkomat.ico')
        self.__window.cal = DateEntry(self.__window,selectmode='day', background='darkblue', foreground='white', borderwidth=2)
        self.__window.cal.grid(row=0, column=0)
        self.__window.entryGodzina = tk.Entry(self.__window, width = 2)
        self.__window.entryGodzina.grid(row=0, column=1)
        self.__window.lbl = tk.Label(self.__window, text=":", width=1).grid(row=0, column=2)
        self.__window.entryMinuta = tk.Entry(self.__window, width = 2)
        self.__window.entryMinuta.grid(row=0, column=3)
        self.__window.lbl2 = tk.Label(self.__window, text=":", width=0).grid(row=0, column=4)
        self.__window.entrySekunda = tk.Entry(self.__window, width = 2)
        self.__window.entrySekunda.grid(row=0, column=5)
        self.__window.buttonOk = tk.Button(self.__window, text = "OK", width=2)
        self.__window.buttonOk.grid(row=0, column=6)
        self.__window.entryGodzina.delete(0, tk.END)
        self.__window.entryGodzina.insert(0,"00")
        self.__window.entryMinuta.delete(0, tk.END)
        self.__window.entryMinuta.insert(0,"00")
        self.__window.entrySekunda.delete(0, tk.END)
        self.__window.entrySekunda.insert(0,"00")     

    def BindButtonOk(self, f):
        self.__window.buttonOk.bind("<Button>", lambda event: f())

    def GetGodzina(self):
        return self.__window.entryGodzina.get()
        
    def GetMinuta(self):
        return self.__window.entryMinuta.get()
        
    def GetSekunda(self):
        return self.__window.entrySekunda.get()
        
    def GetData(self):
        return self.__window.cal.get_date()