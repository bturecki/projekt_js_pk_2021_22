import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from View.DateSelectionView import DateSelectorView


class DateSelectorController():
    """
    Klasa obsługująca logikę zmiany daty z poziomu GUI
    """

    def zmianaAktualnejGodzinyClose(self):
        _godziny = int(
            self.__view.Godzina) if self.__view.Godzina.isdigit() else None
        _minuty = int(
            self.__view.Minuta) if self.__view.Minuta.isdigit() else None
        _sekundy = int(
            self.__view.Sekunda) if self.__view.Sekunda.isdigit() else None
        if(_godziny is None or _godziny < 0 or _godziny > 23 or _minuty is None or _minuty < 0 or _minuty > 60 or _sekundy is None or _sekundy < 0 or _sekundy > 60):
            messagebox.showerror(
                "Błąd", "Ustawiona data jest niepoprawna. Spróbuj ponownie.")
        else:
            self.__parent.setAktualnaData((datetime.strptime(self.__view.Data.strftime(
                '%d.%m.%Y'), '%d.%m.%Y') + timedelta(hours=_godziny, minutes=_minuty, seconds=_sekundy)).strftime('%d.%m.%Y %H:%M'))
            self.__root.destroy()

    def __init__(self, parent):
        self.__root = tk.Toplevel()
        self.__parent = parent
        self.__view = DateSelectorView(self.__root)
        self.__view.BindButtonOk(self.zmianaAktualnejGodzinyClose)

    def run(self):
        """
        Uruchamia główną pętle okna
        """
        self.__root.wait_window(self.__root)

    def GetView(self):
        """
        Funkcja zwracająca instancje widoku. Tylko do testów jednostkowych.
        """
        return self.__view
