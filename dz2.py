for i in range(3):
    a = input('Введите вашу строку: ')
    try:
        b = []
        res = 0
        for i in a:
            b.append(i)
        ch1 = int(b[0])
        ch2 = int(b[1])
        s = ch1 / ch2
    except ZeroDivisionError:
        print('Ошибка деления на ноль! Введите строку повторно: ')
    except ValueError:
        print('Строка состоит из букв, невозможно найти результат деления!')
        break
    else:
        print('Результат деления первого числа на второе: ', s)
        break