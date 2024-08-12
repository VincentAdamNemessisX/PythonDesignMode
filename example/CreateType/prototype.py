import copy


class Protocol:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    @property
    def copy(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    p = Protocol('HTTP', '1.1')
    p2 = p.copy  # copy from p1, then change p2, p1 will not change
    print(p2.name, p2.version)
    p2.name, p2.version = 'FTP', '4.0'
    print(p.name, p.version)
    print(p2.name, p2.version)
