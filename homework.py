from dataclasses import asdict, dataclass
from typing import Dict, Type


@dataclass
class InfoMessage:
    """Информационное сообщение о тренировке."""
    training_type: str
    duration: float
    distance: float
    speed: float
    calories: float
    text = str('Тип тренировки: {training_type}; '
               'Длительность: {duration:.3f} ч.; '
               'Дистанция: {distance:.3f} км; '
               'Ср. скорость: {speed:.3f} км/ч; '
               'Потрачено ккал: {calories:.3f}.')

    def get_message(self) -> str:
        return self.text.format(**asdict(self))


@dataclass
class Training:
    """Базовый класс тренировки."""
    action: int
    duration: float
    weight: float
    M_IN_KM: int = 1000
    T_IN_M: int = 60
    LEN_STEP: float = 0.65

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.LEN_STEP / self.M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
    pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(type(self).__name__,
                           self.duration,
                           self.get_distance(),
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    Run_calories_1: int = 18
    Run_calories_2: int = 20

    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в беговой тренировке"""
        return ((self.Run_calories_1 * self.get_mean_speed()
                - self.Run_calories_2) * self.weight / self.M_IN_KM
                * (self.duration * self.T_IN_M))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    walk_calories_1: float = 0.035
    walk_calories_2: float = 0.029

    def __init__(self, action: int, duration: float,
                 weight: float, height: float):
        super().__init__(action, duration, weight)
        self.height: float = height

    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в спортивной ходьбе"""
        return ((self.walk_calories_1 * self.weight + (self.get_mean_speed()
                 ** 2 // self.height) * self.walk_calories_2 * self.weight)
                * (self.duration * self.T_IN_M))


class Swimming(Training):
    """Тренировка: плавание."""
    swim_calories_1: float = 1.1
    swim_calories_2: float = 2
    LEN_STEP = float(1.38)

    def __init__(self, action: int, duration: float, weight: float,
                 length_pool: float, count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool: float = length_pool
        self.count_pool: int = count_pool

    def get_mean_speed(self) -> float:
        """Функция для получени информации о средней скорости в плавание"""
        return (self.length_pool * self.count_pool
                / self.M_IN_KM / self.duration)

    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в плавание"""
        return ((self.get_mean_speed() + self.swim_calories_1)
                * self.swim_calories_2 * self.weight)

    def get_distance(self) -> float:
        """Функция для получени информации о пройденной дистанции в плавание"""
        return self.action * Swimming.LEN_STEP / self.M_IN_KM


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_type_dict: Dict[str, Type[Training]] = {'SWM': Swimming,
                                                    'RUN': Running,
                                                    'WLK': SportsWalking}
    if workout_type not in workout_type_dict:
        raise TypeError(f'{workout_type} - Неизвестный тип тренировки')

    return workout_type_dict[workout_type](*list(data))


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()

    print(info.get_message())


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
