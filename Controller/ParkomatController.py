import tkinter as tk
from tkinter import messagebox
import time
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from dateutil.rrule import *  
import re
import math
from Model.Pieniadze import *
from View.ParkomatView import View

class Controller():

    def __init__(self):
        self.__root = tk.Tk()
        self.__przechowywaczPieniedzy = PrzechowywaczPieniedzy()
        self.__zmianaAktualnejDaty = ''
        self.__view=View(self.__root)
        self.__view.GetMainWindow().button1gr.bind("<Button>", lambda event, wartosc=0.01: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button2gr.bind("<Button>", lambda event, wartosc=0.02: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button5gr.bind("<Button>", lambda event, wartosc=0.05: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button10gr.bind("<Button>", lambda event, wartosc=0.10: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button20gr.bind("<Button>", lambda event, wartosc=0.20: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button50gr.bind("<Button>", lambda event, wartosc=0.50: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button1zl.bind("<Button>", lambda event, wartosc=1: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button2zl.bind("<Button>", lambda event, wartosc=2: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button5zl.bind("<Button>", lambda event, wartosc=5: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button10zl.bind("<Button>", lambda event, wartosc=10: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button20zl.bind("<Button>", lambda event, wartosc=20: self.dodajPieniadze(wartosc))
        self.__view.GetMainWindow().button50zl.bind("<Button>", lambda event, wartosc=50: self.dodajPieniadze(wartosc))
        self.__view.BindButtonZatwierdz(self.zatwierdz)
        self.__view.BindButtonZmianaAktualnejGodziny(self.zmianaAktualnejGodziny)
        self.__view.SetLiczbaWrzucanychPieniedzy("1")
        self.__view.SetWrzucono(str(self.__przechowywaczPieniedzy.Suma())+" zł")
        self.setAktualnyCzas()

    def run(self):
        """
        Uruchamia główną pętle programu
        """
        self.__root.mainloop()

    def dodajPieniadze(self, wartosc, waluta = 'PLN'):
        """
        Funkcja do dodania wartości wybranej momnety do sumy
        """
        liczbaWrzucanychPieniedzy = int(self.__view.GetLiczbaWrzucanychPieniedzy()) if self.__view.GetLiczbaWrzucanychPieniedzy().isdigit() else None
        if liczbaWrzucanychPieniedzy is None or liczbaWrzucanychPieniedzy < 1:
            messagebox.showerror("Błąd", "Liczba wrzucanych pieniędzy musi być liczbą naturalną dodatnią.")
        else:
            for x in range(liczbaWrzucanychPieniedzy):
                result = self.__przechowywaczPieniedzy.DodajPieniadze(Moneta(wartosc, waluta) if wartosc < 10 else Banknot(wartosc, waluta))
                if result != None:
                    messagebox.showerror("Błąd", result)
                    break
            self.__view.SetWrzucono(str(self.__przechowywaczPieniedzy.Suma())+" zł")
            self.aktualizacjaCzasu()
        self.__view.SetLiczbaWrzucanychPieniedzy("1")

    def setAktualnyCzas(self):
        """
        Funkcja odpowiadająca za aktualizacje czasu
        """
        if self.__zmianaAktualnejDaty != '':
            self.__view.GetMainWindow().labelAktualnaData.config(text = self.__zmianaAktualnejDaty)
        else:
            self.__view.GetMainWindow().labelAktualnaData.config(text = time.strftime("%d") + "." + time.strftime("%m") + "." + time.strftime("%Y") + " " + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
        
        self.aktualizacjaCzasu()
        self.__view.GetMainWindow().labelAktualnaData.after(1000, self.setAktualnyCzas)


    def zatwierdz(self,event):
        """
        Funkcja weryfikująca, zatwierdzająca oraz resetująca dane
        """
        if self.__view.GetNumerRejestracyjny() is None or self.__view.GetNumerRejestracyjny() == "":
                messagebox.showerror("Błąd", "Nie wpisano numeru rejestracyjnego pojazdu.")
        elif bool(re.match('^[A-Z0-9]*$', self.__view.GetNumerRejestracyjny())) == False:
                messagebox.showerror("Błąd", "Numer rejestracyjny może składać się tylko z wielkich liter od A do Z i cyfr.")
        elif self.__przechowywaczPieniedzy.Suma() == 0:
                messagebox.showerror("Błąd", "Nie wrzucono żadnych pieniędzy.")
        else:
            messagebox.showinfo("Info", "Parking opłacony. Numer rejestracyjny: " + self.__view.GetNumerRejestracyjny() + ", czas zakupu: " + self.__view.GetMainWindow().labelAktualnaData.cget("text") + ", termin wyjazdu: " + self.__view.GetDataWyjazduZParkingu())
            self.resetData()
            self.__view.SetLiczbaWrzucanychPieniedzy("1")
            self.__view.SetNumerRejestracyjny("")
            self.__view.SetWrzucono(str(self.__przechowywaczPieniedzy.Suma())+" zł")

    def resetData(self):
        """
        Resetuje wszystkie dane parkometru (np. po opłaceniu resetuje się aby kolejna osoba mogła opłacić swój parking)
        """
        self.__przechowywaczPieniedzy.Reset()
        self.__zmianaAktualnejDaty = ''

    def pobierzDateSekundy(self,start, liczbaSekund):
        """
        Funkcja zwracająca datę wyjazdu na podstawie aktualnej daty oraz liczby sekund,
        która jest aktualnie opłacona jeśli chodzi o parkowanie
        """
        if liczbaSekund == 0:
            return start
        rr = rrule(SECONDLY, byweekday=(MO, TU, WE, TH, FR), byhour=(8,9,10,11,12,13,14,15,16,17,18,19), dtstart=start, interval=liczbaSekund)
        return rr.after(start)

    def getSekundyDlaDodanychPieniedzy(self,suma: int) -> int:
        """
        Funkcja zwracająca czas wyrażony w sekundach, na który pozwala aktalnie
        wrzucona wartość pieniędzy
        """
        if suma <= 2:
            return (18 * suma * 100)
        if suma > 2 and suma <= 6:
            return (9 * (suma - 2) * 100)+ 3600
        if suma > 6:
            return (72 * (suma - 6) * 10) + 3600 * 2

    def getAktualnaData(self) -> datetime:
        """
        Funkcja zwracająca aktualnie wybraną date jako obiekt typu datetime
        """
        return datetime.strptime(self.__view.GetMainWindow().labelAktualnaData.cget("text"),'%d.%m.%Y %H:%M:%S')

    def aktualizacjaCzasu(self):
        """
        Funkcja aktualizujaca czas wyjazdu
        """
        if  self.__przechowywaczPieniedzy.Suma() >= 1:
            self.__view.SetDataWyjazduZParkingu(self.pobierzDateSekundy(self.getAktualnaData(), self.getSekundyDlaDodanychPieniedzy(self.__przechowywaczPieniedzy.Suma())).strftime('%d.%m.%Y %H:%M:%S')) #TODO do dokończenia obliczanie daty wyjazdu
        else:
            self.__view.SetDataWyjazduZParkingu("---------------------")

    def zmianaAktualnejGodziny(self, event):
        """
        Funkcja otwierająca okno służące do wyboru niestandardowej daty oraz godziny
        """
        wybranaData = None
        windowZmianaAktualnejGodziny = tk.Toplevel()
        windowZmianaAktualnejGodziny.title("Zmiana godziny")
        windowZmianaAktualnejGodziny.wm_iconbitmap('Resources/IkonaParkomat.ico')
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
        
        self.__zmianaAktualnejDaty = wybranaData