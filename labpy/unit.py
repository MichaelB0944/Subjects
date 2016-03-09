"""Provide a class for describing units."""


class Immutable:
    """Class for immutable objects."""

    __backup_setattr__ = object.__setattr__

    @classmethod
    def __unlock__(cls, self):
        """Unlock attributes of instance.

        Only use in class instantiation.
        """

        super(cls, self).__setattr__('__setattr__', super().__setattr__)

    @classmethod
    def __lock__(cls, self):
        """Lock attributes of instance.

        Only use in class instantiation.
        """

        super(cls, self).__setattr__('__setattr__', cls.__backup_setattr__)

    @staticmethod
    def wrap(f):
        def g(self, *args, **kwargs):
            self.__unlock__(self)
            f(*args, **kwargs)
            self.__lock__(self)
        return g


# ----- #
# Units #
# ----- #


class Unit(Immutable):
    """Abstract class for units."""

    @Immutable.wrap
    def __init__(self, name):
        self.name = name

    def __setattr__(self, key, value):
        raise AttributeError('object Unit is immutable')

    def __mul__(self, other):
        """Combine unit with fraction."""

        pass

    __rmul__ = __mul__

    def __truediv__(self, other):
        """Separate unit from fraction."""

        pass

    def __rtruediv__(self, other):
        """Separate unit from fraction."""

        return Unit.__truediv__(other, self)
