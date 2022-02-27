
'''umożliwia tworzenie pseudo losowych liczb'''

import random


def losowanie_cyfr():
    """funkcja zwracająca szesc niepowrtarzajacych sie pseudo losowych liczb"""

    szesc_cyfr = []

    count = 1
    while count < 7:
        liczba = random.randint(1,49)
        if liczba not in szesc_cyfr:
            szesc_cyfr.append(liczba)
            count += 1
    return szesc_cyfr

def czy_zbiory_cyfr_sa_rowne(moje):

    """funkcja sprawdza ile losowań jest potrzebnych aby trafić szóstkę i zwraca liczbę"""
    count = 0
    sign = 0
    lista_5 = 0
    while sign == 0:
        los = set(losowanie_cyfr())
        print(los)
        if moje == los:
            sign = 1
        else:
            if len(moje.intersection(los)) == 5:
                lista_5 += 1
            count += 1
    return count, lista_5

ilosc_losowan = czy_zbiory_cyfr_sa_rowne(set(losowanie_cyfr()))
print(f'{ilosc_losowan}')

CZAS = (ilosc_losowan[0] / 3)/52
print(f'ilosc w tym trafionych piątek {ilosc_losowan[1]}')

print('test tomasza')
