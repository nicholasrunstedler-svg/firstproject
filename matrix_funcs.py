"""Functions on matricies"""
from functions import cleanup_time, list_rower, list_flipper
cleanup_time()

def item_replacer_super_awesome_time_67(lst: list, item, index: int) -> list:
    """Takes an item out of a list and an index and replaces it with a desired one"""
    return lst[:index] + [item] + lst[index+1:]


def tuple_reducer(orderednums: tuple) -> int:
    """Reduces a tuple. Always subtracts the first entry from the second \n
    Esentially a bilinear form on R"""
    return -orderednums[0] + orderednums[1]


def multiply_a_row(row: list, scalar: float) -> list:
    """Multiples a row by a nonzero scalar"""
    
    return [x*scalar for x in row]


def single_row_reduction(matrix: list, row_to_use_index: int, to_reduce: int, rowing_needed = False) -> list:
    """Performs what it seems to do"""
    if row_to_use_index == to_reduce:
        raise IndexError("Row used to reduce itself.")

    if rowing_needed:
        new_matrix = list_rower(matrix)

    idx = 0
    entry = matrix[row_to_use_index][idx]
    while entry == 0:
        if idx < len(matrix[row_to_use_index]):
            idx += 1
            entry = matrix[row_to_use_index][idx]
            
        else:
            raise TypeError("ROW FULL OF ZEROES")
        
    # Idx is now the position of the first nonzero entry
    aligned_entry = matrix[to_reduce][idx] #This one will get reduced

    new_row = multiply_a_row(matrix[row_to_use_index],   
                             aligned_entry/matrix[row_to_use_index][idx]) #makes a new row according to the matrix reduction algorithm

    special_list = zip((new_row),matrix[to_reduce]) #Putting them together so I can use my tuple_reducer function simply

    return [tuple_reducer(x) for x in special_list]


def get_row(lst: list, row: int) -> list:
    rowe = []
    for pos in lst:
        if pos[0] == row:
            rowe.append(pos)
    return rowe


def get_col(lst: list, col: int) -> list:
    cole = []
    for pos in lst:
        if pos[1] == col:
            cole.append(pos)
    return cole


    
mat1 = [
    [   1   ,    2     ,   1    ],

    [   2   ,    2     ,   0    ],

    [   0   ,    5     ,   1    ]
]

def matrix_reducer_from_row(matrix: list, row_idx: int) -> list:
    """Reduces a matrix \n
    Starts from chosen row, goes down from there."""
    idx = 0
    reducto = []#[matrix[row_idx]]
    for row in matrix:
        if row == matrix[idx] and row_idx != idx:
            reducto.append(single_row_reduction(matrix, row_idx, idx))
            idx += 1
        elif idx < len(matrix[row_idx]) - 1:
            pass
            idx += 1
    reducto.insert(row_idx, matrix[row_idx])
    return reducto



def weird_reducer(matrix: list) -> list:
    """It just straight up reduces em' """
    reduced = matrix
    for idx in range(len(matrix)):
        reduced = matrix_reducer_from_row(reduced, idx)

    return reduced

def coked_up_reducer(matrix: list) -> list:
    """Coked up reducer."""
    return list_flipper(weird_reducer(list_flipper(weird_reducer(matrix))))

def inverse_exists(matrix: list) -> bool:
    """Checks if a matrix has an inverse"""
    if any(all(y == 0 for y in x) for x in coked_up_reducer(matrix)):
        return False
    return True

mat2 = [ [2, 3, -1, 4, 0, 6, -2, 1, 5],
  [1, -2, 4, -1, 7, -3, 2, 0, 8],
  [3, 0, 2, 6, -1, 1, 9, -4, 0],
  [5, -1, -3, 2, 3, 0, 1, 7, -2],
  [0, 4, 1, -2, 8, -5, 6, 2, 3],
  [2, 6, 0, 1, -3, 4, -1, -2, 9],
  [4, -3, 5, 0, 1, 2, 7, 3, 6],
  [7, 2, -4, 3, 5, -1, 0, 6, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1] ]



    
    


