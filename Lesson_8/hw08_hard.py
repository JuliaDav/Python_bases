'''
Задание_1. Создайте свое исключение для проверки вводимого числа.
Исключение должно возбуждаться, если пользователь ввел отрицательное число.
Также предусмотрите тот, случай, что пользователь ввел не число, а строку
(здесь можно применить встроенное исключение).
'''
class InputError(Exception):
    def __init__(self, a):
        Exception.__init__(self)
        self.a = a
    def __str__(self):
        return 'InputException: Число отрицательно ({0}); ' \
               'нужно ввести положительное'.format(self.a)

def max_chars(text):
    if text < 0:
        raise InputError(text)
    elif text >= 0:
        pass
    else:
        raise InputError(text)

try:
    max_chars(-3)
except InputError as ex:
    print(ex)
except TypeError as ter:
    print(f'Введенное значение не является числом, нужно ввести число')
else:
    print('Не было исключений.')
finally:
    pass

