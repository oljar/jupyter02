# # import tkinter as tk



slownik = {}
keys=[]
values=[]
# Wydrukuj słownik
with open('nota.txt', 'r') as plik:

    linie = plik.readlines()

for linia in linie:
    klucz, wartosc = linia.strip('\n').split('=')
    slownik[klucz] = wartosc
print(slownik)
#


