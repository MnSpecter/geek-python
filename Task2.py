time_sec = int(input('Введите время в секундах: '))
min = time_sec // 60
sec = time_sec % 60
hour = min // 60
min = min % 60
print('Время: {}:{}:{}'.format(hour, min, sec))