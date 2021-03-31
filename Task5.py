income = float(input('Введите объем выручки фирмы: '))
outcome = float(input('Введите объем издержек фирмы'))
if income < outcome:
    print('Фирма убыточная')
elif income == outcome:
    print('Фирма работает в ноль')
else:
    print('Фирма прибыльна')
    print('Рентабельность выручки: ', income / outcome)
    staff = int(input('Введите численность персонала: '))
    print('Чистая прибыль в расчете на одного сотрудника составляет: ', (income - outcome) / staff)