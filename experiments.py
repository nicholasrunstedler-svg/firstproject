import sys
import calendar
from time import sleep
import os

sys.setrecursionlimit(1000)

def f(x, path=None):
    if path is None:
        path = []
        path.append(x)
    return path


def f1(x, path=[]):
    return path + [x]


def subsets(nums, path=[]):
    """Takes all \"Subsets\" of a list"""
    return_list = []
    return_list.append(path)
    for i in range(len(nums)):
        sub_results = subsets(nums[i+1:], path + [nums[i]])
        return_list.extend(sub_results)
    return return_list


def subsets_of_size(nums, size: int) -> list:
    """Takes all \"Subsets\" of a list of specified size"""
    return_list = []
    for i in subsets(nums):
        if len(i) == size:
            return_list.append(i)

    return return_list


def two_toThe_powerOf(number):
    """Takes 2 to the power of the input in a super efficient way"""
    sooper_set = []
    for i in range(number):
        sooper_set.append(i)

    return len(subsets(sooper_set))


#x = int(input("Give a number and ill give you 2 ^ that number "))

print("\x1b[2J\x1b[H", end="")

def find_zeroes(string: str) -> int:
    for i in range(len(string)):
        if string[i] == '0':
            return find_zeroes(string[1:]) + 1
        else:
            return find_zeroes(string[1:])
    return 0
        

#print(find_zeroes(input("Enter a numbser and ill find the zeroes ").strip()))

def item_replacer(lst: list, item: any, entry: int, ):
    """Takes a list, item, and entry, and replaces the item at that entry with the one given.\n
    The entry is taken as intuition would have it. That is, the first entry will be treated as the entry indexed with 1, and not 0"""
    real_entry = entry - 1
    first_half = lst[:real_entry]
    second_half = lst[real_entry + 1:]
    new_list = first_half + [item] + second_half
    
    return new_list
    

def first_non_zero(lst: list) -> float:
    """Finds the first non-zero value in a list and returns it.\n
    Thats it. Intended for aid in matrix reduction algorithms"""
    for i in lst:
        if i != 0:
            return i


def single_row_reduction(row_1: list, row_2: list):
    """ONLY ENTER LISTS OF EQUAL SIZE INTO THIS FUNCTION"""
    new_row2 = row_2
    for entry in row_1:
        index_of_entry = row_1.index(entry) 
        value_to_reduce = row_2[index_of_entry]
        if value_to_reduce != 0:
            new_row2 = item_replacer(new_row2, value_to_reduce - entry * (row_2[row_1.index(first_non_zero(row_1))] / first_non_zero(row_1)), index_of_entry + 1)
            pass
    return new_row2



def list_flipper(lst: list) -> list:
    """IT FLIPS THE LIST!!!"""
    if len(lst) != 0:
        return [lst[-1]] + list_flipper(lst[:-1]) 
    else:
        return [] 


