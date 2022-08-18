M_IN_KM = 1000


class InfoMessage:
    """Информационное сообщение о тренировке."""
    def _init_(self,
               training_type: str,
               duration: float,
               distance: float,
               speed: float,
               calories: float) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories

    def get_message(self) -> str:
        return (f'Тип тренировки:{self.training_type};'
                f'Длительность:{self.duration} ч.;'
                f'Дистанция :{self.distance} км;'
                f'Ср. скорость:{self.speed} км/ч;'
                f'Потрачено ккал:{self.calories}')


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        LEN_STEP = 0.65
        return self.action * LEN_STEP / M_IN_KM

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        return InfoMessage(Training.__name__,
                           self.duration,
                           self.get_distance,
                           self.get_mean_speed(),
                           self.get_spent_calories())


class Running(Training):
    """Тренировка: бег."""
    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в беговой тренировке"""
        COEFF_CALORIE_1: int = 18
        COEFF_CALORIE_2: int = 20
        spent_calories = ((COEFF_CALORIE_1 * self.get_mean_speed()
                          - COEFF_CALORIE_2)
                          * self.weight / M_IN_KM * self.duration)
        return spent_calories


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 height: float,
                 ) -> None:
        super()._init_(self, action, duration, weight)
        self.height = height

    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в спортивной ходьбе"""
        COEFF_CALORIE_3: float = 0.035
        COEFF_CALORIE_4: float = 0.029
        walking_calories = ((COEFF_CALORIE_3 * self.weight
                            + (self.get.mean.speed() ** 2 // self.height)
                            * COEFF_CALORIE_4 * self.weight) * self.duration)
        return walking_calories


class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 length_pool: float,
                 count_pool: float,
                 ) -> None:
        super()._init_(self, action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Функция для получени информации о средней скорости в плавание"""
        average_speed = (self.length_pool * self.count_pool
                         / M_IN_KM / self.duration)
        return average_speed

    def get_spent_calories(self) -> float:
        """Функция для получени информации о каллориях в плавание"""
        COEFF_CALORIE_5: float = 1.1
        COEFF_CALORIE_6: float = 2
        swimming_calories = ((self.get_mean_speed
                             + COEFF_CALORIE_5)
                             * COEFF_CALORIE_6 * self.weight)
        return swimming_calories

    def get_distance(self) -> float:
        """Функция для получени информации о пройденной дистанции в плавание"""
        LEN_STEP: float = 1.38
        return self.action * LEN_STEP / M_IN_KM
    pass


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_type_dict: dict[str, Training] = {'SWM': Swimming,
                                              'RUN': Running,
                                              'WLK': SportsWalking}
    training = workout_type_dict[workout_type] * (data)
    return training


def main(training: Training) -> None:
    """Главная функция."""
    info = InfoMessage.get_message(training.show_training_info())
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
