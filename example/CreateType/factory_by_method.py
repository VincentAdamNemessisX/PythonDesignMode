import json
from xml.etree import ElementTree

"""
通过一个工厂方法，根据文件的后缀名，返回不同的连接器，这是一个简单的工厂方法实现的工厂模式例子
"""


class JsonConnector:
    def __init__(self, file_path: str):
        self.data = dict()
        with open(file_path, 'r') as f:
            self.data = json.load(f)


class XmlConnector:
    def __init__(self, file_path: str):
        self.tree = ElementTree.parse(file_path)
        self.root = self.tree.getroot()


def connection_factory(file_path: str) -> JsonConnector | XmlConnector:
    if file_path.endswith('json'):
        return JsonConnector(file_path)
    elif file_path.endswith('xml'):
        return XmlConnector(file_path)
    else:
        raise ValueError('Unknown format')


x = connection_factory('../docs/data.json')
print(x.data, type(x))
x = connection_factory('../docs/data.xml')
print(x.root.text, type(x))
