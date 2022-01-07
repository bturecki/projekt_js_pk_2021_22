import tkinter
from tkinter import messagebox
import unittest
from Controller.ParkomatController import Controller
from Model.ParkomatExceptions import ZlyNominalExcepion

class TestParkomat5(unittest.TestCase):
    
    def test_1_zl(self):
        parkomatApp = Controller()
        parkomatApp.setEntryText(parkomatApp.view.mainWindow.entryNumerRejestracyjny, "KR123")
        parkomatApp.dodajPieniadze(1)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()
        parkomatApp.view.mainWindow.destroy()

class TestParkomat6(unittest.TestCase):
    
    def test_200_monet(self):
        parkomatApp = Controller()
        parkomatApp.setEntryText(parkomatApp.view.mainWindow.entryNumerRejestracyjny, "KR123")
        parkomatApp.setEntryText(parkomatApp.view.mainWindow.entryLiczbaWrzucanychPieniedzy, "200")
        parkomatApp.dodajPieniadze(0.01)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()
        parkomatApp.view.mainWindow.destroy()

class TestParkomat7(unittest.TestCase):
    
    def test_201_monet(self):
        parkomatApp = Controller()
        parkomatApp.setEntryText(parkomatApp.view.mainWindow.entryLiczbaWrzucanychPieniedzy, "201")
        parkomatApp.dodajPieniadze(0.01)
        parkomatApp.resetData()
        parkomatApp.view.mainWindow.destroy()

class TestParkomat8(unittest.TestCase):

    def test_zatwierdz_bez_wrzucenia_monet(self):
        parkomatApp = Controller()
        parkomatApp.setEntryText(parkomatApp.view.mainWindow.entryNumerRejestracyjny, "KRA123")
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()
        parkomatApp.view.mainWindow.destroy()

class TestParkomat9(unittest.TestCase):

    def test_zatwierdz_bez_lub_bledny_numer_rej(self):
        parkomatApp = Controller()
        parkomatApp.dodajPieniadze(10)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.setEntryText(parkomatApp.view.mainWindow.entryNumerRejestracyjny, "asfasf")
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.resetData()
        parkomatApp.view.mainWindow.destroy()

if __name__ == "__main__":
    unittest.main()