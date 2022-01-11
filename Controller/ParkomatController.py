import tkinter as tk
from tkinter import messagebox
import time
from dateutil.rrule import *  
import re
import math
from Controller.DateSelectionController import DateSelectorController
from Model.Pieniadze import *
from View.ParkomatView import View


            
class Controller():

    def __init__(self):
        self.__root = tk.Tk()
        self.__przechowywaczPieniedzy = PrzechowywaczPieniedzy()
        self.__zmianaAktualnejDaty = ''
        self.__view=View(self.__root)
        self.__view.BindButton1gr(self.dodajPieniadze)
        self.__view.BindButton2gr(self.dodajPieniadze)
        self.__view.BindButton5gr(self.dodajPieniadze)
        self.__view.BindButton10gr(self.dodajPieniadze)
        self.__view.BindButton20gr(self.dodajPieniadze)
        self.__view.BindButton50gr(self.dodajPieniadze)
        self.__view.BindButton1zl(self.dodajPieniadze)
        self.__view.BindButton2zl(self.dodajPieniadze)
        self.__view.BindButton5zl(self.dodajPieniadze)
        self.__view.BindButton10zl(self.dodajPieniadze)
        self.__view.BindButton20zl(self.dodajPieniadze)
        self.__view.BindButton50zl(self.dodajPieniadze)
        self.__view.BindButtonZatwierdz(self.zatwierdz)
        self.__view.BindButtonZmianaAktualnejGodziny(self.zmianaAktualnejGodziny)
        self.__view.SetLiczbaWrzucanychPieniedzy("1")
        self.__view.SetWrzucono(str(self.__przechowywaczPieniedzy.Suma())+" zł")
        self.__view.ResetDataWyjazduZParkingu()
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
            messagebox.showerror("Błąd", "Liczba wrzucanych pieniędzy musi być liczbą dodatnią.")
        else:
            for x in range(liczbaWrzucanychPieniedzy):
                result = self.__przechowywaczPieniedzy.DodajPieniadze(Moneta(wartosc, waluta) if wartosc < 10 else Banknot(wartosc, waluta))
                if result != None:
                    messagebox.showerror("Błąd", result)
                    break
            self.__view.SetWrzucono(str(self.__przechowywaczPieniedzy.Suma())+" zł")
            self.aktualizacjaCzasu()
        self.__view.SetLiczbaWrzucanychPieniedzy("1")

    def setAktualnaData(self, data):
        self.__zmianaAktualnejDaty = data

    def setAktualnyCzas(self):
        """
        Funkcja odpowiadająca za aktualizacje czasu
        """
        if self.__zmianaAktualnejDaty != '':
            self.__view.SetAktualnaData(self.__zmianaAktualnejDaty)
        else:
            self.__view.SetAktualnaData(time.strftime("%d") + "." + time.strftime("%m") + "." + time.strftime("%Y") + " " + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
        
        self.aktualizacjaCzasu()
        self.__view.SetAktualnaDataTimerEvent(1000, self.setAktualnyCzas)

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
            messagebox.showinfo("Info", "Parking opłacony. Numer rejestracyjny: " + self.__view.GetNumerRejestracyjny() + ", czas zakupu: " + self.__view.GetAktualnaData().strftime('%d.%m.%Y %H:%M:%S') + ", termin wyjazdu: " + self.__view.GetDataWyjazduZParkingu())
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
            return math.floor(18 * suma * 100)
        if suma > 2 and suma <= 6:
            return math.floor(9 * (suma - 2) * 100)+ 3600
        if suma > 6:
            return math.floor(72 * (suma - 6) * 10) + 3600 * 2

    def aktualizacjaCzasu(self):
        """
        Funkcja aktualizujaca czas wyjazdu
        """
        if  self.__przechowywaczPieniedzy.Suma() >= 1:
            self.__view.SetDataWyjazduZParkingu(self.pobierzDateSekundy(self.__view.GetAktualnaData(), self.getSekundyDlaDodanychPieniedzy(self.__przechowywaczPieniedzy.Suma())).strftime('%d.%m.%Y %H:%M:%S')) #TODO do dokończenia obliczanie daty wyjazdu
        else:
            self.__view.ResetDataWyjazduZParkingu()

    def zmianaAktualnejGodziny(self, event):
        """
        Funkcja otwierająca okno służące do wyboru niestandardowej daty oraz godziny
        """
        DateSelectorController(self)