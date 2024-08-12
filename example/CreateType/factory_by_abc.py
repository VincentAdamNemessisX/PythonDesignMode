import json
from abc import ABC, abstractmethod
from typing import Annotated
from xml.etree import ElementTree


class Productor(ABC):
    """
    抽象类，定义一个工厂方法，返回一个连接器（由下层实现决定）
    """
    @abstractmethod
    def factory_method(self): ...

    def use(self):
        connector = self.factory_method()
        return connector


class JsonConnector(Productor):
    """
    具体实现类，实现了工厂方法，返回一个Json连接器
    """
    def __init__(self, file_path: str):
        self.data = dict()
        with open(file_path, 'r') as f:
            self.data = json.load(f)

    def factory_method(self):
        return self


class XmlConnector(Productor):
    """
    具体实现类，实现了工厂方法，返回一个Xml连接器
    """
    def __init__(self, file_path: str):
        self.tree = ElementTree.parse(file_path)
        self.root = self.tree.getroot()

    def factory_method(self):
        return self


class ConnectionFactory:
    """
    工厂类，定义一个工厂方法，返回一个连接器（由下层实现决定）
    """
    @abstractmethod
    def factory_method(self, file_path: str): ...

    def get_connector(self, file_path: str) -> Annotated[JsonConnector | XmlConnector, Productor]:
        """
        通过工厂方法获取连接器
        :param file_path: 文件路径
        :return: 规范返回类型以提供更好的代码提示和类型检查
        """
        return self.factory_method(file_path)


class JsonConnectionFactory(ConnectionFactory):
    """
    具体工厂类，实现了工厂方法，返回一个Json连接器
    """
    def factory_method(self, file_path: str):
        return JsonConnector(file_path)


class XmlConnectionFactory(ConnectionFactory):
    """
    具体工厂类，实现了工厂方法，返回一个Xml连接器
    """
    def factory_method(self, file_path: str):
        return XmlConnector(file_path)


# 调用实现了工厂方法的工厂类的get_connector方法来获取对应的连接器
x = JsonConnectionFactory().get_connector('../docs/data.json')
print(x.data, type(x))  # {'test': 'key'} <class '__main__.JsonConnector'>
x = XmlConnectionFactory().get_connector('../docs/data.xml')
print(x.root.text, type(x))  # hello world <class '__main__.XmlConnector'>
