from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def set_next(self, handler): ...

    @abstractmethod
    def handle(self, request): ...


class AbstractHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler: Handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle()
        return None


class ConcreteHandler1(AbstractHandler):
    def handle(self, request):
        if request == 'one':
            return f'ConcreteHandler1: {request}'
        if self.next_handler:
            return self.next_handler.handle(request)


class ConcreteHandler2(AbstractHandler):
    def handle(self, request):
        if request == 'two':
            return f'ConcreteHandler2: {request}'
        if self.next_handler:
            return self.next_handler.handle(request)


class ConcreteHandler3(AbstractHandler):
    def handle(self, request):
        if request == 'three':
            return f'ConcreteHandler3: {request}'
        if self.next_handler:
            return self.next_handler.handle(request)
        else:
            return f'Can\'t handle the request: {request}'


if __name__ == '__main__':
    reqs = ['one', 'two', 'three', 'four']
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler3 = ConcreteHandler3()
    # handler1 -> handler2 -> handler3
    handler1.set_next(handler2).set_next(handler3)
    for req in reqs:
        print(handler1.handle(req))
