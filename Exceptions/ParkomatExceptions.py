class ZlyNominalExcepion(Exception):
    """
    Wyjątek jeśli zostanie wrzucona niepoprawna moneta lub banknot (np. moneta 3 gr lub banknot 30 zł)
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class NieznanaWalutaException(Exception):
    """
    Wyjątek jeśli zostanie wrzucona niepoprawna waluta (bankomat obsługuje tylko PLN)
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class PrzepelnionyBankomatException(Exception):
    """
    Wyjątek jeśli bankomat zostanie przepełniony monetami o tym samym nominale.
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value
