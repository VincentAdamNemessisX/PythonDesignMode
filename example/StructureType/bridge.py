class Shape:
    def __init__(self):
        self.color = None

    def draw(self): ...


class Color:
    def fill(self): ...


class RedColor(Color):
    def fill(self):
        return f'Fill with Red'


class BlueColor(Color):
    def fill(self):
        return f'Fill with Blue'


class Bridge:
    """"
    定义一个桥梁用来连接Shape和Color，shape有draw方法，color有fill方法
    """
    def __init__(self, color):
        self.color = color

    def draw(self): ...


class Circle(Bridge):
    """
    具体实现类，继承了桥梁类，实现了draw方法，同时也可以调用color的fill方法
    """
    def draw(self):
        return f'Draw a {self.color.fill()} circle'


class Square(Bridge):
    def draw(self):
        return f'Draw a {self.color.fill()} square'


if __name__ == '__main__':
    circle = Circle(RedColor())
    square = Square(BlueColor())

    print(circle.draw())
    print(square.draw())
