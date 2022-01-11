import tkinter as tk
from tkcalendar import DateEntry

class DateSelectorView():
    """
    Widok do zmiany aktuanlej daty i godziny
    """

    def __init__(self, master):
        self.__window = master
        self.__window.title("")
        self.__window.wm_iconbitmap('Resources/IkonaParkomat.ico')
        self.__window.__cal = DateEntry(self.__window,selectmode='day', background='darkblue', foreground='white', borderwidth=2)
        self.__window.__cal.grid(row=0, column=0)
        self.__window.__entryGodzina = tk.Entry(self.__window, width = 2)
        self.__window.__entryGodzina.grid(row=0, column=1)
        self.__window.__lbl = tk.Label(self.__window, text=":", width=1).grid(row=0, column=2)
        self.__window.__entryMinuta = tk.Entry(self.__window, width = 2)
        self.__window.__entryMinuta.grid(row=0, column=3)
        self.__window.__lbl2 = tk.Label(self.__window, text=":", width=0).grid(row=0, column=4)
        self.__window.__entrySekunda = tk.Entry(self.__window, width = 2)
        self.__window.__entrySekunda.grid(row=0, column=5)
        self.__window.__buttonOk = tk.Button(self.__window, text = "OK", width=2)
        self.__window.__buttonOk.grid(row=0, column=6)
        self.__window.__entryGodzina.delete(0, tk.END)
        self.__window.__entryGodzina.insert(0,"00")
        self.__window.__entryMinuta.delete(0, tk.END)
        self.__window.__entryMinuta.insert(0,"00")
        self.__window.__entrySekunda.delete(0, tk.END)
        self.__window.__entrySekunda.insert(0,"00")     

    def BindButtonOk(self, f):
        self.__window.__buttonOk.bind("<Button>", lambda event: f())

    def GetGodzina(self):
        return self.__window.__entryGodzina.get()
        
    def SetGodzina(self, m):
        self.__window.__entryGodzina.delete(0, tk.END)
        self.__window.__entryGodzina.insert(0,m)
        
    def GetMinuta(self):
        return self.__window.__entryMinuta.get()
        
    def SetMinuta(self, m):
        self.__window.__entryMinuta.delete(0, tk.END)
        self.__window.__entryMinuta.insert(0,m)

    def GetSekunda(self):
        return self.__window.__entrySekunda.get()

    def SetSekunda(self, m):
        self.__window.__entrySekunda.delete(0, tk.END)
        self.__window.__entrySekunda.insert(0,m)
        
    def GetData(self):
        return self.__window.__cal.get_date()