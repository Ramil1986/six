# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep

class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(3)
            i += 1

TrafficLight = TrafficLight()
TrafficLight.running()

# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width


    def mass(self):
        s = self._length * self._width * 25 * 0.05
        print(f'Асфальта необходимо: {s} тн')

road1 = Road(20, 1000)
road1.mass()




# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname} {self.position}')

    def get_total_income(self):
        summa = self._income.get('wage') + self._income.get('bonus')
        print(f'Доход работника: {summa}')

Position1 = Position('Ramil', 'Nizamov', 'buh', 25000, 10000)
Position1.get_full_name()
Position1.get_total_income()

# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} стартует'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        return f' {self.name} повернула {direction}'

    def show_speed(self):
        return f' Текущая скорость {self.name} - {self.speed} км/час'

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не полицеская машина'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f' Текущая скорость {self.name} - {self.speed} км/час превышена, пожалуйста сбавьте скорость!'
        else:
            return f' Текущая скорость {self.name}- {self.speed} км/час нормальная, двигайтесь дальше'

class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f' Текущая скорость {self.name} - {self.speed} км/час превышена, пожалуйста сбавьте скорость!'
        else:
            return f' Текущая скорость {self.name}- {self.speed} км/час нормальная, двигайтесь дальше'

class PoliceCar(Car):
    pass

BMW = SportCar(150, 'Red', 'BMW', False)
oka = TownCar(20, 'White', 'Oka', False)
lada = WorkCar(40, 'Rose', 'Lada', True)
ford = PoliceCar(120, 'Blue',  'Ford', True)
print(BMW.show_speed())
print(oka.show_speed())
print(lada.show_speed())
print(ford.show_speed())
print(BMW.turn('влево'))
print(lada.turn('направо'))
print(BMW.police())
print(oka.police())
print(lada.police())
print(ford.police())

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title


    def draw(self):
        print(f'запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки ручкой')

class Pencil(Stationery):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки карандашом')

class Handle(Stationery):
    def draw(self):
        print(f'Вы взяли {self.title}. Запуск отрисовки маркером')

a = Pen('ручка')
b = Pencil('карандаш')
c = Handle('маркер')
a.draw()
b.draw()
c.draw()
