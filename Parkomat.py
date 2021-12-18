#Import biblioteki do tworzenia GUI
from tkinter import *
from tkinter import messagebox
import time
def dodajMonete1gr(wartosc):
    messagebox.showinfo("Test", wartosc)

#Funkcja odpowiadająca za aktualizacje czasu
def clock():
    labelAktualnaData.config(text = time.strftime("%d") + "." + time.strftime("%m") + "." + time.strftime("%Y") + " " + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
    labelAktualnaData.after(1000, clock)

#Tworzenie instancji okna tkinter
mainWindow = Tk()

#Ustawienia okna
mainWindow.title("Parkomat")
mainWindow.geometry("301x300")
mainWindow.eval('tk::PlaceWindow . center')

#Pole tekstowe na numer rejestracyjny pojazdu
Label(mainWindow, text="Numer rejestracyjny: ", width=20).grid(row=0, column=0)
entryNumerRejestracyjny = Entry(mainWindow, width=20)
entryNumerRejestracyjny.grid(row=0, column=1)
#Aktualna data
Label(mainWindow, text="Aktualna data: ", width=20).grid(row=1, column=0)
labelAktualnaData = Label(mainWindow, width=20)
labelAktualnaData.grid(row=1, column=1)
#Data wyjazdu z parkingu
Label(mainWindow, text="Data wyjazdu z parkingu : ", width=20).grid(row=2, column=0)
labelDataWyjazduZParkingu = Label(mainWindow, width=20)
labelDataWyjazduZParkingu.grid(row=2, column=1)
#Przyciski z monetami
Label(mainWindow, text=" ").grid(row=3)
button1gr = Button(mainWindow, text = "1gr", width=20, command= lambda: dodajMonete1gr(0.01))
button1gr.grid(row=4, column=0)
button2gr = Button(mainWindow, text = "2gr", width=20, command= lambda: dodajMonete1gr(0.0))
button2gr.grid(row=5, column=0)
button5gr = Button(mainWindow, text = "5gr", width=20, command= lambda: dodajMonete1gr(0.05))
button5gr.grid(row=6, column=0)
button10gr = Button(mainWindow, text = "10gr", width=20, command= lambda: dodajMonete1gr(0.10))
button10gr.grid(row=7, column=0)
button20gr = Button(mainWindow, text = "20gr", width=20, command= lambda: dodajMonete1gr(0.20))
button20gr.grid(row=8, column=0)
button50gr = Button(mainWindow, text = "50gr", width=20, command= lambda: dodajMonete1gr(0.50))
button50gr.grid(row=9, column=0)
button1zl = Button(mainWindow, text = "1zł", width=20, command= lambda: dodajMonete1gr(1))
button1zl.grid(row=4, column=1)
button2zl = Button(mainWindow, text = "2zł", width=20, command= lambda: dodajMonete1gr(2))
button2zl.grid(row=5, column=1)
button5zl = Button(mainWindow, text = "5zł", width=20, command= lambda: dodajMonete1gr(5))
button5zl.grid(row=6, column=1)
button10zl = Button(mainWindow, text = "10zł", width=20, command= lambda: dodajMonete1gr(10))
button10zl.grid(row=7, column=1)
button20zl = Button(mainWindow, text = "20zł", width=20, command= lambda: dodajMonete1gr(20))
button20zl.grid(row=8, column=1)
button50zl = Button(mainWindow, text = "50zł", width=20, command= lambda: dodajMonete1gr(50))
button50zl.grid(row=9, column=1)
#Pole pozwalające wpisać liczbę wrzucanych monet
Label(mainWindow, text=" ").grid(row=10)
Label(mainWindow, text="Liczba wrzucanych monet : ", width=20).grid(row=11, column=0)
entryLiczbaWrzuconychMonet = Entry(mainWindow, width=20)
entryLiczbaWrzuconychMonet.grid(row=11, column=1)
#Przycisk zatwierdź
Label(mainWindow, text=" ").grid(row=12)
buttonZatwierdz = Button(mainWindow, text = "Zatwierdź", width=40)
buttonZatwierdz.grid(row=13, column=0, columnspan = 2)

clock()


#Pętla odpowiadająca za działanie głównego okna
mainWindow.mainloop()