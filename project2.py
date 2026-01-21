from functions import cleanup_time
from functions import chess
from sys import setrecursionlimit
import copy
#from theorem_testing_functions import Vector, Vector3
#from Graph_theory import fac
cleanup_time()
setrecursionlimit(200000)

def subsets(A: list, cur = None, powerset = None):
    """Pass"""
    if len(A) < 1:
        powerset.append(cur)
    if cur is None:
        cur = []
        powerset = []

    for i in range(len(A)):
        subsets(A[i+1:], cur + [A[i]], powerset)
    return powerset


def permutation_generator(A: list, permutation = None, permutation_list = None):
    """Pass"""
    if permutation is None:
        permutation = []
        permutation_list = []
    if len(A) < 1:
        permutation_list.append(permutation)
        #return permutation

    for i in range(len(A)):
        permutation_generator(A[:i] + A[i+1:], permutation + [A[i]], permutation_list)
    return permutation_list

def unravel(A: list,unravelled = None):
    """Unravels a listylist into only a list \n
    Esentially worthless"""
    if unravelled is None:
        unravelled = []
    if (all(type(x) != list for x in A)):
        unravelled += A
    else:
        for r in A:
            if type(r) == list:
                unravel(r, unravelled)
            else:
                unravelled += [r]
    return unravelled

def iseven(n):
    if n % 2 == 0:
        return True
    return False

def s(lst: list = []):
    if lst:
        for r in lst:
            yield iseven(r)

lst = [1,2,3] #A useful list

#We shall treat all matricies as squares

def mtrx_mul(mat1: list,mat2: list, rows = 0, cols = 0) -> list:
    """pass"""
    #Cols is the number of columns in the first matrix
    #Rows is the number of rows in the first matrix
    #Cols of second is found by dividing below
    if not rows:
        size = int(len(mat1) ** (1/2))
        rows = size
        cols = size
        rowed1 = chess.list_rower(mat1, cols)
        rowed2 = chess.list_rower(mat2, size)
    else:
        rowed1 = chess.list_rower(mat1, cols)
        size = len(mat2) // cols #Of the second one in columns
        rowed2 = chess.list_rower(mat2, size)
    
    newmatrix = []
    for i in range(rows): 
        for j in range(size):
            toappend = 0
            for k in range(cols):
                toappend += rowed1[i][k]*rowed2[k][j]
            newmatrix.append(toappend)
            
    return newmatrix

def mtrx_pwr(mat: list, n: int, size = None, newmatrix = None, old = None) -> list:
    """Proving I am an genius function."""
    if size is None:
        size = int(len(mat) ** (1/2))
        newmatrix = []
        old = copy.deepcopy(mat)
    if n <= 1:
        newmatrix = copy.deepcopy(mat)
        return newmatrix
        
    else:
        return mtrx_pwr(mtrx_mul(old, mat), n-1, size, newmatrix, old)



class MatrixMultiplicationError(Exception):
    pass

class MatrixSizeError(Exception):
    pass

class Matrix:
    def __init__(self, mat: list, row: int, col: int):
        self.mat = mat
        self.row = row #Number of rows
        self.col = col #Number of columns

    def __str__(self):
        return f"{self.mat}"

    def __mul__(self, B):
        if  self.col == B.row:
            new_mat = Matrix(mtrx_mul(self.mat, B.mat, self.row, self.col), self.row, B.col)
        else:
            raise MatrixMultiplicationError("Incompatible matricies")
        return new_mat
    
    def __len__(self):
        return len(self.mat)

    def rowed(self):
        return list(chess.list_rower(self.mat, self.row))

    def collummed(self):
        return list(chess.list_colummer(self.mat, self.row))
    
class SquareMatrix(Matrix):
    def __init__(self, mat, row, col):
        if row != col:
            raise MatrixSizeError("Matrix is not a square matrix")
        super().__init__(mat, row, col)
        if float(len(self.mat) / row) != float(col):
            raise MatrixSizeError("Matrix is not a square matrix") 

    def raisedto(self, n):
        return SquareMatrix(mtrx_pwr(self.mat, n), self.row, self.col)
    
    def issymmetric(self):
        return self.collummed() == self.rowed()

        

