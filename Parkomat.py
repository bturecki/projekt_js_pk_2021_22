from tkinter import *
from tkinter import messagebox
import time
from tkcalendar import Calendar, DateEntry
from datetime import datetime, timedelta

def resetZmienneGlobalne():
    global sumaWrzuconychMonet
    sumaWrzuconychMonet = 0

    global zmianaAktualnejDaty
    zmianaAktualnejDaty = ''

def zatwierdz():
    """
    Funkcja weryfikująca, zatwierdzająca oraz resetująca dane
    """
    global sumaWrzuconychMonet
    if len(entryNumerRejestracyjny.get()) < 1 or len(entryNumerRejestracyjny.get()) > 7:
            messagebox.showerror("Błąd", "Wpisano niepoprawny numer rejestracyjny pojazdu.")
    elif sumaWrzuconychMonet == 0:
            messagebox.showerror("Błąd", "Nie wrzucono żadnych monet.")
    else:
        messagebox.showinfo("Info", "Zatwierdzono.")
        resetZmienneGlobalne()
        setEntryText(entryLiczbaWrzucanychMonet, "1")
        setEntryText(entryNumerRejestracyjny, "")



def zmianaAktualnejGodziny():
    """
    Funkcja otwierająca okno służące do wyboru niestandardowej daty oraz godziny
    """
    wybranaData = None
    windowZmianaAktualnejGodziny = Toplevel()
    windowZmianaAktualnejGodziny.title("Zmiana godziny")
    cal = DateEntry(windowZmianaAktualnejGodziny,selectmode='day', background='darkblue', foreground='white', borderwidth=2)
    cal.grid(row=0, column=0)
    entryGodzina = Entry(windowZmianaAktualnejGodziny, width = 2)
    entryGodzina.grid(row=0, column=1)
    Label(windowZmianaAktualnejGodziny, text=":", width=1).grid(row=0, column=2)
    entryMinuta = Entry(windowZmianaAktualnejGodziny, width = 2)
    entryMinuta.grid(row=0, column=3)
    Label(windowZmianaAktualnejGodziny, text=":", width=0).grid(row=0, column=4)
    entrySekunda = Entry(windowZmianaAktualnejGodziny, width = 2)
    entrySekunda.grid(row=0, column=5)

    def zmianaAktualnejGodzinyClose():
        _godziny = int(entryGodzina.get()) if entryGodzina.get().isdigit() else None
        _minuty = int(entryMinuta.get()) if entryMinuta.get().isdigit() else None
        _sekundy = int(entrySekunda.get()) if entrySekunda.get().isdigit() else None
        if(_godziny is None or _godziny < 0 or _godziny > 23 or _minuty is None or _minuty < 0 or _minuty > 60 or _sekundy is None or _sekundy < 0 or _sekundy > 60):
            messagebox.showerror("Błąd", "Ustawiona data jest niepoprawna. Spróbuj ponownie.")
        else:
            _data = (datetime.strptime(cal.get_date().strftime('%d.%m.%y'), '%d.%m.%y') + timedelta(hours=_godziny, minutes=_minuty, seconds= _sekundy)).strftime('%d.%m.%y %H:%M:%S')
            nonlocal wybranaData
            wybranaData = _data
            windowZmianaAktualnejGodziny.destroy()

    buttonOk = Button(windowZmianaAktualnejGodziny, text = "OK", width=2, command= zmianaAktualnejGodzinyClose)
    buttonOk.grid(row=0, column=6)
    setEntryText(entryGodzina, "00")
    setEntryText(entryMinuta, "00")
    setEntryText(entrySekunda, "00")

    windowZmianaAktualnejGodziny.wait_window(windowZmianaAktualnejGodziny)
    
    global zmianaAktualnejDaty
    zmianaAktualnejDaty = wybranaData


def setEntryText(cntrl, text):
    """
    Pomocnik do ustawiania tekstu w kontrolkach typu Entry
    """
    cntrl.delete(0, END)
    cntrl.insert(0,text)

