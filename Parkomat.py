import tkinter as tk
from tkinter import messagebox
import time
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from dateutil.rrule import *  
from Models.Pieniadze import *
import re
import math

def resetData():
    """
    Resetuje wszystkie dane parkometru (np. po opłaceniu resetuje się aby kolejna osoba mogła opłacić swój parking)
    """
    przechowywaczPieniedzy.Reset()
    global zmianaAktualnejDaty
    zmianaAktualnejDaty = ''

def pobierzDateSekundy(start, x):
    """
    Funkcja zwracająca datę wyjazdu na podstawie aktualnej daty oraz liczby sekund,
    która jest aktualnie opłacona jeśli chodzi o parkowanie
    """
    rr = rrule(SECONDLY, byweekday=(MO, TU, WE, TH, FR), byhour=(8,9,10,11,12,13,14,15,16,17,18,19), dtstart=start, interval=x)
    return rr.after(start)

def getSekundyDlaDodanychPieniedzy(suma: int) -> int: #TODO do dokończenia obliczanie daty wyjazdu
    hours = (suma >= 2) * 1 + (suma >= 6) * 1 +max(0, math.floor((suma - 6) / 5))
    return hours * 60 * 60

def getAktualnaData() -> datetime:
    return datetime.strptime(labelAktualnaData.cget("text"),'%d.%m.%Y %H:%M:%S')

def aktualizacjaCzasu():
    """
    Funkcja aktualizujaca czas wyjazdu
    """
    if  przechowywaczPieniedzy.Suma() > 0:
        setlLabelText(labelDataWyjazduZParkingu,pobierzDateSekundy(getAktualnaData(), getSekundyDlaDodanychPieniedzy(przechowywaczPieniedzy.Suma())).strftime('%d.%m.%Y %H:%M:%S')) #TODO do dokończenia obliczanie daty wyjazdu
    else:
        labelDataWyjazduZParkingu.config(text = "---------------------")

def setlLabelText(cntrl, text):
    """
    Pomocnik do ustawiania tekstu w kontrolkach typu Label
    """
    cntrl.config(text=text)

def zatwierdz():
    """
    Funkcja weryfikująca, zatwierdzająca oraz resetująca dane
    """
    if entryNumerRejestracyjny.get() is None or entryNumerRejestracyjny.get() == "":
            messagebox.showerror("Błąd", "Nie wpisano numeru rejestracyjnego pojazdu.")
    elif bool(re.match('^[A-Z0-9]*$', entryNumerRejestracyjny.get())) == False:
            messagebox.showerror("Błąd", "Numer rejestracyjny może składać się tylko z wielkich liter od A do Z i cyfr.")
    elif przechowywaczPieniedzy.Suma() == 0:
            messagebox.showerror("Błąd", "Nie wrzucono żadnych pieniędzy.")
    else:
        messagebox.showinfo("Info", "Parking opłacony. Numer rejestracyjny: " + entryNumerRejestracyjny.get() + ", czas zakupu: " + labelAktualnaData.cget("text") + ", termin wyjazdu: " + labelDataWyjazduZParkingu.cget("text"))
        resetData()
        setEntryText(entryLiczbaWrzucanychPieniedzy, "1")
        setEntryText(entryNumerRejestracyjny, "")
        setlLabelText(labelWrzucono,str(przechowywaczPieniedzy.Suma())+" zł")

