import tkinter as tk
from datetime import datetime


class View():
    """
    Główny widok parkomatu
    """

    def __init__(self, master):
        self.__mainWindow = master
        self.__mainWindow.title("Parkomat")
        self.__mainWindow.geometry("301x380")
        self.__mainWindow.wm_iconbitmap('Resources/IkonaParkomat.ico')
        self.__mainWindow.eval('tk::PlaceWindow . center')
        # Pole tekstowe na numer rejestracyjny pojazdu
        self.__mainWindow.__labelNumerRejestracyjny = tk.Label(
            self.__mainWindow, text="Numer rejestracyjny: ", width=20).grid(row=0, column=0)
        self.__mainWindow.__entryNumerRejestracyjny = tk.Entry(
            self.__mainWindow, width=20)
        self.__mainWindow.__entryNumerRejestracyjny.grid(row=0, column=1)
        # Aktualna data
        self.__mainWindow.__labelAktualnaDataLbl = tk.Label(
            self.__mainWindow, text="Aktualna data: ", width=20).grid(row=1, column=0)
        self.__mainWindow.__labelAktualnaData = tk.Label(
            self.__mainWindow, width=20)
        self.__mainWindow.__labelAktualnaData.grid(row=1, column=1)

        # Suma wrzuconych pieniędzy
        self.__mainWindow.__labelAktualnieWrzucona = tk.Label(
            self.__mainWindow, text="Aktualnie wrzucona suma: ", width=20).grid(row=2, column=0)
        self.__mainWindow.__labelWrzucono = tk.Label(
            self.__mainWindow, width=20)
        self.__mainWindow.__labelWrzucono.grid(row=2, column=1)

        # Data wyjazdu z parkingu
        self.__mainWindow.__labelDataWyjazdu = tk.Label(
            self.__mainWindow, text="Data wyjazdu z parkingu : ", width=20).grid(row=3, column=0)
        self.__mainWindow.__labelDataWyjazduZParkingu = tk.Label(
            self.__mainWindow, width=20)
        self.__mainWindow.__labelDataWyjazduZParkingu.grid(row=3, column=1)

        # Przyciski z pieniędzmi
        self.__mainWindow.__empty1 = tk.Label(
            self.__mainWindow, text=" ").grid(row=4)
        self.__mainWindow.__button1gr = tk.Button(
            self.__mainWindow, text="1gr", width=20)
        self.__mainWindow.__button1gr.grid(row=5, column=0)
        self.__mainWindow.__button2gr = tk.Button(
            self.__mainWindow, text="2gr", width=20)
        self.__mainWindow.__button2gr.grid(row=6, column=0)
        self.__mainWindow.__button5gr = tk.Button(
            self.__mainWindow, text="5gr", width=20)
        self.__mainWindow.__button5gr.grid(row=7, column=0)
        self.__mainWindow.__button10gr = tk.Button(
            self.__mainWindow, text="10gr", width=20)
        self.__mainWindow.__button10gr.grid(row=8, column=0)
        self.__mainWindow.__button20gr = tk.Button(
            self.__mainWindow, text="20gr", width=20)
        self.__mainWindow.__button20gr.grid(row=9, column=0)
        self.__mainWindow.__button50gr = tk.Button(
            self.__mainWindow, text="50gr", width=20)
        self.__mainWindow.__button50gr.grid(row=10, column=0)
        self.__mainWindow.__button1zl = tk.Button(
            self.__mainWindow, text="1zł", width=20)
        self.__mainWindow.__button1zl.grid(row=5, column=1)
        self.__mainWindow.__button2zl = tk.Button(
            self.__mainWindow, text="2zł", width=20)
        self.__mainWindow.__button2zl.grid(row=6, column=1)
        self.__mainWindow.__button5zl = tk.Button(
            self.__mainWindow, text="5zł", width=20)
        self.__mainWindow.__button5zl.grid(row=7, column=1)
        self.__mainWindow.__button10zl = tk.Button(
            self.__mainWindow, text="10zł", width=20)
        self.__mainWindow.__button10zl.grid(row=8, column=1)
        self.__mainWindow.__button20zl = tk.Button(
            self.__mainWindow, text="20zł", width=20)
        self.__mainWindow.__button20zl.grid(row=9, column=1)
        self.__mainWindow.__button50zl = tk.Button(
            self.__mainWindow, text="50zł", width=20)
        self.__mainWindow.__button50zl.grid(row=10, column=1)

        # Pole pozwalające wpisać liczbę wrzucanych pieniędzy
        self.__mainWindow.__empty2 = tk.Label(
            self.__mainWindow, text=" ").grid(row=11)
        self.__mainWindow.__labelLiczbaWrzucanych = tk.Label(
            self.__mainWindow, text="Liczba wrzucanych: ", width=20).grid(row=12, column=0)
        self.__mainWindow.__entryLiczbaWrzucanychPieniedzy = tk.Entry(
            self.__mainWindow, width=20)
        self.__mainWindow.__entryLiczbaWrzucanychPieniedzy.grid(
            row=12, column=1)

        # Przycisk zatwierdź
        self.__mainWindow.__empty3 = tk.Label(
            self.__mainWindow, text=" ").grid(row=13)
        self.__mainWindow.__buttonZatwierdz = tk.Button(
            self.__mainWindow, text="Zatwierdź", width=40)
        self.__mainWindow.__buttonZatwierdz.grid(
            row=14, column=0, columnspan=2)

        # Zmiana aktualnej godziny
        self.__mainWindow.__empty4 = tk.Label(
            self.__mainWindow, text=" ").grid(row=13)
        self.__mainWindow.__buttonZmianaAktualnejGodziny = tk.Button(
            self.__mainWindow, text="Zmiana aktualnej daty i godziny", width=40)
        self.__mainWindow.__buttonZmianaAktualnejGodziny.grid(
            row=15, column=0, columnspan=2)

    @property
    def NumerRejestracyjny(self):
        return self.__mainWindow.__entryNumerRejestracyjny.get()

    @NumerRejestracyjny.setter
    def NumerRejestracyjny(self, text):
        self.__mainWindow.__entryNumerRejestracyjny.delete(0, tk.END)
        self.__mainWindow.__entryNumerRejestracyjny.insert(0, text)

    @property
    def AktualnaData(self) -> datetime:
        return datetime.strptime(self.__mainWindow.__labelAktualnaData.cget("text"), '%d.%m.%Y %H:%M')

    @AktualnaData.setter
    def AktualnaData(self, text):
        self.__mainWindow.__labelAktualnaData.config(text=text)

    def SetAktualnaDataTimerEvent(self, time, event):
        self.__mainWindow.__labelAktualnaData.after(time, event)

    @property
    def LiczbaWrzucanychPieniedzy(self):
        return self.__mainWindow.__entryLiczbaWrzucanychPieniedzy.get()

    @LiczbaWrzucanychPieniedzy.setter
    def LiczbaWrzucanychPieniedzy(self, text):
        self.__mainWindow.__entryLiczbaWrzucanychPieniedzy.delete(0, tk.END)
        self.__mainWindow.__entryLiczbaWrzucanychPieniedzy.insert(0, text)

    @property
    def Wrzucono(self):
        return self.__mainWindow.__labelWrzucono.cget("text"),

    @Wrzucono.setter
    def Wrzucono(self, text):
        self.__mainWindow.__labelWrzucono.config(text=text)

    @property
    def DataWyjazduZParkingu(self):
        return self.__mainWindow.__labelDataWyjazduZParkingu.cget("text")

    @DataWyjazduZParkingu.setter
    def DataWyjazduZParkingu(self, text):
        self.__mainWindow.__labelDataWyjazduZParkingu.config(text=text)

    def ResetDataWyjazduZParkingu(self):
        self.__mainWindow.__labelDataWyjazduZParkingu.config(
            text="---------------------")

    def BindButtonZatwierdz(self, f):
        self.__mainWindow.__buttonZatwierdz.bind("<Button>", f)

    def BindButtonZmianaAktualnejGodziny(self, f):
        self.__mainWindow.__buttonZmianaAktualnejGodziny.bind("<Button>", f)

    def BindButton1gr(self, f):
        self.__mainWindow.__button1gr.bind(
            "<Button>", lambda event, wartosc=0.01: f(wartosc))

    def BindButton2gr(self, f):
        self.__mainWindow.__button2gr.bind(
            "<Button>", lambda event, wartosc=0.02: f(wartosc))

    def BindButton5gr(self, f):
        self.__mainWindow.__button5gr.bind(
            "<Button>", lambda event, wartosc=0.05: f(wartosc))

    def BindButton10gr(self, f):
        self.__mainWindow.__button10gr.bind(
            "<Button>", lambda event, wartosc=0.10: f(wartosc))

    def BindButton20gr(self, f):
        self.__mainWindow.__button20gr.bind(
            "<Button>", lambda event, wartosc=0.20: f(wartosc))

    def BindButton50gr(self, f):
        self.__mainWindow.__button50gr.bind(
            "<Button>", lambda event, wartosc=0.50: f(wartosc))

    def BindButton1zl(self, f):
        self.__mainWindow.__button1zl.bind(
            "<Button>", lambda event, wartosc=1: f(wartosc))

    def BindButton2zl(self, f):
        self.__mainWindow.__button2zl.bind(
            "<Button>", lambda event, wartosc=2: f(wartosc))

    def BindButton5zl(self, f):
        self.__mainWindow.__button5zl.bind(
            "<Button>", lambda event, wartosc=5: f(wartosc))

    def BindButton10zl(self, f):
        self.__mainWindow.__button10zl.bind(
            "<Button>", lambda event, wartosc=10: f(wartosc))

    def BindButton20zl(self, f):
        self.__mainWindow.__button20zl.bind(
            "<Button>", lambda event, wartosc=20: f(wartosc))

    def BindButton50zl(self, f):
        self.__mainWindow.__button50zl.bind(
            "<Button>", lambda event, wartosc=50: f(wartosc))
