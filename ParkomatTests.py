import tkinter
from tkinter import messagebox
import unittest
from Controller import ParkomatController
from Controller.DateSelectionController import DateSelectorController
from Controller.ParkomatController import Controller
from Exceptions.ParkomatExceptions import ZlyNominalExcepion

class TestsParkomat(unittest.TestCase):
                               
    def test_1(self):
        parkomatApp = Controller()
        t = DateSelectorController(parkomatApp)
        t.GetView().Godzina = 25
        t.zmianaAktualnejGodzinyClose()
        t.GetView().Godzina = 12
        t.GetView().Minuta = 34
        t.zmianaAktualnejGodzinyClose()
        parkomatApp.resetData()

    def test_2(self):
        parkomatApp = Controller()
        parkomatApp.dodajPieniadze(2)
        parkomatApp.dodajPieniadze(4)
        parkomatApp.dodajPieniadze(5)
        parkomatApp.dodajPieniadze(5)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()

    def test_3(self):
        parkomatApp = Controller()
        parkomatApp.setAktualnaData("20.01.2022 19:00:01")
        parkomatApp.GetView().NumerRejestracyjny = "KRA123"
        parkomatApp.dodajPieniadze(5)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()

    def test_4(self):
        parkomatApp = Controller()
        parkomatApp.setAktualnaData("21.01.2022 19:00:01")
        parkomatApp.GetView().NumerRejestracyjny = "KRA123"
        parkomatApp.dodajPieniadze(5)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()
        
    def test_5(self):
        parkomatApp = Controller()
        parkomatApp.GetView().NumerRejestracyjny = "KRA123"
        parkomatApp.dodajPieniadze(1)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()

    def test_6(self):
        parkomatApp = Controller()
        parkomatApp.GetView().NumerRejestracyjny = "KRA321"
        parkomatApp.GetView().LiczbaWrzucanychPieniedzy = "200"
        parkomatApp.dodajPieniadze(0.01)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()

    def test_7(self):
        parkomatApp = Controller()
        parkomatApp.GetView().LiczbaWrzucanychPieniedzy = "200"
        parkomatApp.dodajPieniadze(0.01)
        parkomatApp.resetData()

    def test_8(self):
        parkomatApp = Controller()
        parkomatApp.GetView().NumerRejestracyjny = "KRA123"
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()

    def test_9(self):
        parkomatApp = Controller()
        parkomatApp.dodajPieniadze(10)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.GetView().NumerRejestracyjny = "asdasfsad"
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()

if __name__ == "__main__":
    unittest.main()