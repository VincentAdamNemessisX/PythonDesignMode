from abc import ABC, abstractmethod


class Email(ABC):
    @abstractmethod
    def send(self, message): ...


class EmailServer(Email):

    def send(self, message: str):
        print(f'Send email to server: {message}')


class ProxyEmail(Email):
    """
    代理类，用于控制发送邮件的权限并记录日志
    """
    def __init__(self):
        self.email = EmailServer()

    def send(self, message: str):
        if self.is_allowed_to_send("user"):
            self.email.send(message)
            self.log(f"Email send to server: {message}")
        else:
            self.log(f"Email send to server[{message}] failed, user not allowed")

    @staticmethod
    def is_allowed_to_send(user):
        if user == 'admin':
            return False
        return True

    @staticmethod
    def log(message: str):
        print(f'Log[{message}]')


if __name__ == "__main__":
    email = ProxyEmail()
    email.send("Hello")
    email.send("Hello admin")
