__author__ = 'heaven.zyc'


class MyException(RuntimeError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)