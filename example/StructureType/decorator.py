from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self): ...


class ConcreteComponent(Component):
    """
    具体组件类，实现了组件接口
    """
    def operation(self):
        return 'ConcreteComponent'


class Decorator(Component):
    """
    装饰器抽象类，继承自组件接口
    """
    def __init__(self):
        self.component = None

    @abstractmethod
    def operation(self): ...


class ConcreteDecoratorA(Decorator):
    """
    具体装饰器类，实现了装饰器接口
    """
    def __init__(self, component: Component):
        super().__init__()
        self.component = component

    def operation(self):
        return f'ConcreteDecoratorA({self.component.operation()})'


class ConcreteDecoratorB(Decorator):
    """
    具体装饰器类，实现了装饰器接口
    """
    def __init__(self, component: Component):
        super().__init__()
        self.component = component

    def operation(self):
        return f'ConcreteDecoratorB({self.component.operation()})'


if __name__ == '__main__':
    cpt = ConcreteComponent()
    decorator_a = ConcreteDecoratorA(cpt)
    decorator_b = ConcreteDecoratorB(decorator_a)
    print(decorator_b.operation())
