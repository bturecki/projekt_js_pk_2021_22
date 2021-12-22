from decimal import *
getcontext().prec = 2
class Pieniadz:
    
    def __init__(self,wartosc, waluta):
        if isinstance(wartosc, Decimal) == False:
            raise NotImplementedError() #TODO dodać własne exception
        if isinstance(waluta, str) == False:
            raise NotImplementedError() #TODO dodać własne exception
        self.__wartosc = Decimal(wartosc)
        self.__waluta = waluta
            
    def GetWartosc(self):
        return self.__wartosc
        
    def GetWaluta(self):
        return self.__waluta

class Moneta(Pieniadz):
    def __init__(self, wartosc, waluta):
        if wartosc not in [0.01,0.02,0.05,0.1,0.2,0.5,1,2,5]:
            raise NotImplementedError() #TODO dodać własne exception
        elif waluta.upper() is not 'PLN':
            raise NotImplementedError() #TODO dodać własne exception
        else:
            super().__init__(wartosc, waluta)

class Banknot(Pieniadz):
    def __init__(self, wartosc, waluta):
        if wartosc not in [10,20,50,100,500]:
            raise NotImplementedError() #TODO dodać własne exception
        elif waluta.upper() is not 'PLN':
            raise NotImplementedError() #TODO dodać własne exception
        else:
            super().__init__(wartosc, waluta)

class PrzechowywaczPieniedzy:
     __waluta = 'PLN'
     _lista = []

     def DodajMonete(self, pieniadz):
        if isinstance(pieniadz, Pieniadz):
            if pieniadz.GetWaluta() == self.__waluta:
                self.__lista.append(pieniadz)
            else:
                raise NotImplementedError('Nieznana waluta') #TODO dodać własne exception
        else:
            raise NotImplementedError('Przesłany obiekt nie pieniądzem') #TODO dodać własne exception

     def Suma(self):
        s = 0
        for x in self.__lista:
            s = s + x.GetWartosc()
        return Decimal(s)
    
