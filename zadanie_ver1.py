#!/usr/bin/python3

data_table_length =10
data_table = []
occuring_indexes = []

print('Wypelnij liste 10 danymi: ')

for i in range(data_table_length):
    wyraz = input(f'{i + 1} : ')
    data_table.append(wyraz)

search_string = input('Szukany wyraz: ')

for num, value in enumerate(data_table):
    if value == search_string:
        occuring_indexes.append(num)

if len(occuring_indexes) == 0:
    print(f'Brak wystapien wyrazu {search_string}')
else:
    print(f'Wyraz {search_string} pojawil sie w tablicy na indeksach : {tuple(occuring_indexes)}')