def zmianaAktualnejGodziny():
    """
    Funkcja otwierająca okno służące do wyboru niestandardowej daty oraz godziny
    """
    wybranaData = None
    windowZmianaAktualnejGodziny = tk.Toplevel()
    windowZmianaAktualnejGodziny.title("Zmiana godziny")
    cal = DateEntry(windowZmianaAktualnejGodziny,selectmode='day', background='darkblue', foreground='white', borderwidth=2)
    cal.grid(row=0, column=0)
    entryGodzina = tk.Entry(windowZmianaAktualnejGodziny, width = 2)
    entryGodzina.grid(row=0, column=1)
    tk.Label(windowZmianaAktualnejGodziny, text=":", width=1).grid(row=0, column=2)
    entryMinuta = tk.Entry(windowZmianaAktualnejGodziny, width = 2)
    entryMinuta.grid(row=0, column=3)
    tk.Label(windowZmianaAktualnejGodziny, text=":", width=0).grid(row=0, column=4)
    entrySekunda = tk.Entry(windowZmianaAktualnejGodziny, width = 2)
    entrySekunda.grid(row=0, column=5)

    def zmianaAktualnejGodzinyClose():
        _godziny = int(entryGodzina.get()) if entryGodzina.get().isdigit() else None
        _minuty = int(entryMinuta.get()) if entryMinuta.get().isdigit() else None
        _sekundy = int(entrySekunda.get()) if entrySekunda.get().isdigit() else None
        if(_godziny is None or _godziny < 0 or _godziny > 23 or _minuty is None or _minuty < 0 or _minuty > 60 or _sekundy is None or _sekundy < 0 or _sekundy > 60):
            messagebox.showerror("Błąd", "Ustawiona data jest niepoprawna. Spróbuj ponownie.")
        else:
            _data = (datetime.strptime(cal.get_date().strftime('%d.%m.%Y'), '%d.%m.%Y') + timedelta(hours=_godziny, minutes=_minuty, seconds= _sekundy)).strftime('%d.%m.%Y %H:%M:%S')
            nonlocal wybranaData
            wybranaData = _data
            windowZmianaAktualnejGodziny.destroy()

    buttonOk = tk.Button(windowZmianaAktualnejGodziny, text = "OK", width=2, command= zmianaAktualnejGodzinyClose)
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
    cntrl.delete(0, tk.END)
    cntrl.insert(0,text)

def dodajPieniadze(wartosc, waluta = 'PLN'):
    """
    Funkcja do dodania wartości wybranej momnety do sumy
    """
    _liczbaWrzucanychPieniedzy = int(entryLiczbaWrzucanychPieniedzy.get()) if entryLiczbaWrzucanychPieniedzy.get().isdigit() else None
    if _liczbaWrzucanychPieniedzy is None or _liczbaWrzucanychPieniedzy < 1:
        messagebox.showerror("Błąd", "Liczba wrzucanych pieniędzy musi być liczbą naturalną dodatnią.")
    else:
        for x in range(_liczbaWrzucanychPieniedzy):
            result = przechowywaczPieniedzy.DodajPieniadze(Moneta(wartosc, waluta) if wartosc < 10 else Banknot(wartosc, waluta))
            if result != None:
                messagebox.showerror("Błąd", result)
                break
        setlLabelText(labelWrzucono,str(przechowywaczPieniedzy.Suma())+" zł")
        aktualizacjaCzasu()
    setEntryText(entryLiczbaWrzucanychPieniedzy, "1")


def setAktualnyCzas():
    """
    Funkcja odpowiadająca za aktualizacje czasu
    """
    global zmianaAktualnejDaty
    if zmianaAktualnejDaty != '':
        labelAktualnaData.config(text = zmianaAktualnejDaty)
    else:
        labelAktualnaData.config(text = time.strftime("%d") + "." + time.strftime("%m") + "." + time.strftime("%Y") + " " + time.strftime("%H") + ":" + time.strftime("%M") + ":" + time.strftime("%S"))
    
    aktualizacjaCzasu()
    labelAktualnaData.after(1000, setAktualnyCzas)

#Tworzenie instancji okna tkinter
mainWindow = tk.Tk()

przechowywaczPieniedzy = PrzechowywaczPieniedzy()
resetData()

#Ustawienia okna
mainWindow.title("Parkomat")
mainWindow.geometry("301x380")
mainWindow.eval('tk::PlaceWindow . center')

#Pole tekstowe na numer rejestracyjny pojazdu
tk.Label(mainWindow, text="Numer rejestracyjny: ", width=20).grid(row=0, column=0)
entryNumerRejestracyjny = tk.Entry(mainWindow, width=20)
entryNumerRejestracyjny.grid(row=0, column=1)
#Aktualna data
tk.Label(mainWindow, text="Aktualna data: ", width=20).grid(row=1, column=0)
labelAktualnaData = tk.Label(mainWindow, width=20)
labelAktualnaData.grid(row=1, column=1)

