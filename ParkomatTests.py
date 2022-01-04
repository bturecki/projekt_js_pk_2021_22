import tkinter
from tkinter import messagebox
import unittest
from Controller.ParkomatController import Controller
from Model.ParkomatExceptions import ZlyNominalExcepion

class TestParkomat8(unittest.TestCase):
    
    def test_zatwierdz_bez_wrzucenia_monet(self):
        parkomatApp = Controller()
        parkomatApp.setEntryText(parkomatApp.view.mainWindow.entryNumerRejestracyjny, "KRA123")
        parkomatApp.zatwierdz("<Button>")

class TestParkomat9(unittest.TestCase):
    def test_zatwierdz_bez_lub_bledny_numer_rej(self):
        parkomatApp = Controller()
        parkomatApp.dodajPieniadze(10)
        parkomatApp.zatwierdz("<Button>")
        parkomatApp.setEntryText(parkomatApp.view.mainWindow.entryNumerRejestracyjny, "asfasf")
        parkomatApp.zatwierdz("<Button>")

if __name__ == "__main__":
    unittest.main()