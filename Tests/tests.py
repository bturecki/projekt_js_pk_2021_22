import tkinter as tk
import unittest

class TKinterTestCase(unittest.TestCase):
    """
    Klasa do testów jednostkowych
    """
    def setUp(self):
        self.root=tk.Tk()
        self.pump_events()

    def tearDown(self):
        if self.root:
            self.root.destroy()
            self.pump_events()

    def pump_events(self):
        while self.root.dooneevent(tk.ALL_EVENTS | tk.DONT_WAIT):
            pass

class TestNumerRejestracyjny(TKinterTestCase): #TODO zrobić testy
    def test_enter(self):
        self.pump_events()
