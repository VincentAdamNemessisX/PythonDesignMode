from abc import ABC, abstractmethod


class FileComponent(ABC):
    """
    抽象类，定义一个文件组件的基本属性和操作
    """
    def __init__(self):
        self.name = None

    @abstractmethod
    def list(self): ...


class File(FileComponent):
    """
    具体实现类，实现了文件组件的操作
    """
    def __init__(self, name):
        super().__init__()
        self.name = name

    def list(self):
        return self.name


class Folder(FileComponent):
    """
    具体实现类，实现了文件组件的操作，并追加了一个列表属性，用来存储子文件/文件夹
    """
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.children = []

    def list(self):
        return self.children

    def add(self, *args: FileComponent):
        """
        添加子文件/文件夹
        :param args: 文件/文件夹
        :type args: 文件组件对象
        """
        for f in args:
            self.children.append(f)

    def remove(self, f: FileComponent):
        self.children.remove(f)

    def get(self, index: int):
        return self.children[index]


if __name__ == '__main__':
    root = Folder(name="root")
    f1 = File(name="file1")
    f2 = Folder(name="folder2")
    root.add(f1, f2)
    print(root.list())
    f3 = File(name="file3")
    f4 = Folder(name="folder4")
    f2.add(f3, f4)
    print(f2.list())
