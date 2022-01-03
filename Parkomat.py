import tkinter as tk
from tkinter import messagebox
import time
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from dateutil.rrule import *  
from Models.Pieniadze import *
import re
import math

from Models.Pieniadze import *

# GUI
class View():

    def __init__(self, master):
        self.mainWindow = master
        self.mainWindow.title("Parkomat")
        self.mainWindow.geometry("301x380")
        self.mainWindow.wm_iconbitmap('IkonaParkomat.ico')
        self.mainWindow.eval('tk::PlaceWindow . center')
        #Pole tekstowe na numer rejestracyjny pojazdu
        self.mainWindow.labelNumerRejestracyjny = tk.Label(self.mainWindow, text="Numer rejestracyjny: ", width=20).grid(row=0, column=0)
        self.mainWindow.entryNumerRejestracyjny = tk.Entry(self.mainWindow, width=20)
        self.mainWindow.entryNumerRejestracyjny.grid(row=0, column=1)
        #Aktualna data
        self.mainWindow.labelAktualnaDataLbl = tk.Label(self.mainWindow, text="Aktualna data: ", width=20).grid(row=1, column=0)
        self.mainWindow.labelAktualnaData = tk.Label(self.mainWindow, width=20)
        self.mainWindow.labelAktualnaData.grid(row=1, column=1)

        #Suma wrzuconych pieniędzy
        self.mainWindow.labelAktualnieWrzucona = tk.Label(self.mainWindow, text="Aktualnie wrzucona suma: ", width=20).grid(row=2, column=0)
        self.mainWindow.labelWrzucono = tk.Label(self.mainWindow, width=20)
        self.mainWindow.labelWrzucono.grid(row=2, column=1)

        #Data wyjazdu z parkingu
        self.mainWindow.labelDataWyjazdu = tk.Label(self.mainWindow, text="Data wyjazdu z parkingu : ", width=20).grid(row=3, column=0)
        self.mainWindow.labelDataWyjazduZParkingu = tk.Label(self.mainWindow, width=20)
        self.mainWindow.labelDataWyjazduZParkingu.grid(row=3, column=1)
        self.mainWindow.labelDataWyjazduZParkingu.config(text = "---------------------")

        #Przyciski z pieniędzmi
        self.mainWindow.empty1 = tk.Label(self.mainWindow, text=" ").grid(row=4)
        self.mainWindow.button1gr = tk.Button(self.mainWindow, text = "1gr", width=20)
        self.mainWindow.button1gr.grid(row=5, column=0)
        self.mainWindow.button2gr = tk.Button(self.mainWindow, text = "2gr", width=20)
        self.mainWindow.button2gr.grid(row=6, column=0)
        self.mainWindow.button5gr = tk.Button(self.mainWindow, text = "5gr", width=20)
        self.mainWindow.button5gr.grid(row=7, column=0)
        self.mainWindow.button10gr = tk.Button(self.mainWindow, text = "10gr", width=20)
        self.mainWindow.button10gr.grid(row=8, column=0)
        self.mainWindow.button20gr = tk.Button(self.mainWindow, text = "20gr", width=20)
        self.mainWindow.button20gr.grid(row=9, column=0)
        self.mainWindow.button50gr = tk.Button(self.mainWindow, text = "50gr", width=20)
        self.mainWindow.button50gr.grid(row=10, column=0)
        self.mainWindow.button1zl = tk.Button(self.mainWindow, text = "1zł", width=20)
        self.mainWindow.button1zl.grid(row=5, column=1)
        self.mainWindow.button2zl = tk.Button(self.mainWindow, text = "2zł", width=20)
        self.mainWindow.button2zl.grid(row=6, column=1)
        self.mainWindow.button5zl = tk.Button(self.mainWindow, text = "5zł", width=20)
        self.mainWindow.button5zl.grid(row=7, column=1)
        self.mainWindow.button10zl = tk.Button(self.mainWindow, text = "10zł", width=20)
        self.mainWindow.button10zl.grid(row=8, column=1)
        self.mainWindow.button20zl = tk.Button(self.mainWindow, text = "20zł", width=20)
        self.mainWindow.button20zl.grid(row=9, column=1)
        self.mainWindow.button50zl = tk.Button(self.mainWindow, text = "50zł", width=20)
        self.mainWindow.button50zl.grid(row=10, column=1)

        #Pole pozwalające wpisać liczbę wrzucanych pieniędzy
        self.mainWindow.empty2 = tk.Label(self.mainWindow, text=" ").grid(row=11)
        self.mainWindow.labelLiczbaWrzucanych = tk.Label(self.mainWindow, text="Liczba wrzucanych: ", width=20).grid(row=12, column=0)
        self.mainWindow.entryLiczbaWrzucanychPieniedzy = tk.Entry(self.mainWindow, width=20)
        self.mainWindow.entryLiczbaWrzucanychPieniedzy.grid(row=12, column=1)

        #Przycisk zatwierdź
        self.mainWindow.empty3 = tk.Label(self.mainWindow, text=" ").grid(row=13)
        self.mainWindow.buttonZatwierdz = tk.Button(self.mainWindow, text = "Zatwierdź", width=40)
        self.mainWindow.buttonZatwierdz.grid(row=14, column=0, columnspan = 2)

        #Zmiana aktualnej godziny
        self.mainWindow.empty4 = tk.Label(self.mainWindow, text=" ").grid(row=13)
        self.mainWindow.buttonZmianaAktualnejGodziny = tk.Button(self.mainWindow, text = "Zmiana aktualnej godziny", width=40)
        self.mainWindow.buttonZmianaAktualnejGodziny.grid(row=15, column=0, columnspan=2)
    


