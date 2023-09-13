# import tkinter as tk
#
# def validate(input):
#     if input.isdigit():
#         return True
#     elif input == "":
#         return True
#     else:
#         return False
#
# root = tk.Tk()
# entry = tk.Entry(root, validate="key")
# entry['validatecommand'] = (root.register(validate), '%P')
# entry.pack()
# root.mainloop()

# Otwórz plik
with open('nota.txt', 'r') as plik:
    # Odczytaj linie pliku
    linie = plik.readlines()

# Stwórz pusty słownik
slownik = {}


for linia in linie:

    klucz, wartosc = linia.strip().split('=')

    slownik[klucz] = wartosc
    print(slownik[klucz])





name_col_x_tab0 = 'x'



name_serial_var = 'seria X'
polynom_degree = 2
step_value = 1
scope_down_entry_tab0 = 0
scope_up_entry_tab0 = 100
formula_x = '41.1*math.sqrt(x)'
formula_y = 'y'
time_tag = 'ZEIT:'
column_x_tag_tab1 = 'M51: Pa'
column_y_tag_tab1 = 'M53: Pa'
down_scope_tab1 = 0
up_scope_tab_1 = 100
scale_time_chart = 100
name_of_chart = 'Wykres przepływowy'
name_of_X_axis_tab3 = 'objętościowy strumień powietrza'
unit_of_X_axis_tab3 = 'm3/h'
name_of_Y_axis_tab3 = 'spręż dyspozycyjny'
unit_of_Y_axis_tab3 = 'Pa'

scope_down_x_background_entry_tab0 = 0
scope_up_x_background_entry_tab0 = 100
scope_down_y_background_entry_tab0 = 5
scope_up_y_background_entry_tab0 = 105
trasparency_picture = 0.5

# Wydrukuj słownik



