"""Provide a class for describing units."""


class Unit:
    """Abstract class for units."""

    def __init__(self, name='Unit', base=None, full_name=None, parent=None):
        # Unlock object for initialization
        temp_setattr = self.__setattr__
        super().__setattr__('__setattr__', super().__setattr__)

        self.__name__ = name
        self.full_name = full_name or name
        self.parent = parent

        if base is None:
            self.composition = None
            self.power = None
        elif isinstance(base, Unit):
            self.composition = base.composition
            self.power = base.power
        else:
            raise TypeError('expected Unit got %s' % repr(type(base)))

        # Lock object after initialization
        self.__setattr__ = temp_setattr

    def __setattr__(self, key, value):
        raise AttributeError('object Unit is immutable')

    def __mul__(self, other):
        """Combine unit with fraction."""

        pass

    __rmul__ = __mul__

    def __truediv__(self, other):
        """Combine values of different or the same units."""

        pass

    def __rtruediv__(self, other):
        return Unit.__truediv__(other, self)

    def __pow__(self, power, modulo=None):
        pass


# ----- #
# Units #
# ----- #

"Units gathered from www.wikibooks.org/wiki/General_Chemistry/Units" \
    "Unit information available under CC Attribution-ShareAlike license"

# SI Fundamental Units
l = Unit('l', full_name='Length')
t = Unit('t', full_name='Time')
m = Unit('m', full_name='Mass')
T = Unit('T', full_name='Thermodynamic Temperature')
n = Unit('n', full_name='Amount of Substance')
Q = Unit('Q', full_name='Electrical Charge')

vol = Unit('vol', full_name='Volume')
press = Unit('press', full_name='Pressure')

# SI Fundamental Units (Unit Symbols)
meter = Unit('meter', full_name='Meter', parent=l)
s = Unit('s', full_name='Second', parent=t)
kg = Unit('kg', full_name='Kilogram', parent=m)
K = Unit('K', full_name='Kelvin', parent=T)
mol = Unit('mol', full_name='Mole', parent=n)
C = Unit('C', full_name='Coulomb', parent=Q)

# SI Derived Units
N = Unit('N', kg * meter / (s ** 2), full_name='Newton')
J = Unit('J', kg * (meter ** 2) / (s ** 2), full_name='Joule')
Pa = Unit('Pa', kg / meter / (s ** 2), full_name='Pascal')
W = Unit('W', kg * (meter ** 2) / (s ** 3), full_name='Watt')
A = Unit('A', C / s, full_name='Ampere')
V = Unit('V', J / C, full_name='Volt')


class UsefulUnit:
    """Other Useful Units"""
    L = Unit('L', full_name='Liter', parent=vol)
    atm = Unit('atm', full_name='Atmosphere', parent=press)


class SolutionUnit:
    """solution Concentration Units"""
    M = Unit('M', mol / UsefulUnit.L, full_name='Molarity')
    m = Unit('m', mol / kg, full_name='Molality')
    X = Unit('X', full_name='Mole Fraction')
    ppm = Unit('ppm', full_name='Parts per Million')
    ppb = Unit('ppb', full_name='Parts per Billion')