# Logika
class Controller():

    def __init__(self):
        self.root = tk.Tk()
        self.przechowywaczPieniedzy = PrzechowywaczPieniedzy()
        self.zmianaAktualnejDaty = ''
        self.view=View(self.root)
        self.view.mainWindow.button1gr.bind("<Button>", lambda event, wartosc=0.01: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button2gr.bind("<Button>", lambda event, wartosc=0.02: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button5gr.bind("<Button>", lambda event, wartosc=0.05: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button10gr.bind("<Button>", lambda event, wartosc=0.10: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button20gr.bind("<Button>", lambda event, wartosc=0.20: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button50gr.bind("<Button>", lambda event, wartosc=0.50: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button1zl.bind("<Button>", lambda event, wartosc=1: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button2zl.bind("<Button>", lambda event, wartosc=2: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button5zl.bind("<Button>", lambda event, wartosc=5: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button10zl.bind("<Button>", lambda event, wartosc=10: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button20zl.bind("<Button>", lambda event, wartosc=20: self.dodajPieniadze(wartosc))
        self.view.mainWindow.button50zl.bind("<Button>", lambda event, wartosc=50: self.dodajPieniadze(wartosc))
        self.view.mainWindow.buttonZatwierdz.bind("<Button>", self.zatwierdz)
        self.view.mainWindow.buttonZmianaAktualnejGodziny.bind("<Button>", self.zmianaAktualnejGodziny)
        self.setEntryText(self.view.mainWindow.entryLiczbaWrzucanychPieniedzy, "1")
        self.setAktualnyCzas()
        self.setlLabelText(self.view.mainWindow.labelWrzucono,str(self.przechowywaczPieniedzy.Suma())+" zł")
        self.run()

    def run(self):
        self.root.mainloop()

    def setEntryText(self, cntrl, text):
        """
        Pomocnik do ustawiania tekstu w kontrolkach typu Entry
        """
        cntrl.delete(0, tk.END)
        cntrl.insert(0,text)

    def setlLabelText(self, cntrl, text):
        """
        Pomocnik do ustawiania tekstu w kontrolkach typu Label
        """
        cntrl.config(text=text)

    def dodajPieniadze(self, wartosc, waluta = 'PLN'):
        """
        Funkcja do dodania wartości wybranej momnety do sumy
        """
        _liczbaWrzucanychPieniedzy = int(self.view.mainWindow.entryLiczbaWrzucanychPieniedzy.get()) if self.view.mainWindow.entryLiczbaWrzucanychPieniedzy.get().isdigit() else None
        if _liczbaWrzucanychPieniedzy is None or _liczbaWrzucanychPieniedzy < 1:
            messagebox.showerror("Błąd", "Liczba wrzucanych pieniędzy musi być liczbą naturalną dodatnią.")
        else:
            for x in range(_liczbaWrzucanychPieniedzy):
                result = self.przechowywaczPieniedzy.DodajPieniadze(Moneta(wartosc, waluta) if wartosc < 10 else Banknot(wartosc, waluta))
                if result != None:
                    messagebox.showerror("Błąd", result)
                    break
            self.setlLabelText(self.view.mainWindow.labelWrzucono,str(self.przechowywaczPieniedzy.Suma())+" zł")
            self.aktualizacjaCzasu()
        self.setEntryText(self.view.mainWindow.entryLiczbaWrzucanychPieniedzy, "1")

    def setAktualnyCzas(self):
        """
        Funkcja odpowiadająca za aktualizacje czasu
        """
        if self.zmianaAktualnejDaty != '':
            self.view.mainWindow.labelAktualnaData.config(text = self.zmianaAktualnejDaty)
        else:
            self.view.mainWindow.labelAktualnaData.config(text = time.strftime("%d") + "." + time.strftime("%m") + "." + time.strftime("%Y") + " " + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
        
        self.aktualizacjaCzasu()
        self.view.mainWindow.labelAktualnaData.after(1000, self.setAktualnyCzas)


    def zatwierdz(self,event):
        """
        Funkcja weryfikująca, zatwierdzająca oraz resetująca dane
        """
        if self.view.mainWindow.entryNumerRejestracyjny.get() is None or self.view.mainWindow.entryNumerRejestracyjny.get() == "":
                messagebox.showerror("Błąd", "Nie wpisano numeru rejestracyjnego pojazdu.")
        elif bool(re.match('^[A-Z0-9]*$', self.view.mainWindow.entryNumerRejestracyjny.get())) == False:
                messagebox.showerror("Błąd", "Numer rejestracyjny może składać się tylko z wielkich liter od A do Z i cyfr.")
        elif self.przechowywaczPieniedzy.Suma() == 0:
                messagebox.showerror("Błąd", "Nie wrzucono żadnych pieniędzy.")
        else:
            messagebox.showinfo("Info", "Parking opłacony. Numer rejestracyjny: " + self.view.mainWindow.entryNumerRejestracyjny.get() + ", czas zakupu: " + self.view.mainWindow.labelAktualnaData.cget("text") + ", termin wyjazdu: " + self.view.mainWindow.labelDataWyjazduZParkingu.cget("text"))
            self.resetData()
            self.setEntryText(self.view.mainWindow.entryLiczbaWrzucanychPieniedzy, "1")
            self.setEntryText(self.view.mainWindow.entryNumerRejestracyjny, "")
            self.setlLabelText(self.view.mainWindow.labelWrzucono,str(self.przechowywaczPieniedzy.Suma())+" zł")


    def resetData(self):
        """
        Resetuje wszystkie dane parkometru (np. po opłaceniu resetuje się aby kolejna osoba mogła opłacić swój parking)
        """
        self.przechowywaczPieniedzy.Reset()
        self.zmianaAktualnejDaty = ''

    def pobierzDateSekundy(self,start, x):
        """
        Funkcja zwracająca datę wyjazdu na podstawie aktualnej daty oraz liczby sekund,
        która jest aktualnie opłacona jeśli chodzi o parkowanie
        """
        if x == 0:
            return start
        rr = rrule(SECONDLY, byweekday=(MO, TU, WE, TH, FR), byhour=(8,9,10,11,12,13,14,15,16,17,18,19), dtstart=start, interval=x)
        return rr.after(start)

    def getSekundyDlaDodanychPieniedzy(self,suma: int) -> int: #TODO do dokończenia obliczanie daty wyjazdu
        """
        Funkcja zwracająca czas wyrażony w sekundach, na który pozwala aktalnie
        wrzucona wartość pieniędzy
        """
        t3 = (suma - 6) / 5
        t2 = math.floor(t3)
        t = max(0, t2)
        hours = (suma >= 2) * 1 + (suma >= 6) * 1 + max(0, math.floor((suma - 6) / 5))
        return hours * 60 * 60

    def getAktualnaData(self) -> datetime:
        """
        Funkcja zwracająca aktualnie wybraną date jako obiekt typu datetime
        """
        return datetime.strptime(self.view.mainWindow.labelAktualnaData.cget("text"),'%d.%m.%Y %H:%M:%S')

    def aktualizacjaCzasu(self):
        """
        Funkcja aktualizujaca czas wyjazdu
        """
        if  self.przechowywaczPieniedzy.Suma() >= 1:
            self.setlLabelText(self.view.mainWindow.labelDataWyjazduZParkingu,self.pobierzDateSekundy(self.getAktualnaData(), self.getSekundyDlaDodanychPieniedzy(self.przechowywaczPieniedzy.Suma())).strftime('%d.%m.%Y %H:%M:%S')) #TODO do dokończenia obliczanie daty wyjazdu
        else:
            self.view.mainWindow.labelDataWyjazduZParkingu.config(text = "---------------------")

    def zmianaAktualnejGodziny(self, event):
        """
        Funkcja otwierająca okno służące do wyboru niestandardowej daty oraz godziny
        """
        wybranaData = None
        windowZmianaAktualnejGodziny = tk.Toplevel()
        windowZmianaAktualnejGodziny.title("Zmiana godziny")
        windowZmianaAktualnejGodziny.wm_iconbitmap('IkonaParkomat.ico')
        cal = DateEntry(windowZmianaAktualnejGodziny,selectmode='day', background='darkblue', foreground='white', borderwidth=2)
        cal.grid(row=0, column=0)
        entryGodzina = tk.Entry(windowZmianaAktualnejGodziny, width = 2)
        entryGodzina.grid(row=0, column=1)
        tk.Label(windowZmianaAktualnejGodziny, text=":", width=1).grid(row=0, column=2)
        entryMinuta = tk.Entry(windowZmianaAktualnejGodziny, width = 2)
        entryMinuta.grid(row=0, column=3)
        tk.Label(windowZmianaAktualnejGodziny, text=":", width=0).grid(row=0, column=4)
        entrySekunda = tk.Entry(windowZmianaAktualnejGodziny, width = 2)
        entrySekunda.grid(row=0, column=5)

        def zmianaAktualnejGodzinyClose():
            _godziny = int(entryGodzina.get()) if entryGodzina.get().isdigit() else None
            _minuty = int(entryMinuta.get()) if entryMinuta.get().isdigit() else None
            _sekundy = int(entrySekunda.get()) if entrySekunda.get().isdigit() else None
            if(_godziny is None or _godziny < 0 or _godziny > 23 or _minuty is None or _minuty < 0 or _minuty > 60 or _sekundy is None or _sekundy < 0 or _sekundy > 60):
                messagebox.showerror("Błąd", "Ustawiona data jest niepoprawna. Spróbuj ponownie.")
            else:
                _data = (datetime.strptime(cal.get_date().strftime('%d.%m.%Y'), '%d.%m.%Y') + timedelta(hours=_godziny, minutes=_minuty, seconds= _sekundy)).strftime('%d.%m.%Y %H:%M:%S')
                nonlocal wybranaData
                wybranaData = _data
                windowZmianaAktualnejGodziny.destroy()

        buttonOk = tk.Button(windowZmianaAktualnejGodziny, text = "OK", width=2, command= zmianaAktualnejGodzinyClose)
        buttonOk.grid(row=0, column=6)
        entryGodzina.delete(0, tk.END)
        entryGodzina.insert(0,"00")
        entryMinuta.delete(0, tk.END)
        entryMinuta.insert(0,"00")
        entrySekunda.delete(0, tk.END)
        entrySekunda.insert(0,"00")

        windowZmianaAktualnejGodziny.wait_window(windowZmianaAktualnejGodziny)
        
        self.zmianaAktualnejDaty = wybranaData

if __name__ == '__main__':
    c = Controller()