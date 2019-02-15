'''
Задание 1. Реализовать класс-строитель. В его конструктор передать два списка.
Класс должен возвратить python-объект словарь. Проверить, что объект
создается корректно - создать экземпляр класса и обратиться к значению
элемента словаря, как к атрибуту класса.
'''
class WorkerBuilder:
    def __init__(self, name, information):
        for key, value in name.items():
            setattr(self, key, value)
        for key, value in information.items():
            setattr(self, key, value)

worker = WorkerBuilder({"name": "Петр","surname": "Алексеев"}, {"age": 10, 'income': 20000})
print(f'{worker.name} {worker.surname}')
print(f'Возраст: {worker.age}, доход: {worker.income}')

'''
Задание 2.
Создать класс-обертку для списка. Список передвайте в конструктор класса.
Реализуйте удаление всех элементов из списка через функцию clear.
Но функция должна применяться не к списку, а к экземпляру класса.
Внутри класса должно быть предусмотрено делегирование этой функции методу (clear)
списка.
'''
class Wrapper:
    def __init__(self, object):
        self.wrapped = object
        print(self.wrapped)

    def __getattr__(self, attrname):
        return getattr(self.wrapped, attrname)

x = Wrapper([1, 2, 3])
x.clear()
print(x.wrapped)

