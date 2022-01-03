from Model.ParkomatExceptions import *

class Pieniadz:
    
    def __init__(self,wartosc, waluta):
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
    def __init__(self, wartosc, waluta):
        if wartosc not in [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]:
            raise ZlyNominalExcepion(wartosc)
        elif waluta.upper() != 'PLN':
            raise NieznanaWalutaException(waluta)
        else:
            super().__init__(wartosc, waluta)

class Banknot(Pieniadz):
    def __init__(self, wartosc, waluta):
        if wartosc not in [10,20,50,100,500]:
            raise ZlyNominalExcepion(wartosc)
        elif waluta.upper() != 'PLN':
            raise NieznanaWalutaException(waluta)
        else:
            super().__init__(wartosc, waluta)

class PrzechowywaczPieniedzy:
     __waluta = 'PLN'
     __lista = []

     def DodajPieniadze(self, pieniadz):
        if isinstance(pieniadz, Pieniadz):
            if isinstance(pieniadz, Moneta):
                if len([p for p in self.__lista if p.GetWartosc() == pieniadz.GetWartosc()]) == 200:
                    return "Automat przepełniony monetami o wartości " + str(pieniadz.GetWartosc()) + " " + pieniadz.GetWaluta() + "! Wrzuć inny nominał."
            if pieniadz.GetWaluta() == self.__waluta:
                self.__lista.append(pieniadz)
            else:
                raise NieznanaWalutaException(pieniadz.GetWaluta())
        else:
            raise ValueError("Przesyłany pieniadz musi byc typu Pieniadz.")

     def Suma(self):
        s = 0
        for x in self.__lista:
            s = s + round(x.GetWartosc(),2)
        return round(s,2)

     def Reset(self):
         self.__lista = []



    
