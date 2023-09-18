from tkinter import messagebox
class Errors:
    def err_lack_of_file_or_bad_data(self):
        messagebox.showerror('Error','Nie załadowano danych - brak pliku lub błędne dane ')

    def err_lack_of_file(self):
        messagebox.showerror('Error', 'Brak pliku')

    def err_bad_data(self):
        messagebox.showerror('Error', 'Coś poszło nie tak. Sprawdź plik i nazwy kolum')

    def err_bad_process(self):
        messagebox.showerror('Error', 'Coś poszło nie tak podczas zamiany zakresu czasu')

    def err_save_problem (self):
        messagebox.showerror('Error', 'Coś poszło nie tak podczas zapisu danch')

    def err_export_problem(self):
        messagebox.showerror('Error','Coś poszło nie tak podczas przesłyania dalej danych')
    def err_export_count(self):
        messagebox.showerror('Error','Coś poszło nie tak podczas przesłyania dalej danych')