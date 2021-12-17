#Import biblioteki do tworzenia GUI
from tkinter import *
from tkinter import messagebox

def dodajMonete1gr(wartosc):
    messagebox.showinfo("Test", wartosc)

#Tworzenie instancji okna tkinter
mainWindow = Tk()

#Ustawienia okna
mainWindow.title("Parkomat")
mainWindow.geometry("301x300")
mainWindow.eval('tk::PlaceWindow . center')

#Pole tekstowe na numer rejestracyjny pojazdu
Label(mainWindow, text="Numer rejestracyjny: ", width=20).grid(row=0, column=0)
entryNumerRejestracyjny = Entry(mainWindow, width=20).grid(row=0, column=1)
#Aktualna data
Label(mainWindow, text="Aktualna data: ", width=20).grid(row=1, column=0)
entryAktualnaData = Entry(mainWindow, state=DISABLED, width=20).grid(row=1, column=1)
#Data wyjazdu z parkingu
Label(mainWindow, text="Data wyjazdu z parkingu : ", width=20).grid(row=2, column=0)
entryDataWyjazduZParkingu = Entry(mainWindow, state=DISABLED, width=20).grid(row=2, column=1)
#Przyciski z monetami
Label(mainWindow, text=" ").grid(row=3)
button1gr = Button(mainWindow, text = "1gr", width=20, command= lambda: dodajMonete1gr(0.01)).grid(row=4, column=0)
button2gr = Button(mainWindow, text = "2gr", width=20, command= lambda: dodajMonete1gr(0.0)).grid(row=5, column=0)
button5gr = Button(mainWindow, text = "5gr", width=20, command= lambda: dodajMonete1gr(0.05)).grid(row=6, column=0)
button10gr = Button(mainWindow, text = "10gr", width=20, command= lambda: dodajMonete1gr(0.10)).grid(row=7, column=0)
button20gr = Button(mainWindow, text = "20gr", width=20, command= lambda: dodajMonete1gr(0.20)).grid(row=8, column=0)
button50gr = Button(mainWindow, text = "50gr", width=20, command= lambda: dodajMonete1gr(0.50)).grid(row=9, column=0)
button1zl = Button(mainWindow, text = "1zł", width=20, command= lambda: dodajMonete1gr(1)).grid(row=4, column=1)
button2zl = Button(mainWindow, text = "2zł", width=20, command= lambda: dodajMonete1gr(2)).grid(row=5, column=1)
button5zl = Button(mainWindow, text = "5zł", width=20, command= lambda: dodajMonete1gr(5)).grid(row=6, column=1)
button10zl = Button(mainWindow, text = "10zł", width=20, command= lambda: dodajMonete1gr(10)).grid(row=7, column=1)
button20zl = Button(mainWindow, text = "20zł", width=20, command= lambda: dodajMonete1gr(20)).grid(row=8, column=1)
button50zl = Button(mainWindow, text = "50zł", width=20, command= lambda: dodajMonete1gr(50)).grid(row=9, column=1)
#Pole pozwalające wpisać liczbę wrzucanych monet
Label(mainWindow, text=" ").grid(row=10)
Label(mainWindow, text="Liczba wrzucanych monet : ", width=20).grid(row=11, column=0)
entryLiczbaWrzuconychMonet = Entry(mainWindow, width=20).grid(row=11, column=1)
#Przycisk zatwierdź
Label(mainWindow, text=" ").grid(row=12)
buttonZatwierdz = Button(mainWindow, text = "Zatwierdź", width=40).grid(row=13, column=0, columnspan = 2)
#Pętla odpowiadająca za działanie głównego okna
mainWindow.mainloop()