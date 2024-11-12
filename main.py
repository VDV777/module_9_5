# Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
# Наследования достаточно, класс оставьте пустым при помощи оператора pass.
#
# Создайте класс Iterator, который обладает следующими свойствами:
# Атрибуты объекта:
# start - целое число, с которого начинается итерация.
# stop - целое число, на котором заканчивается итерация.
# step - шаг, с которым совершается итерация.
# pointer - указывает на текущее число в итерации (изначально start)
# Методы:
# __init__(self, start, stop, step=1) - принимающий значения старта и конца итерации, а также шага. В этом методе в первую очередь проверяется step на равенство 0. Если равно, то выбрасывается исключение StepValueError('шаг не может быть равен 0')
# __iter__ - метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
# __next__ - метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация завершится либо когда pointer станет больше stop, либо меньше stop. Учтите это при описании метода.
#
# Пункты задачи:
# Создайте класс исключения StepValueError.
# Создайте класс Iterator и опишите его атрибуты и методы.
# Создайте несколько объектов класса Iterator и совершите итерации с ними при помощи цикла for.


class StepValueError(ValueError):
    ...


class Iterator:

    def __init__(self, start: int, stop: int, step: int = 1):

        self.start: int = start
        self.stop: int = stop
        self.step: int = step
        self.pointer: int = start

    def __iter__(self) -> 'Iterator':

        self.pointer = self.start
        return self

    def __next__(self) -> int:

        if self.step == 0:
            raise StepValueError()

        self.pointer += self.step

        if self.step > 0:
            if self.pointer > self.stop:

                raise StopIteration()

        if self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration()

        return self.pointer


iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
    print()
for i in iter3:
    print(i, end=' ')
    print()
for i in iter4:
    print(i, end=' ')
    print()
for i in iter5:
    print(i, end=' ')
    print()



