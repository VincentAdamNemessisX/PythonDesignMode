"""
单例模式简单实现及调用
单例模式用于
"""


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = 0


s1 = Singleton()
s1.value += 100
print(s1.value)
s2 = Singleton()  # 重新调用__init__方法，value被重置为0
print(s1.value)
print(s2.value)
