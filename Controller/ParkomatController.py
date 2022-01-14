import datetime
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
    """
    Główna klasa obsługująca logikę parkomatu
    """

    def __init__(self):
        self.__root = tk.Tk()
        self.__przechowywaczPieniedzy = PrzechowywaczPieniedzy()
        self.__zmianaAktualnejDaty = ''
        self.__view = View(self.__root)
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
        self.__view.BindButtonZmianaAktualnejGodziny(
            self.zmianaAktualnejGodziny)
        self.__view.LiczbaWrzucanychPieniedzy = "1"
        self.__view.Wrzucono = str(self.__przechowywaczPieniedzy.Suma())+" zł"
        self.__view.ResetDataWyjazduZParkingu()
        self.setAktualnyCzas()

    def run(self):
        """
        Uruchamia główną pętle programu
        """
        self.__root.mainloop()

    def dodajPieniadze(self, wartosc, waluta='PLN'):
        """
        Funkcja do dodania wartości wybranej momnety do sumy
        """
        liczbaWrzucanychPieniedzy = int(
            self.__view.LiczbaWrzucanychPieniedzy) if self.__view.LiczbaWrzucanychPieniedzy.isdigit() else None
        if liczbaWrzucanychPieniedzy is None or liczbaWrzucanychPieniedzy < 1:
            messagebox.showerror(
                "Błąd", "Liczba wrzucanych pieniędzy musi być liczbą dodatnią.")
        else:
            for x in range(liczbaWrzucanychPieniedzy):
                result = self.__przechowywaczPieniedzy.DodajPieniadze(
                    Moneta(wartosc, waluta) if wartosc < 10 else Banknot(wartosc, waluta))
                if result != None:
                    messagebox.showerror("Błąd", result)
                    break
            self.__view.Wrzucono = str(
                self.__przechowywaczPieniedzy.Suma())+" zł"
            self.aktualizacjaCzasu()
        self.__view.LiczbaWrzucanychPieniedzy = "1"

    def setAktualnyCzas(self):
        """
        Funkcja odpowiadająca za aktualizacje czasu
        """
        if self.__zmianaAktualnejDaty != '':
            self.__view.AktualnaData = self.__zmianaAktualnejDaty
        else:
            self.__view.AktualnaData = time.strftime("%d") + "." + time.strftime("%m") + "." + time.strftime(
                "%Y") + " " + time.strftime("%H") + ":" + time.strftime("%M")

        self.aktualizacjaCzasu()
        self.__view.SetAktualnaDataTimerEvent(1000, self.setAktualnyCzas)

    def zatwierdz(self, event):
        """
        Funkcja weryfikująca, zatwierdzająca oraz resetująca dane
        """
        if self.__view.NumerRejestracyjny is None or self.__view.NumerRejestracyjny == "":
            messagebox.showerror(
                "Błąd", "Nie wpisano numeru rejestracyjnego pojazdu.")
        elif bool(re.match('^[A-Z0-9]*$', self.__view.NumerRejestracyjny)) == False:
            messagebox.showerror(
                "Błąd", "Numer rejestracyjny może składać się tylko z wielkich liter od A do Z i cyfr.")
        elif self.__przechowywaczPieniedzy.Suma() == 0:
            messagebox.showerror("Błąd", "Nie wrzucono żadnych pieniędzy.")
        else:
            self.setAktualnyCzas()
            messagebox.showinfo("Info", "Parking opłacony. Numer rejestracyjny: " + self.__view.NumerRejestracyjny + ", czas zakupu: " +
                                self.__view.AktualnaData.strftime('%d.%m.%Y %H:%M') + ", termin wyjazdu: " + self.__view.DataWyjazduZParkingu)
            self.resetData()
            self.__view.LiczbaWrzucanychPieniedzy = "1"
            self.__view.NumerRejestracyjny = ""
            self.__view.Wrzucono = str(
                self.__przechowywaczPieniedzy.Suma())+" zł"

    def resetData(self):
        """
        Resetuje wszystkie dane parkometru (np. po opłaceniu resetuje się aby kolejna osoba mogła opłacić swój parking)
        """
        self.__przechowywaczPieniedzy.Reset()
        self.__zmianaAktualnejDaty = ''

    def pobierzDateSekundy(self, aktualnaData, liczbaSekund):
        """
        Funkcja zwracająca datę wyjazdu na podstawie aktualnej daty oraz liczby sekund,
        która jest aktualnie opłacona jeśli chodzi o parkowanie
        """
        start = self.getDataRozpoczecia(aktualnaData, liczbaSekund)
        licznikDodanychSekund = 0
        returnValue = None
        while True:
            dodanaData = start + datetime.timedelta(0, 1)
            if dodanaData.weekday() == 5 or dodanaData.weekday() == 6:
                start = dodanaData
                continue
            if dodanaData.hour > 19 or dodanaData.hour < 8:
                start = dodanaData
                continue
            licznikDodanychSekund = licznikDodanychSekund + 1
            start = dodanaData
            if licznikDodanychSekund == liczbaSekund:
                returnValue = dodanaData
                break
            
        if returnValue == None:
            raise BrakDatyWyjazduException("returnValue is None")
        else:
            return returnValue

    def getDataRozpoczecia(self, start, liczbaSekund) -> datetime:
        """
        Funkcja zwracająca datę początkową z walidacją godzin i dni kiedy parkomat nie działa
        """
        darmowe_godziny = [0, 1, 2, 3, 4, 5, 6, 7, 20, 21, 22, 23]

        if liczbaSekund > 0:
            if start.hour in darmowe_godziny:

                if start.weekday() == 4:
                    start = start + datetime.timedelta(days=3)
                elif start.weekday() == 5:
                    start = start + datetime.timedelta(days=2)
                elif start.weekday() == 6:
                    start = start + datetime.timedelta(days=1)

                if start.hour > 19 or start.hour < 8:
                    start = start.replace(hour=8, minute=00)

        return start

    def getSekundyDlaDodanychPieniedzy(self, suma: int) -> int:
        """
        Funkcja zwracająca czas wyrażony w sekundach, na który pozwala aktalnie
        wrzucona wartość pieniędzy
        """
        if suma <= 2:
            return math.floor(18 * suma * 100)
        if suma > 2 and suma <= 6:
            return math.floor(9 * (suma - 2) * 100) + 3600
        if suma > 6:
            return math.floor(72 * (suma - 6) * 10) + 3600 * 2

    def aktualizacjaCzasu(self):
        """
        Funkcja aktualizujaca czas wyjazdu
        """
        if self.__przechowywaczPieniedzy.Suma() >= 1:
            self.__view.DataWyjazduZParkingu = (self.pobierzDateSekundy(self.__view.AktualnaData, self.getSekundyDlaDodanychPieniedzy(
                self.__przechowywaczPieniedzy.Suma())).strftime('%d.%m.%Y %H:%M'))
        else:
            self.__view.ResetDataWyjazduZParkingu()

    def zmianaAktualnejGodziny(self, event):
        """
        Funkcja otwierająca okno służące do wyboru niestandardowej daty oraz godziny
        """
        dsc = DateSelectorController(self)
        dsc.run()

    def GetView(self):
        """
        Funkcja zwracająca instancje widoku. Tylko do testów jednostkowych.
        """
        return self.__view

    def setAktualnaData(self, data):
        """
        Funkcja ustawiająca aktualną datę. Tylko do testów jednostkowych.
        """
        self.__zmianaAktualnejDaty = data
