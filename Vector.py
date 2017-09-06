from math import sqrt,acos,pi
from decimal import Decimal,getcontext

getcontext().prec = 30

class Vector (object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'
    
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(self.coordinates)
        
        except ValueError:
            raise ValueError('input coordinates must be nonempty')
        except TypeError:
            raise TypeError('input coorindates must be an iterable')

    def __str__(self):
        return 'vector :{}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def __add__(self,v):
        newV = [x+y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(newV)
##        newV =[]
##        for i in range(len(self.coordinates)):
##            newV.append(self.coordinates[i]+v.coordinates[i])
##        return Vector(newV)
 
    def __sub__(self,v):
        newV = [x-y for x,y in zip(self.coordinates,v.coordinates)]
        return Vector(newV)
    
    def times_scalar(self,scalar_const):
        return Vector([Decimal(scalar_const)*x for x in self.coordinates])

    
    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return sqrt(sum(coordinates_squared))

    def normalization(self):#direction
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal('1.0')/Decimal(magnitude))
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)
        #return Vector([x/self.magnitude() for x in self.coordinates])
    
    def dot(self,w):#result is a scalar
        product = [x*y for x,y in zip(self.coordinates,w.coordinates)]
        return sum(product)

    def angle_with(self,w,in_degree = False):
##        dot_product = self.dot(w)
##        mod_x = self.magnitude()
##        mod_y = w.magnitude()
##        cos_theta = dot_product / (mod_x * mod_y)
##        theta_in_rad = acos(cos_theta)
##        if in_degree == True:
##            theta_in_deg = (180 * theta_in_rad) / pi
##            return theta_in_deg
##        else:
##            return theta_in_rad
        try:
            u1 = self.normalization()
            u2 = w.normalization()
            angle_in_radians = acos(round(u1.dot(u2),5))
            if in_degree == True:
                degrees_per_radian = 180 / pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('Cannot compute an angle with the zero vector')
            else:
                raise e
    def is_zero(self,tolerance = 1e-10):
        return self.magnitude() < tolerance
    
    def check_parallel(self,w):
        return ( self.is_zero() or
                w.is_zero() or
                self.angle_with(w) == 0 or
                self.angle_with(w) == pi)

    def check_ortho(self,w,tolerance = 1e-10):
        return (abs(self.dot(w)) < tolerance)
    
    
        
