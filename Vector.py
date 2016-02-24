class DimensionError(Exception):
    pass

def int_str(x):
    return [str(i) for i in x]

class Vector:
    def __init__(self, *args, extra=0):
        if extra:
            self.val = []
        else:
            self.val = args
        self.dim = len(args)
        for i in range(extra):
            self.val.append(0)
            
    def __repr__(self):
        return 'Vector(' + ', '.join(int_str(self.val)) + ')'
        
    def __str__(self):
        return '<' + ', '.join(int_str(self.val)) + '>'
    
    # Vector Magnitude
    def mag(self):
        return (i ** 2 for i in self.val) ** (1 / 2)
    
    # Dimension Check
    def __dim__(self, other):
        if not (type(other) == Vector):
            raise TypeError('Expected {0} got {1}'.format(Vector.__name__, type(other).__name__))
        if not (self.dim == other.dim):
            raise DimensionError
    
    # Math Operators #
    
    def __add__(self, other):
        self.__dim__(other)
        newV = Vector(extra=self.dim)
        for i in range(self.dim):
            newV.val[i] = self.val[i] + other.val[i]
        return newV
        
    def __sub__(self, other):
        self.__dim__(other)
        newV = Vector(extra=self.dim)
        for i in range(self.dim):
            newV.val[i] = self.val[i] - other.val[i]
        return newV
        
    def __mul__(self, other):
        try:
            other = float(other)
            newS = Vector(extra=self.dim)
            for i in range(self.dim):
                newS.val[i] = self.val[i] * other
        except:
            self.__dim__(other)
            newS = 0
            for i in range(self.dim):
                newS += self.val[i] * other.val[i]
        return newS
        
    def __rmul__(self, other):
        return self.__mul__(other)
        
    # Common Vector Methods 
    
    def proj(self, other):
        self.__dim__(other)
        return ((self * other) / other.mag() ** 2) * other
