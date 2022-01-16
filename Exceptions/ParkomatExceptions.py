class ZlyNominalExcepion(Exception):
    """
    Wyjątek jeśli zostanie wrzucona niepoprawna moneta lub banknot (np. moneta 3 gr lub banknot 30 zł)
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NieznanaWalutaException(Exception):
    """
    Wyjątek jeśli zostanie wrzucona niepoprawna waluta (bankomat obsługuje tylko PLN)
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return repr(self.value)


class BrakDatyWyjazduException(Exception):
    """
    Wyjątek jeśli data wyjazdu nie zostanie poprawnie obliczona
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PrzepelnionyBankomatException(Exception):
    """
    Wyjątek jeśli bankomat zostanie przepełniony monetami o tym samym nominale.
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value

class NiepoprawnieUstawionaDataException(Exception):
    """
    Wyjątek jeśli użytkownik wprowadzi niepoprawnie datę lub godzinę podczas zmiany aktualnej daty.
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value

class BrakNumeruRejestracyjnegoException(Exception):
    """
    Wyjątek jeśli użytkownik nie wprowadzi numeru rejestracyjnego.
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value

class NiepoprawnieUstawionyNumerRejestracyjnyException(Exception):
    """
    Wyjątek jeśli użytkownik wprowadzi niepoprawnie ustawiony numer rejestracyjny.
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value

class BrakPieniedzyException(Exception):
    """
    Wyjątek jeśli użytkownik nie wprowadzi żadnych pieniędzy.
    """

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return self.value