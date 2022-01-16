import tkinter
from tkinter import messagebox
import unittest
from Controller import ParkomatController
from Controller.DateSelectionController import DateSelectorController
from Controller.ParkomatController import Controller
from Exceptions.ParkomatExceptions import ZlyNominalExcepion


class TestsParkomat(unittest.TestCase):

    def setUp(self):
        self.__parkomatApp = Controller()

    def tearDown(self):
        self.__parkomatApp.resetData()

    def test_1(self):
        self.__parkomatApp.resetData()
        t = DateSelectorController(self.__parkomatApp)
        # Ustawiam niepoprawną godzinę, pojawia się komunikat o błędzie
        t.GetView().Godzina = 25
        t.zmianaAktualnejGodzinyClose()
        t.GetView().Godzina = 12  # Ustawiam poprawną godzinę
        t.GetView().Minuta = 34
        t.zmianaAktualnejGodzinyClose()
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST1"
        # Dodaje pieniądze żeby pojawił się komunikat
        self.__parkomatApp.dodajPieniadze(2)
        self.assertNotIn(
            "-", self.__parkomatApp.GetView().DataWyjazduZParkingu)
        # Zatwierdzam i pokazuje komunikat o aktualnej dacie
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_2(self):
        self.__parkomatApp.resetData()
        self.__parkomatApp.dodajPieniadze(2)
        self.__parkomatApp.dodajPieniadze(2)
        self.__parkomatApp.dodajPieniadze(2)
        self.__parkomatApp.dodajPieniadze(5)
        self.__parkomatApp.dodajPieniadze(5)
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST2"
        self.assertNotIn(
            "-", self.__parkomatApp.GetView().DataWyjazduZParkingu)

        # Zatwierdzam, komunikat - czas wyjazdu 4 godziny po aktualnej dacie
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_3(self):
        self.__parkomatApp.resetData()
        self.__parkomatApp.setAktualnaData("20.01.2022 19:01")
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST3"
        self.__parkomatApp.dodajPieniadze(5)
        self.assertNotIn(
            "-", self.__parkomatApp.GetView().DataWyjazduZParkingu)
        # Zatwierdzam, komunikat - czas wyjazdu na następny dzień
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_4(self):
        self.__parkomatApp.resetData()
        self.__parkomatApp.setAktualnaData("21.01.2022 19:01")
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST4"
        self.__parkomatApp.dodajPieniadze(5)
        self.assertNotIn(
            "-", self.__parkomatApp.GetView().DataWyjazduZParkingu)
        # Zatwierdzam, komunikat - czas wyjazdu na następny tydzień
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_5(self):
        self.__parkomatApp.resetData()
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST5"
        self.__parkomatApp.dodajPieniadze(1)
        self.assertNotIn(
            "-", self.__parkomatApp.GetView().DataWyjazduZParkingu)
        # Zatwierdzam, komunikat - czas wyjazdu pół godziny po aktualnym czasie
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_6(self):
        self.__parkomatApp.resetData()
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST6"
        self.__parkomatApp.GetView().LiczbaWrzucanychPieniedzy = "200"
        self.__parkomatApp.dodajPieniadze(0.01)
        self.assertEqual(self.__parkomatApp.GetPrzechowywaczMonet().Suma(), 2)
        # Zatwierdzam, komunikat - czas wyjazdu godzina po aktualnym czasie
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_7(self):
        self.__parkomatApp.resetData()
        self.__parkomatApp.GetView().LiczbaWrzucanychPieniedzy = "201"
        # Zatwierdzam, komunikat - przepełnienie parkomatu
        self.__parkomatApp.dodajPieniadze(0.01)
        self.assertEqual(self.__parkomatApp.GetPrzechowywaczMonet().Suma(), 2)
        self.__parkomatApp.resetData()

    def test_8(self):
        self.__parkomatApp.resetData()
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST8"
        self.assertIn("-", self.__parkomatApp.GetView().DataWyjazduZParkingu)
        # Zatwierdzam, komunikat - brak wrzuconych pieniędzy
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_9(self):
        self.__parkomatApp.resetData()
        self.__parkomatApp.dodajPieniadze(10)
        self.assertEqual(self.__parkomatApp.GetView().NumerRejestracyjny, "")
        # Zatwierdzam, komunikat - brak numeru rejestracyjnego
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.GetView().NumerRejestracyjny = "test9nie_poprawny_numer"
        # Zatwierdzam, komunikat - niepoprawnie wpisany numer rejestracyjny
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.assertEqual(self.__parkomatApp.GetView(
        ).NumerRejestracyjny, "test9_nie_poprawny_numer")
        self.__parkomatApp.resetData()


if __name__ == "__main__":
    unittest.main()
