class DimensionError(Exception):
    pass


def int_str(x):
    return [str(i) for i in x]


class Vector:
    def __init__(self, *args, extra=0):
        if extra:
            self.val = []
        else:
            self.val = list(args)
        self.dim = len(args) or extra
        for i in range(extra):
            self.val.append(0)
            
    def __repr__(self):
        return Vector.__name__ + '(' + ', '.join(int_str(self.val)) + ')'
        
    def __str__(self):
        return '<' + ', '.join(int_str(self.val)) + '>'
    
    # Vector Magnitude
    def mag(self):
        return sum([i ** 2 for i in self.val]) ** (1 / 2)
    
    # Dimension Check
    def __dim__(self, other):
        if not (type(other) == Vector):
            raise TypeError('Expected {0} got {1}'.format(Vector.__name__, type(other).__name__))
        if not (self.dim == other.dim):
            raise DimensionError
    
    # Math Operators #
    
    def __add__(self, other):
        self.__dim__(other)
        new_v = Vector(extra=self.dim)
        for i in range(self.dim):
            new_v.val[i] = self.val[i] + other.val[i]
        return new_v
        
    def __sub__(self, other):
        self.__dim__(other)
        new_v = Vector(extra=self.dim)
        for i in range(self.dim):
            new_v.val[i] = self.val[i] - other.val[i]
        return new_v
        
    def __mul__(self, other):
        if type(other) in {int, float}:
            new_s = Vector(extra=self.dim)
            for i in range(self.dim):
                new_s.val[i] = self.val[i] * other
        else:
            self.__dim__(other)
            new_s = 0
            for i in range(self.dim):
                new_s += self.val[i] * other.val[i]
        return new_s
        
    def __rmul__(self, other):
        return self.__mul__(other)
        
    # Common Vector Methods 
    
    def project(self, other):
        self.__dim__(other)
        return ((self * other) / other.mag() ** 2) * other

    def unit(self):
        return self * (1 / self.mag())
