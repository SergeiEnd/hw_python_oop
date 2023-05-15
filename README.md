# Модуль фитнес-трекера
Модуль расчета и отображения полной информации о тренировках по данным от блока датчиков.
## Задача
Реализовать программный модуль по методологии ООП для расчета и отображения информации о прошедшей тренировке по данным от блока датчиков.

### Базовый класс
class Training
Свойства класса
action - основное считываемое действие во время тренировке (шаг - бег, ходьба; гребок - плавание);
duration - длительность тренировки;
weight - вес спортсмена;
M_IN_KM = 1000 - константа для перевода значений из метров в километры. Её значение — 1000.
LEN_STEP - расстояние, которое спортсмен преодалевает за один шаг или гребок. Один шаг — это 0.65 метра, один гребок при плавании — 1.38 метра.
Методы класса
get_distance() - метод возвращает значение дистанции приодоленной за тренировку
### базовая формула расчета
шаг * LEN_STEP / M_IN_KM
get_mean_speed() - метод возвращает значение средней скорости движения во время тренировки
### базовая формула расчета
дистанция / длительность
get_spent_calories() - метод возвращает число потраченных колорий
show_training_info() - метод возвращает объект возвращает объект класса сообщения
Классы наследнки
Класс беговой тренировки

class Running
Свойства класса
наследуюутся

Методы класса
пререопределить метод:

get_spent_calories() - метод возвращает число потраченных колорий
### формула расчета
(18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
Класс спортивной ходьбы

class SportsWalking
Свойства класса
Добавляемые свойства:

height - рост
Методы класса
пререопределить метод:

get_spent_calories() - метод возвращает число потраченных колорий
### формула расчета
(18 * средняя_скорость - 20) * вес_спортсмена / M_IN_KM * время_тренировки_в_минутах
Класс тренировки в бассейне

class Swimming
Свойства класса
Добавляемые свойства:

length_pool - длина бассейна
count_pool - количество проплытых бассейнов
Методы класса
пререопределить метод:

get_mean_speed() - метод возвращает значение средней скорости движения во время тренировки
### формула расчета
длина_бассейна * count_pool / M_IN_KM / время_тренеровки
get_spent_calories() - метод возвращает число потраченных колорий
### формула расчета
(скорость + 1.1) * 2 * вес
Класс информационного сообщения
class InfoMessage
Свойства класса
training_type - тип тренировки
duration - длительность тренировки
distance -дистанция приодоленная за тренировку
speed - средняя скорость движения во время движения
calories - потраченные за время тренировки килокалории
Методы класса
get_message() - метод выводит возвращает строку сообщения:
### выводимое сообщение
### все значения типа float округляются до 3 знаков после запятой
> 'Тип тренировки: {training_type}; Длительность: {duration} ч.; Дистанция: {distance} км; Ср. скорость: {speed} км/ч; Потрачено ккал: {calories}'.
Функции модуля
> def read_package
Функция read_package принимает на вход код тренировки и список её параметров.
Функция должна определить тип тренировки и создать объект соответствующего класса, передав ему на вход параметры, полученные во втором аргументе. Этот объект функция должна вернуть.
> def main(training)
Функция main() должна принимать на вход экземпляр класса Training.

При выполнении функции main()для этого экземпляра должен быть вызван метод show_training_info(); результатом выполнения метода должен быть объект класса InfoMessage, его нужно сохранить в переменную info.
Для объекта InfoMessage, сохранённого в переменной info, должен быть вызван метод, который вернет строку сообщения с данными о тренировке; эту строку нужно передать в функцию print().
Инструкции по установке
- Клонируйте репозиторий:

``` git clone git@github.com:SergeiEnd/hw_python_oop.git ```
- Установите и активируйте виртуальное окружение:

для MacOS
``` python3 -m venv venv ```
для Windows
``` python -m venv venv ```
``` source venv/bin/activate ```
``` source venv/Scripts/activate ```
- Установите зависимости из файла requirements.txt:

``` pip install -r requirements.txt ```

Автор
## Сергей Ендовицкий 
(lightfire.89@mail.ru) 
(telegram @end_sergio)