#Suma wrzuconych pieniędzy
tk.Label(mainWindow, text="Aktualnie wrzucona suma: ", width=20).grid(row=2, column=0)
labelWrzucono = tk.Label(mainWindow, width=20)
labelWrzucono.grid(row=2, column=1)

#Data wyjazdu z parkingu
tk.Label(mainWindow, text="Data wyjazdu z parkingu : ", width=20).grid(row=3, column=0)
labelDataWyjazduZParkingu = tk.Label(mainWindow, width=20)
labelDataWyjazduZParkingu.grid(row=3, column=1)
labelDataWyjazduZParkingu.config(text = "---------------------")
#Przyciski z pieniędzmi
tk.Label(mainWindow, text=" ").grid(row=4)
button1gr = tk.Button(mainWindow, text = "1gr", width=20, command= lambda: dodajPieniadze(0.01))
button1gr.grid(row=5, column=0)
button2gr = tk.Button(mainWindow, text = "2gr", width=20, command= lambda: dodajPieniadze(0.02))
button2gr.grid(row=6, column=0)
button5gr = tk.Button(mainWindow, text = "5gr", width=20, command= lambda: dodajPieniadze(0.05))
button5gr.grid(row=7, column=0)
button10gr = tk.Button(mainWindow, text = "10gr", width=20, command= lambda: dodajPieniadze(0.10))
button10gr.grid(row=8, column=0)
button20gr = tk.Button(mainWindow, text = "20gr", width=20, command= lambda: dodajPieniadze(0.20))
button20gr.grid(row=9, column=0)
button50gr = tk.Button(mainWindow, text = "50gr", width=20, command= lambda: dodajPieniadze(0.50))
button50gr.grid(row=10, column=0)
button1zl = tk.Button(mainWindow, text = "1zł", width=20, command= lambda: dodajPieniadze(1))
button1zl.grid(row=5, column=1)
button2zl = tk.Button(mainWindow, text = "2zł", width=20, command= lambda: dodajPieniadze(2))
button2zl.grid(row=6, column=1)
button5zl = tk.Button(mainWindow, text = "5zł", width=20, command= lambda: dodajPieniadze(5))
button5zl.grid(row=7, column=1)
button10zl = tk.Button(mainWindow, text = "10zł", width=20, command= lambda: dodajPieniadze(10))
button10zl.grid(row=8, column=1)
button20zl = tk.Button(mainWindow, text = "20zł", width=20, command= lambda: dodajPieniadze(20))
button20zl.grid(row=9, column=1)
button50zl = tk.Button(mainWindow, text = "50zł", width=20, command= lambda: dodajPieniadze(50))
button50zl.grid(row=10, column=1)
#Pole pozwalające wpisać liczbę wrzucanych pieniędzy
tk.Label(mainWindow, text=" ").grid(row=11)
tk.Label(mainWindow, text="Liczba wrzucanych: ", width=20).grid(row=12, column=0)
entryLiczbaWrzucanychPieniedzy = tk.Entry(mainWindow, width=20)
entryLiczbaWrzucanychPieniedzy.grid(row=12, column=1)
setEntryText(entryLiczbaWrzucanychPieniedzy, "1")

#Przycisk zatwierdź
tk.Label(mainWindow, text=" ").grid(row=13)
buttonZatwierdz = tk.Button(mainWindow, text = "Zatwierdź", width=40, command=zatwierdz)
buttonZatwierdz.grid(row=14, column=0, columnspan = 2)

#Zmiana aktualnej godziny
tk.Label(mainWindow, text=" ").grid(row=13)
buttonZmianaAktualnejGodziny = tk.Button(mainWindow, text = "Zmiana aktualnej godziny", width=40, command=zmianaAktualnejGodziny)
buttonZmianaAktualnejGodziny.grid(row=15, column=0, columnspan=2)

setAktualnyCzas()
setlLabelText(labelWrzucono,str(przechowywaczPieniedzy.Suma())+" zł")

#Pętla odpowiadająca za działanie głównego okna
mainWindow.mainloop()