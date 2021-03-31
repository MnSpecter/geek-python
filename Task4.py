number = input('Введите положительное целое число: ')
symbols = list(number)
max = int(symbols[0])
for symb in symbols:
    symb = int(symb)
    if symb > max:
        max = symb

print('Максимальная цифра в числе: ', max)