class Vector:
    def __init__(self,coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
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
        return Vector([scalar_const*x for x in self.coordinates])

    
