import datetime
import tkinter
from tkinter import messagebox
import unittest
from Controller import ParkomatController
from Controller.DateSelectionController import DateSelectorController
from Controller.ParkomatController import Controller
from Exceptions.ParkomatExceptions import *
import time
import re
import math
from datetime import datetime

class TestsParkomat(unittest.TestCase):

    def setUp(self):
        self.__parkomatApp = Controller()

    def tearDown(self):
        self.__parkomatApp.resetData()

    def test_1(self):
        """
        1. Ustaw niepoprawną godzinę. Oczekiwany komunikat o błędzie. Ustawić godzinę na 12:34.
        """
        self.__parkomatApp.resetData()
        t = DateSelectorController(self.__parkomatApp)
        t.GetView().Godzina = 25 #Ustawiam niepoprawną godzinę
        self.assertRaises(NiepoprawnieUstawionaDataException, t.zmianaAktualnejGodzinyClose) #Powinien być błąd
        t.GetView().Godzina = 12  # Ustawiam poprawną godzinę
        t.GetView().Minuta = 34 # Ustawiam poprawną minutę
        t.zmianaAktualnejGodzinyClose()
        self.__parkomatApp.setAktualnyCzas()
        self.assertEqual(self.__parkomatApp.GetView().AktualnaData.hour, 12) #Brak błędu - wszystko jest ok
        self.assertEqual(self.__parkomatApp.GetView().AktualnaData.minute, 34) #Brak błędu - wszystko jest ok
        self.__parkomatApp.resetData()

    def test_2(self):
        """
        2. Wrzucić 2zł, oczekiwany termin wyjazdu godzinę po aktualnym czasie.
        Dorzuć 4zł, oczekiwany termin wyjazdu dwie godziny po aktualnym czasie.
        Dorzuć 5zł, oczekiwany termin wyjazdu trzy godziny po aktualnym czasie. 
        Dorzuć kolejne 5zł, oczekiwany termin wyjazdu cztery godziny po aktualnym czasie.
        """
        self.__parkomatApp.resetData()
        self.__parkomatApp.setAktualnaData("18.01.2022 08:00") #ustawiam datę, na przykład 18.01.2022 godzina 8:00
        self.__parkomatApp.dodajPieniadze(2) #dorzucam 2 zł
        self.assertEqual(self.__parkomatApp.GetView().DataWyjazduZParkingu, "18.01.2022 09:00") #data wyjazdu godzine po aktualnej dacie
        self.__parkomatApp.dodajPieniadze(2)
        self.__parkomatApp.dodajPieniadze(2) #dorzucam 4 zł
        self.assertEqual(self.__parkomatApp.GetView().DataWyjazduZParkingu, "18.01.2022 10:00") #data wyjazdu dwie godziny po aktualnej dacie
        self.__parkomatApp.dodajPieniadze(5)
        self.assertEqual(self.__parkomatApp.GetView().DataWyjazduZParkingu, "18.01.2022 11:00") #data wyjazdu trzy godziny po aktualnej dacie
        self.__parkomatApp.dodajPieniadze(5)
        self.assertEqual(self.__parkomatApp.GetView().DataWyjazduZParkingu, "18.01.2022 12:00") #data wyjazdu cztery godziny po aktualnej dacie
        self.__parkomatApp.resetData()

    def test_3(self):
        """
        3. Wrzucić tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny dzień,
        zgodnie z zasadami -- wrzucić tyle monet aby termin wyjazdu był po godzinie 19:00,dorzucić monetę 5zł.
        """
        self.__parkomatApp.resetData()
        self.__parkomatApp.setAktualnaData("19.01.2022 19:01") #ustawiam datę, na przykład 19.01.2022 godzina 19:01
        self.__parkomatApp.dodajPieniadze(5)
        self.assertEqual(self.__parkomatApp.GetView().DataWyjazduZParkingu, "20.01.2022 08:46") #data wyjazdu na następny dzień
        self.__parkomatApp.resetData()

    def test_4(self):
        """
        4. Wrzucić tyle pieniędzy, aby termin wyjazdu przeszedł na kolejny tydzień,
        zgodnie z zasadami - wrzucić tyle monet aby termin wyjazdu był w piątek po godzinie 19:00, a potem dorzucić monetę 5zł.
        """
        self.__parkomatApp.resetData()
        self.__parkomatApp.setAktualnaData("21.01.2022 19:01") #ustawiam datę, na przykład 19.01.2022 godzina 19:01
        self.__parkomatApp.dodajPieniadze(5)
        self.assertEqual(self.__parkomatApp.GetView().DataWyjazduZParkingu, "24.01.2022 08:46") #data wyjazdu na następny tydzień
        self.__parkomatApp.resetData()

    def test_5(self):
        """
        5. Wrzucić 1zł, oczekiwany termin wyjazdu pól godziny po aktualnym czasie.
        """
        self.__parkomatApp.resetData()
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST5"
        self.__parkomatApp.dodajPieniadze(1)
        self.assertNotIn(
            "-", self.__parkomatApp.GetView().DataWyjazduZParkingu)
        # Zatwierdzam, komunikat - czas wyjazdu pół godziny po aktualnym czasie
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_6(self):
        """
        6. Wrzucić 200 monet 1gr, oczekiwany termin wyjazdu godzinę po aktualnym czasie.
        """
        self.__parkomatApp.resetData()
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST6"
        self.__parkomatApp.GetView().LiczbaWrzucanychPieniedzy = "200"
        self.__parkomatApp.dodajPieniadze(0.01)
        self.assertEqual(self.__parkomatApp.GetPrzechowywaczMonet().Suma(), 2)
        # Zatwierdzam, komunikat - czas wyjazdu godzina po aktualnym czasie
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_7(self):
        """
        7. Wrzucić 201 monet 1gr, oczekiwana informacja o przepełnieniu parkomatu.
        """
        self.__parkomatApp.resetData()
        self.__parkomatApp.GetView().LiczbaWrzucanychPieniedzy = "201"
        # Zatwierdzam, komunikat - przepełnienie parkomatu
        self.__parkomatApp.dodajPieniadze(0.01)
        self.assertEqual(self.__parkomatApp.GetPrzechowywaczMonet().Suma(), 2)
        self.__parkomatApp.resetData()

    def test_8(self):
        """
        8. Wciśnięcie "Zatwierdź" bez wrzucenia monet -- oczekiwana informacja o błędzie.
        """
        self.__parkomatApp.resetData()
        self.__parkomatApp.GetView().NumerRejestracyjny = "TEST8"
        self.assertIn("-", self.__parkomatApp.GetView().DataWyjazduZParkingu)
        # Zatwierdzam, komunikat - brak wrzuconych pieniędzy
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.resetData()

    def test_9(self):
        """
        9. Wciśnięcie "Zatwierdź" bez wpisania numeru rejestracyjnego -- oczekiwana informacja o błędzie. 
        Wciśnięcie "Zatwierdź" po wpisaniu niepoprawnego numeru rejestracyjnego -- oczekiwana informacja o błędzie. 
        """
        self.__parkomatApp.resetData()
        self.__parkomatApp.dodajPieniadze(10)
        self.assertEqual(self.__parkomatApp.GetView().NumerRejestracyjny, "")
        # Zatwierdzam, komunikat - brak numeru rejestracyjnego
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.__parkomatApp.GetView().NumerRejestracyjny = "test9_nie_poprawny_numer"
        # Zatwierdzam, komunikat - niepoprawnie wpisany numer rejestracyjny
        self.__parkomatApp.zatwierdz("<ButtonRelease>")
        self.assertEqual(self.__parkomatApp.GetView(
        ).NumerRejestracyjny, "test9_nie_poprawny_numer")
        self.__parkomatApp.resetData()


if __name__ == "__main__":
    unittest.main()
