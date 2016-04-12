"""Library for handling significant figures."""


from decimal import *


class SigFig:
    """A decimal that follows significant figure rules.

    Significant figures are used for determining the reasonable
    precision to use when performing calculations using measurements.

    """

    @staticmethod
    def then_setattr(self):
        raise AttributeError('SigFig is immutable')

    def __init__(self, value=Decimal()):
        self.context = Context(prec=len(str(value))-1)
        self.value = self.context.create_decimal(value)
        self.visual = lambda: '%.{0}e'.format(len(value.__str__()) - 2) % value
        self.__setattr__ = self.then_setattr

    def __add__(self, other):
        pass

    __radd__ = __add__

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        return SigFig.__add__(-self, other)

    def __mul__(self, other):
        pass

    __rmul__ = __mul__

    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass

    def __neg__(self):
        pass

    def __pow__(self, power, modulo=None):
        pass
