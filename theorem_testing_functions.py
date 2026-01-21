"""This module is intended to keep theorem testing function which \n
are useful but not useful enough to keep in functions.py
"""
from project2 import *
import math
cleanup_time()

def Rx(theta: float):
    """Use radians"""
    return SquareMatrix([1, 0, 0, 
                         0, math.cos(theta), -math.sin(theta), 
                         0, math.sin(theta), math.cos(theta)], 
                         3, 3)

def Rz(theta: float):
        return SquareMatrix([
                         math.cos(theta), -math.sin(theta), 0, 
                         math.sin(theta), math.cos(theta), 0,
                         0, 0, 1],
                         3, 3)


j = complex(0, 1)

class VectorLengthError(Exception):
    pass


class Vector:
    """pass"""

    def __init__(self, *args):
        self.n = [i for i in args]

    def __add__(self, v):
        lst = []
        if len(self.n) != len(v.n):
            raise VectorLengthError("Vectors incompatible for addition")
        else:
            for i in range(len(self.n)):
                lst.append(self.n[i] + v.n[i])
        return Vector(*lst)
    
    def __str__(self):
        return f"{self.n}"
    
    def __len__(self):
        return len(self.n)
    
    def change(self, i: int, val: float):
        """Base function for changing vector argument value when vector is of arbitrary length \n
        Adds value to the end of vector if intex is too large"""
        if i < 1:
            raise ValueError("Innapropriate value for vector")
        new = self.n[:i-1] + [val] + self.n[i:]
        self.n = new

    def dot(self, u):
        if len(self.n) != len(u.n):
            raise VectorLengthError("Cannot dot these vectors")
        else:
            tot = 0
            for i in range(len(self.n)):
                tot += self.n[i] * (u.n[i].conjugate())
        return tot
    
    def mag(self):
        return Vector.dot(self,self)
    
    def converttomatrix(self):
        return Matrix(self.n, len(self.n), 1)

    def mulbymat(self,matrix: Matrix):
        vec_matrix: Matrix = self.converttomatrix()
        return matrix * vec_matrix



class Vector3(Vector):

    def __init__(self, *args):
        super().__init__(*args)
        self.x = self.n[0]
        self.y = self.n[1]
        self.z = self.n[2]

    def Rot(self, angle: float, axis: str = 'x'):
        if axis == 'x':
            self.n = self.mulbymat(Rx(angle)).mat
            #self = Vector3(*self.n)
            #print(self.n)
            #print(type(self.n))
            #Vector3(*self.n)
        elif axis == 'z':
            self.n = self.mulbymat(Rz(angle)).mat
        return self.n