def dodajMonete(wartosc):
    """
    Funkcja do dodania wartości wybranej momnety do sumy
    """
    _liczbaWrzucanychMonet = int(entryLiczbaWrzucanychMonet.get()) if entryLiczbaWrzucanychMonet.get().isdigit() else None
    if _liczbaWrzucanychMonet is None or _liczbaWrzucanychMonet < 1:
        messagebox.showerror("Błąd", "Liczba wrzucanych monet musi być liczbą naturalną dodatnią.")
    else:
        global sumaWrzuconychMonet
        sumaWrzuconychMonet = sumaWrzuconychMonet + _liczbaWrzucanychMonet * wartosc
        messagebox.showinfo("Info", "Aktualnie wrzucono: " + str(sumaWrzuconychMonet))
    setEntryText(entryLiczbaWrzucanychMonet, "1")

def setAktualnyCzas():
    """
    Funkcja odpowiadająca za aktualizacje czasu
    """
    global zmianaAktualnejDaty
    if zmianaAktualnejDaty != '':
        labelAktualnaData.config(text = zmianaAktualnejDaty)
    else:
        labelAktualnaData.config(text = time.strftime("%d") + "." + time.strftime("%m") + "." + time.strftime("%Y") + " " + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
    labelAktualnaData.after(1000, setAktualnyCzas)

#Tworzenie instancji okna tkinter
mainWindow = Tk()

resetZmienneGlobalne()

#Ustawienia okna
mainWindow.title("Parkomat")
mainWindow.geometry("301x360")
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
labelDataWyjazduZParkingu.config(text = "---------------------")
#Przyciski z monetami
Label(mainWindow, text=" ").grid(row=3)
button1gr = Button(mainWindow, text = "1gr", width=20, command= lambda: dodajMonete(0.01))
button1gr.grid(row=4, column=0)
button2gr = Button(mainWindow, text = "2gr", width=20, command= lambda: dodajMonete(0.02))
button2gr.grid(row=5, column=0)
button5gr = Button(mainWindow, text = "5gr", width=20, command= lambda: dodajMonete(0.05))
button5gr.grid(row=6, column=0)
button10gr = Button(mainWindow, text = "10gr", width=20, command= lambda: dodajMonete(0.10))
button10gr.grid(row=7, column=0)
button20gr = Button(mainWindow, text = "20gr", width=20, command= lambda: dodajMonete(0.20))
button20gr.grid(row=8, column=0)
button50gr = Button(mainWindow, text = "50gr", width=20, command= lambda: dodajMonete(0.50))
button50gr.grid(row=9, column=0)
button1zl = Button(mainWindow, text = "1zł", width=20, command= lambda: dodajMonete(1))
button1zl.grid(row=4, column=1)
button2zl = Button(mainWindow, text = "2zł", width=20, command= lambda: dodajMonete(2))
button2zl.grid(row=5, column=1)
button5zl = Button(mainWindow, text = "5zł", width=20, command= lambda: dodajMonete(5))
button5zl.grid(row=6, column=1)
button10zl = Button(mainWindow, text = "10zł", width=20, command= lambda: dodajMonete(10))
button10zl.grid(row=7, column=1)
button20zl = Button(mainWindow, text = "20zł", width=20, command= lambda: dodajMonete(20))
button20zl.grid(row=8, column=1)
button50zl = Button(mainWindow, text = "50zł", width=20, command= lambda: dodajMonete(50))
button50zl.grid(row=9, column=1)
#Pole pozwalające wpisać liczbę wrzucanych monet
Label(mainWindow, text=" ").grid(row=10)
Label(mainWindow, text="Liczba wrzucanych monet : ", width=20).grid(row=11, column=0)
entryLiczbaWrzucanychMonet = Entry(mainWindow, width=20)
entryLiczbaWrzucanychMonet.grid(row=11, column=1)
setEntryText(entryLiczbaWrzucanychMonet, "1")

#Przycisk zatwierdź
Label(mainWindow, text=" ").grid(row=12)
buttonZatwierdz = Button(mainWindow, text = "Zatwierdź", width=40, command=zatwierdz)
buttonZatwierdz.grid(row=13, column=0, columnspan = 2)

#Zmiana aktualnej godziny
Label(mainWindow, text=" ").grid(row=12)
buttonZmianaAktualnejGodziny = Button(mainWindow, text = "Zmiana aktualnej godziny", width=40, command=zmianaAktualnejGodziny)
buttonZmianaAktualnejGodziny.grid(row=14, column=0, columnspan=2)

setAktualnyCzas()

#Pętla odpowiadająca za działanie głównego okna
mainWindow.mainloop()