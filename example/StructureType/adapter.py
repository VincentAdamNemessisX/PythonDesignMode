class Target:
    def request(self) -> str:
        return "Target: The default target's behavior."


class Source:
    @staticmethod
    def specific_request() -> str:
        return 'Source: The default source\'s behavior.'


class ClassAdapter(Target, Source):
    def request(self) -> str:
        return self.specific_request()


class ObjectAdapter(Target):
    def __init__(self, source: Source):
        self.source = source

    def request(self) -> str:
        return self.source.specific_request()


def client_code(target) -> None:
    print(target.request())


if __name__ == '__main__':
    print('Client: I can work just fine with the Target objects:', end=" ")
    tgt = Target()
    client_code(tgt)

    sre = Source()
    print('Client: The Source class is incompatible with the Target class. '
          'But I can work with it via the Adapter:', end=" ")
    adapter_class = ClassAdapter()
    client_code(adapter_class)

    print('Client: The Source class is incompatible with the Target class. '
          'But I can work with it via the Adapter:', end=" ")
    adapter_object = ObjectAdapter(sre)
    client_code(adapter_object)
