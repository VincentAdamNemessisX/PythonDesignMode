from abc import ABC, abstractmethod


class CarBuilder(ABC):
    """
    构造者基类，定义构建的步骤（不关心顺序）
    """
    @abstractmethod
    def set_wheels(self, value: int):
        pass

    @abstractmethod
    def set_seats(self, value: int):
        pass

    @abstractmethod
    def set_engine(self, value: str):
        pass

    @abstractmethod
    def set_color(self, value: str):
        pass


class Car:
    """
    产品类，用来存储构建的结果
    """
    def __init__(self):
        self.wheels = None
        self.seats = None
        self.engine = None
        self.color = None

    def __str__(self):
        return f'Car(wheels={self.wheels}, seats={self.seats}, engine={self.engine}, color={self.color})'


class GoodCarBuilder(CarBuilder):
    """
    具体构造者，实现构建的步骤
    """
    def __init__(self):
        self.car = Car()

    def reset(self):
        self.car = Car()

    def set_wheels(self, value: int):
        self.car.wheels = value

    def set_seats(self, value: int):
        self.car.seats = value

    def set_engine(self, value: str):
        self.car.engine = value

    def set_color(self, value: str):
        self.car.color = value


class Director:
    """
    用来编排构建步骤的顺序
    """
    def __init__(self, bdr: CarBuilder):
        self.builder = bdr

    def make_good_car(self):
        self.builder.reset()
        self.builder.set_wheels(4)
        self.builder.set_seats(2)
        self.builder.set_engine('V8')
        self.builder.set_color('Red')


if __name__ == '__main__':
    builder = GoodCarBuilder()
    director = Director(builder)
    director.make_good_car()
    print(builder.car)
