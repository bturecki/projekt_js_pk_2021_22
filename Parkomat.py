#Import biblioteki do tworzenia GUI
from tkinter import *

#Tworzenie instancji okna tkinter
mainWindow = Tk()

#Ustawienia okna
mainWindow.title("Parkomat")
mainWindow.geometry("400x500")
mainWindow.eval('tk::PlaceWindow . center')

#Pętla odpowiadająca za działanie głównego okna
mainWindow.mainloop()