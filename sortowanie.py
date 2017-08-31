#!/usr/bin/env python3
'''
Program losuje 30 liczb z przedzialu 0-300 a nastepnie sortuje\
metoda babelkowa + zapisuje do pliku /files/sortowanie.csv

'''

from random import randint
from time import sleep
import pathlib
import csv
import datetime

sort_list = [] #lista z wylosowanymi liczbami do sortowania
copied_list = []#lista niezmienna z wylosowanymi liczbami
def list_to_copy(): #kopiowanie listy
    for i in range(0, len(sort_list)):
        copied_list.append(sort_list[i])

def losuj():
    for i in range(30): #losowanie liczb
        sort_list.append( randint(0,300) ) #dodanie wylosowanej liczby do listy
    print("Wylosowane liczby: "+ str(sort_list)) # wyswietlenie calej listy

def sortuj(): #sortowanie babelkowe
    print("Rozpoczecie sortowania.")
    while True:
        swap = False #zmienna do sprawdzania czy byla zmiana miejsc
        for i in range(0, (len(sort_list)-1)):
            if sort_list[i] > sort_list[i+1]: #sprawdzenie czy liczba z prawej jest mniejsza
                sort_list[i], sort_list[i+1] = sort_list[i+1], sort_list[i]#zamiana miejsc
                swap = True #zapisanie ze nastapila zamiana
                print(sort_list)
                #sleep(0.05)#do obserwacji zmian
        if swap is False:
            print("Wylosowane liczby:", copied_list)
            print("Posortowana lista:", sort_list)
            return sort_list
def zapis_do_pliku(): #zapis wylosowanych liczb i wyniku do pliku
    date = datetime.datetime.now()#pobranie daty i godziny
    data=date.strftime("%d-%m-%y %H:%M:%S")#format daty i godziny
    target_path = pathlib.Path('files/sortowanie.csv') #sciezka do pliku
    with target_path.open('a', newline='') as target_file: #otwarcie pliku z atrybutem append
        writer = csv.writer(target_file)
        writer.writerow(["======="+data+"======"])
        writer.writerow(["wylosowane liczby:"])
        writer.writerow(copied_list)
        writer.writerow(sort_list)
        writer.writerow(["Posortowane liczby ^"])
        print("Finished writing", target_path)
    
        

def main():
    losuj()
    list_to_copy()
    sortuj()
    zapis_do_pliku()
    
main()

    