import tkinter
from tkinter import messagebox
import unittest
from Controller import ParkomatController
from Controller.DateSelectionController import DateSelectorController
from Controller.ParkomatController import Controller
from Exceptions.ParkomatExceptions import ZlyNominalExcepion


class TestsParkomat(unittest.TestCase):
    
    __parkomatApp = Controller()

    def test_1(self):
        t = DateSelectorController(self.__parkomatApp)
        t.GetView().Godzina = 25
        t.zmianaAktualnejGodzinyClose()
        t.GetView().Godzina = 12
        t.GetView().Minuta = 34
        t.zmianaAktualnejGodzinyClose()
        self.__parkomatApp.resetData()

    def test_2(self):
        self.__parkomatApp.dodajPieniadze(2)
        self.__parkomatApp.dodajPieniadze(2)
        self.__parkomatApp.dodajPieniadze(2)
        self.__parkomatApp.dodajPieniadze(5)
        self.__parkomatApp.dodajPieniadze(5)
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_3(self):
        self.__parkomatApp.setAktualnaData("20.01.2022 19:01")
        self.__parkomatApp.GetView().NumerRejestracyjny = "KRA123"
        self.__parkomatApp.dodajPieniadze(5)
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_4(self):
        self.__parkomatApp.setAktualnaData("21.01.2022 19:01")
        self.__parkomatApp.GetView().NumerRejestracyjny = "KRA123"
        self.__parkomatApp.dodajPieniadze(5)
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_5(self):
        self.__parkomatApp.GetView().NumerRejestracyjny = "KRA123"
        self.__parkomatApp.dodajPieniadze(1)
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_6(self):
        self.__parkomatApp.GetView().NumerRejestracyjny = "KRA321"
        self.__parkomatApp.GetView().LiczbaWrzucanychPieniedzy = "200"
        self.__parkomatApp.dodajPieniadze(0.01)
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_7(self):
        self.__parkomatApp.GetView().LiczbaWrzucanychPieniedzy = "200"
        self.__parkomatApp.dodajPieniadze(0.01)
        self.__parkomatApp.resetData()

    def test_8(self):
        self.__parkomatApp.GetView().NumerRejestracyjny = "KRA123"
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_9(self):
        self.__parkomatApp.dodajPieniadze(10)
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.GetView().NumerRejestracyjny = "asdasfsad"
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()


if __name__ == "__main__":
    unittest.main()
