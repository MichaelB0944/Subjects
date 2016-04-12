"""Subclass to create immutable objects.

Example:
    class Ex(Immutable):
        @Ex.make_mutable
        def __init__(self, name, count):
            self.name = name
            self.count = count
"""


class Immutable:
    def __init__(self):
        self.__mutable__ = False

    def __setattr__(self, key, value):
        if self.__mutable__:
            super().__setattr__(key, value)
        else:
            raise AttributeError('object {0} is immutable'.format(repr(self)))

    @staticmethod
    def make_mutable(f):
        def mutable(*args, **kwargs):
            super().__setattr__('__mutable__', True)
            output = f(*args, **kwargs)
            super().__setattr__('__mutable__', False)

            return output

        return mutable
