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
    text = ('Тип тренировки: {}; '
            'Длительность: {:.3f} ч.; '
            'Дистанция: {:.3f} км; '
            'Ср. скорость: {:.3f} км/ч; '
            'Потрачено ккал: {:.3f}.')

    def get_message(self) -> str:
        return self.text.format(*asdict(self).values())


@dataclass
class Training:
    """Базовый класс тренировки."""
    action: int
    duration: float
    weight: float
    m_in_km: int = 1000
    t_in_m: int = 60
    len_step: float = 0.65

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        return self.action * self.len_step / self.m_in_km

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
    Run_cc_1: int = 18
    Run_cc_2: int = 20

    def __init__(self):
        super().__init__(self.action, self.duration, self.weight)

    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в беговой тренировке"""
        return ((self.Run_cc_1 * self.get_mean_speed()
                - self.Run_cc_2) * self.weight / self.m_in_km
                * (self.duration * self.t_in_m))


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    walk_cc_1: float = 0.035
    walk_cc_2: float = 0.029

    def __init__(self, height: float):
        super().__init__(self.action, self.duration, self.weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в спортивной ходьбе"""
        return ((self.walk_cc_1 * self.weight + (self.get_mean_speed()
                 ** 2 // self.height) * self.walk_cc_2 * self.weight)
                * (self.duration * self.t_in_m))


class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP: float = 1.38
    swim_cc_1: float = 1.1
    swim_cc_2: float = 2

    def __init__(self, length_pool: float, count_pool: int,) -> None:
        super().__init__(self.action, self.duration, self.weight)
        self.length_pool = float(length_pool)
        self.count_pool = int(count_pool)

    def get_mean_speed(self) -> float:
        """Функция для получени информации о средней скорости в плавание"""
        return (self.length_pool * self.count_pool
                / self.m_in_km / self.duration)

    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в плавание"""
        return ((self.get_mean_speed() + self.swim_cc_1)
                * self.swim_cc_2 * self.weight)

    def get_distance(self) -> float:
        """Функция для получени информации о пройденной дистанции в плавание"""
        return self.action * self.len_step / self.m_in_km


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_type_dict: Dict[str, Type[Training]] = {'SWM': Swimming,
                                                    'RUN': Running,
                                                    'WLK': SportsWalking}
    if workout_type not in list(packages):
        try:
            raise TypeError(f'{workout_type} - Неизвестный тип тренировки')
        except TypeError:
            print(f'{workout_type} - Неизвестный тип тренировки')
    return workout_type_dict[workout_type](*str(data))


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()

    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180])
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
