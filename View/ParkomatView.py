import tkinter as tk

class View():

    def __init__(self, master):
        self.mainWindow = master
        self.mainWindow.title("Parkomat")
        self.mainWindow.geometry("301x380")
        self.mainWindow.wm_iconbitmap('Resources/IkonaParkomat.ico')
        self.mainWindow.eval('tk::PlaceWindow . center')
        #Pole tekstowe na numer rejestracyjny pojazdu
        self.mainWindow.labelNumerRejestracyjny = tk.Label(self.mainWindow, text="Numer rejestracyjny: ", width=20).grid(row=0, column=0)
        self.mainWindow.entryNumerRejestracyjny = tk.Entry(self.mainWindow, width=20)
        self.mainWindow.entryNumerRejestracyjny.grid(row=0, column=1)
        #Aktualna data
        self.mainWindow.labelAktualnaDataLbl = tk.Label(self.mainWindow, text="Aktualna data: ", width=20).grid(row=1, column=0)
        self.mainWindow.labelAktualnaData = tk.Label(self.mainWindow, width=20)
        self.mainWindow.labelAktualnaData.grid(row=1, column=1)

        #Suma wrzuconych pieniędzy
        self.mainWindow.labelAktualnieWrzucona = tk.Label(self.mainWindow, text="Aktualnie wrzucona suma: ", width=20).grid(row=2, column=0)
        self.mainWindow.labelWrzucono = tk.Label(self.mainWindow, width=20)
        self.mainWindow.labelWrzucono.grid(row=2, column=1)

        #Data wyjazdu z parkingu
        self.mainWindow.labelDataWyjazdu = tk.Label(self.mainWindow, text="Data wyjazdu z parkingu : ", width=20).grid(row=3, column=0)
        self.mainWindow.labelDataWyjazduZParkingu = tk.Label(self.mainWindow, width=20)
        self.mainWindow.labelDataWyjazduZParkingu.grid(row=3, column=1)
        self.mainWindow.labelDataWyjazduZParkingu.config(text = "---------------------")

        #Przyciski z pieniędzmi
        self.mainWindow.empty1 = tk.Label(self.mainWindow, text=" ").grid(row=4)
        self.mainWindow.button1gr = tk.Button(self.mainWindow, text = "1gr", width=20)
        self.mainWindow.button1gr.grid(row=5, column=0)
        self.mainWindow.button2gr = tk.Button(self.mainWindow, text = "2gr", width=20)
        self.mainWindow.button2gr.grid(row=6, column=0)
        self.mainWindow.button5gr = tk.Button(self.mainWindow, text = "5gr", width=20)
        self.mainWindow.button5gr.grid(row=7, column=0)
        self.mainWindow.button10gr = tk.Button(self.mainWindow, text = "10gr", width=20)
        self.mainWindow.button10gr.grid(row=8, column=0)
        self.mainWindow.button20gr = tk.Button(self.mainWindow, text = "20gr", width=20)
        self.mainWindow.button20gr.grid(row=9, column=0)
        self.mainWindow.button50gr = tk.Button(self.mainWindow, text = "50gr", width=20)
        self.mainWindow.button50gr.grid(row=10, column=0)
        self.mainWindow.button1zl = tk.Button(self.mainWindow, text = "1zł", width=20)
        self.mainWindow.button1zl.grid(row=5, column=1)
        self.mainWindow.button2zl = tk.Button(self.mainWindow, text = "2zł", width=20)
        self.mainWindow.button2zl.grid(row=6, column=1)
        self.mainWindow.button5zl = tk.Button(self.mainWindow, text = "5zł", width=20)
        self.mainWindow.button5zl.grid(row=7, column=1)
        self.mainWindow.button10zl = tk.Button(self.mainWindow, text = "10zł", width=20)
        self.mainWindow.button10zl.grid(row=8, column=1)
        self.mainWindow.button20zl = tk.Button(self.mainWindow, text = "20zł", width=20)
        self.mainWindow.button20zl.grid(row=9, column=1)
        self.mainWindow.button50zl = tk.Button(self.mainWindow, text = "50zł", width=20)
        self.mainWindow.button50zl.grid(row=10, column=1)

        #Pole pozwalające wpisać liczbę wrzucanych pieniędzy
        self.mainWindow.empty2 = tk.Label(self.mainWindow, text=" ").grid(row=11)
        self.mainWindow.labelLiczbaWrzucanych = tk.Label(self.mainWindow, text="Liczba wrzucanych: ", width=20).grid(row=12, column=0)
        self.mainWindow.entryLiczbaWrzucanychPieniedzy = tk.Entry(self.mainWindow, width=20)
        self.mainWindow.entryLiczbaWrzucanychPieniedzy.grid(row=12, column=1)

        #Przycisk zatwierdź
        self.mainWindow.empty3 = tk.Label(self.mainWindow, text=" ").grid(row=13)
        self.mainWindow.buttonZatwierdz = tk.Button(self.mainWindow, text = "Zatwierdź", width=40)
        self.mainWindow.buttonZatwierdz.grid(row=14, column=0, columnspan = 2)

        #Zmiana aktualnej godziny
        self.mainWindow.empty4 = tk.Label(self.mainWindow, text=" ").grid(row=13)
        self.mainWindow.buttonZmianaAktualnejGodziny = tk.Button(self.mainWindow, text = "Zmiana aktualnej godziny", width=40)
        self.mainWindow.buttonZmianaAktualnejGodziny.grid(row=15, column=0, columnspan=2)
    
