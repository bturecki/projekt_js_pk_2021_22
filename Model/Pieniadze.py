from Exceptions.ParkomatExceptions import *


class Pieniadz:
    """
    Bazowa klasa dla różnych rodzajów pieniędzy
    """

    def __init__(self, wartosc, waluta):
        if isinstance(wartosc, float) == False and isinstance(wartosc, int) == False:
            raise ValueError("Wartosc musi byc typu liczbowego.")
        if isinstance(waluta, str) == False:
            raise ValueError("Waluta musi byc typu słownego.")
        self.__wartosc = wartosc
        self.__waluta = waluta

    def GetWartosc(self):
        return self.__wartosc

    def GetWaluta(self):
        return self.__waluta


class Moneta(Pieniadz):
    """
    Rozszerzenie klasy Pieniadz. Obsługuje tylko monety.
    """

    def __init__(self, wartosc, waluta):
        if wartosc not in [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5]:
            raise ZlyNominalExcepion(wartosc)
        elif waluta.upper() != 'PLN':
            raise NieznanaWalutaException(waluta)
        else:
            super().__init__(wartosc, waluta)


class Banknot(Pieniadz):
    """
    Rozszerzenie klasy Pieniadz. Obsługuje tylko banknoty.
    """

    def __init__(self, wartosc, waluta):
        if wartosc not in [10, 20, 50, 100, 500]:
            raise ZlyNominalExcepion(wartosc)
        elif waluta.upper() != 'PLN':
            raise NieznanaWalutaException(waluta)
        else:
            super().__init__(wartosc, waluta)


class PrzechowywaczPieniedzy:
    """
    Klasa do przechowywania wszystkich wrzuconych pieniędzy do parkomatu
    """
    __waluta = 'PLN'
    __lista = []

    def DodajPieniadze(self, pieniadz):
        """
        Dodaje obiekt typu Pieniadz do sumy pieniędzy
        """
        try:
            if isinstance(pieniadz, Pieniadz):
                if isinstance(pieniadz, Moneta):
                    if len([p for p in self.__lista if p.GetWartosc() == pieniadz.GetWartosc()]) == 200:
                        raise PrzepelnionyBankomatException("Automat przepełniony monetami o wartości " + str(
                            pieniadz.GetWartosc()) + " " + pieniadz.GetWaluta() + "! Wrzuć inny nominał.")
                if pieniadz.GetWaluta() == self.__waluta:
                    self.__lista.append(pieniadz)
                else:
                    raise NieznanaWalutaException(pieniadz.GetWaluta())
            else:
                raise ValueError("Przesyłany pieniadz musi byc typu Pieniadz.")
        # Obsługuję tylko ten błąd, ponieważ jest to błąd, który faktycznie może mieć miejsce i jest przewidziany.
        except PrzepelnionyBankomatException as ex:
            return ex
        except:  # Reszta błędów powinna być wyrzucana jako błąd programu.
            raise

    def Suma(self):
        """
        Funkcja zwracająca sumę wrzuconych pieniędzy
        """
        s = 0
        for x in self.__lista:
            s = s + round(x.GetWartosc(), 2)
        return round(s, 2)

    def Reset(self):
        """
        Funkcja resetująca wszystkie dane dotyczące przechowywacza monet
        """
        self.__lista = []
