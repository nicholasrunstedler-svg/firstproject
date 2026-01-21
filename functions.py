"""This module contains functions for various experiments."""
import copy
from time import sleep
from random import randint
from os import system
import pygame
from experiments import list_flipper
import sys
#from chess import check_vertical_entries

sys.setrecursionlimit(1000000)
sys.set_int_max_str_digits(1000000)


if True: #Very useful
    def pnrit(words):
        print(words)

    def pint(words): # words words
        print(words)

    def pirnt(text):
        print(text)

    def prnit(text):
        print(text)

    def prit(text):
        print(text)

    def prnt(text):
        print(text)

    def prin(text):
        print(text)

    def prinnt(text):
        print(text)

    def priint(text):
        print(text)

    def printt(text):
        print(text)

    def prent(text):
        print(text)

    def pront(text):
        print(text)

    def prant(text):
        print(text)

    def pr8nt(text):
        print(text)

    def prjnt(text):
        print(text)

    def prmnt(text):
        print(text)

    def Print(text):
        print(text)

    def PRINT(text):
        print(text)

    def prind(text):
        print(text)

    def prinz(text):
        print(text)


def cleanup_time() -> None:
    system('cls')
cleanup_time()

class number_theory:
    """A class made for the development of number theoretical functions."""
    def __init__(self):
        pass


    def fac(n, memo = None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n < 1:
            return 1
        memo[n] = number_theory.fac(n-1, memo) * n
        return memo[n]


    def P(n, r) -> int:
        """This function calculates the number of permutations of n items taken r at a time."""
        num = number_theory.fac(n) / number_theory.fac(n - r)
        return int(num)

        # return fac(n) // fac(n - r)


    def C(n, r) -> int:
        """Takes the number of r combinations of n elements"""
        n_choose_r = number_theory.P(n, r) / number_theory.fac(r)
        return int(n_choose_r)


    def C_args(n, args: list) -> int:
        """Big permutation time"""
        amount = 1
        start = 0
        choose = args[0]

        for number in args[:]:
            if n - start > 0:
                amount *= number_theory.C(n - start, number)
                start += number
            else:
                bool("Kitten")

        return amount


    def increment(x, y) -> int:
        """This function increments x by y."""
        return x + y


    def fib(n, memo = None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]

        if n < 2:
            return n
        memo[n] = number_theory.fib(n - 1, memo) + number_theory.fib(n - 2, memo)
        return memo[n]


    def triang(n, memo = None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n < 1:
            return 0
        memo[n] = number_theory.triang(n - 1, memo) + n
        return memo[n]


    def odd_sum(n, memo = None):
        if n % 2 == 0:
            raise ValueError("Supposed to be odd number") #Me being a goofy goober
        if memo is None: #Avoids dict getting dragged across calls
            memo = {}
        if n in memo: #If value already computed, return that value
            return memo[n]
        if n < 1: #Base case
            return 0
        memo[n] = number_theory.odd_sum(n - 2, memo) + n #Recursive step
        return memo[n] #Returns up the stack. Is necessary.


    def gcd(a: int, b: int) -> int:
        """A simple function to find the greatest common divisor of two numbers"""
        if b == 0:
            raise ValueError(
                "The Euclidean algorithm only works for values where the divisor is not zero")
        else:
            special_list = [a, b]
            nRemainder: float = 1
            while nRemainder != 0:
                nRemainder = special_list[-2] % special_list[-1]
                special_list.append(nRemainder)
            return special_list[-2]


    def super_gcd(*args) -> int:
        value_list = [number_theory.gcd(args[0],args[1])]
        for i in args:
            if args.index(i) <= 1:
                pass
            elif args.index(i) <= len(args):
                value_list.append(number_theory.gcd((value_list[-1]), i))

        return value_list[-1]


    def lcm(a, b) -> int:
        """A simple function to find the least common multiple of two integers"""
        least = (a * b) / number_theory.gcd(a, b)
        return int(least)


    def manual_prime_test(limit: int) -> list:
        """Manually computes all primes less than a given positive integer"""
        current_num = 2
        prime_list = [2]
        while current_num <= limit:
            if all(current_num % prime != 0 for prime in prime_list):
             prime_list.append(current_num)
            current_num += 1
        return prime_list


    def seive_of_erathosnes(limit: int) -> list:
        nums = list(range(2,limit+1))
        primes = []


        while nums:
            primes.append(nums[0])
            for i in nums:
                if i % primes[-1] == 0:
                    nums.remove(i)
        return primes
    

    def non_negative_divisors(n: int) -> list:
        """Finds em."""
        if n < 0:
            return 0

        divisors = []

        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        return divisors


    def prime_factorisation(n: int) -> str:
       """Factorises all integers up to the maximum value stored in primes.txt
       Currently: 5754571 ~ 5.7 million
       """
       with open("primes.txt", 'r') as p:
           primes = p.read()
           primes = primes.replace(',', '')
           primes = primes.replace('\n', ' ')
           primes = [int (i) for i in primes.split()]

       if n in primes:
           return n
       elif n > primes[-1]:
           print("Primes up to that value are not yet stored")
           return f'{n}'

       elif n == 1:
           return '1'
       else:
           num = n
           factorised = ''
           for i in primes:
               if num > 1:
                   while num % i == 0:
                       factorised += f'{i}x'
                       num /= i
               else:
                   return factorised[:-1]


    def summation(start: int, end: int, lst: list) -> int:
        """pass"""
        tot = 0
        if len(lst) >= end:
            for i in range(start - 1, end):
                tot += lst[i]
        return tot


    def prod(start: int, end: int, lst: list) -> int:
        """pass"""
        tot = 1
        if len(lst) >= end:
            for i in range(start-1, end):
                tot *= lst[i]
        return tot


    def round_to_100(n: float) -> int:
        if n < 50:
            return 0
        elif 100 > n >= 50:
            return 100
        if abs(int(str(n)[-2:])- 100) <= 50:
            return int(str(n)[:-2] + '00') + 100
        else:
            return int(str(n)[:-2] + '00')


def permutate(items: list) -> list:
    """A much, much, much faster permutator than permutate_beta()"""
    permutation = []
    length = len((items))
    new_items = copy.deepcopy(items)
    while len(permutation) < length:
        rand = randint(0, length - len(permutation) - 1)
        item = new_items[rand]
        new_items.pop(rand)
        permutation.append(item)
    return permutation


def permutation_generator(A: list, permutation = None, permutation_list = None):
    """Recursive permutation generation for maximal speed"""
    if permutation is None:
        permutation = []
        permutation_list = []
    if len(A) < 1:
        permutation_list.append(permutation)
    for i in range(len(A)):
        permutation_generator(A[:i] + A[i+1:], permutation + [A[i]], permutation_list)
    return permutation_list


def r_permutation(items: list, r: int) -> list:
    """This function returns an r permutaion of n items where r <= n. Note if r > n the function exits the code."""
    if r < len(items):
        return_list = []
        indexing_list = []
        indexing_length = len(items)
        iteration_counter = 0
        i = 0
        while i <= indexing_length:
            indexing_list.append(i)
            i += 1
        for i in indexing_list:
            iteration_counter += 1
            if iteration_counter <= r and len(return_list) < r:
                take_number = randint(
                    0, indexing_length - len(return_list) - 1)
                return_list.append(items[take_number])
                items.pop(take_number)
            else:
                return return_list
    elif r == len(items):
        return permutate(items)
    elif r > len(items):
        exit(0)


def undertale_print(string: str) -> None:
    """Prints out messages in the generative style of undertale"""
    character = 0
    while character < len(string):
        if string[character] == " ":
            print(string[character], end="", flush=True)
            character += 1
        else:
            print(string[character], end="", flush=True)
            character += 1
            sleep(.05)
    print()


def undertale_print_customTime(string: str,time: float) -> None:
    """Prints out messages in the generative style of undertale"""
    character = 0
    while character < len(string):
        if string[character] == " ":
            print(string[character], end="", flush=True)
            character += 1
        else:
            print(string[character], end="", flush=True)
            character += 1
            sleep(time)
    print()


def undertale_print_pygame(string: str, screen: pygame.Surface) -> None:
    """Prints out messages in the generative style of undertale. \n
    Adjusted version to be compatible with the pygame interface."""
    offset = 0
    text_color = (0, 0, 0)
    letter_list = []
    letter_vars = []
    letter_names = []
    font = pygame.font.Font(None, 48)

    for current_letter_index in range(len(string)):
        letter_list.append(string[current_letter_index])
        letter_vars.append(f"{current_letter_index}")
        letter_names.append(f"{current_letter_index}")

    for vars in letter_vars:
        vars = font.render(f"{string[int(vars)]}", True, text_color)
        screen.blit(vars, (150 + offset, 180))
        pygame.display.flip()
        offset += vars.get_width()
        sleep(.05)
#cleanup_time()

def path_checker(ordered_pairs: list) -> int:
    """
    A function to find the number of connections in a list of ordered pairs of numbers.\n
    Do not evaluate this function with anything but lists of ordered pairs of integers
    """
    connection_count = 0
    for i in ordered_pairs:
        check_number = i[1]
        for j in ordered_pairs:
            if j[0] == check_number:
                connection_count += 1
    return connection_count


def find_one_path(graph: list) -> list:
    """This function finds the first path in a list of ordered nodes.\n
    Starting from the first one."""
    path_list = [graph[0]]
    for i in graph:
        for j in graph:
            if i[1] == j[0] and i != j and path_list[-1][1] == j[0] and j not in path_list:
                path_list.append(j)
    return path_list


def explore(graph: list,start_node: int) -> list:
    """This function finds the first path in a list of ordered nodes.\n
    Starting from the value of the second input."""
    path_list = [graph[start_node]]
    start = graph.index(graph[start_node])
    for i in graph[start:]:
        for j in graph[start:]:
            if i[1] == j[0] and i != j and path_list[-1][1] == j[0] and j not in path_list:
                path_list.append(j)
    return path_list


def explore_from(graph: list,start_node: int,search_start: int) -> list:
    """This function finds the first path in a list of ordered nodes.\n
    Starting from the value of the second input."""
    path_list = [graph[start_node]]
    for i in graph[search_start:]:
        for j in graph[search_start:]:
            if i[1] == j[0] and i != j and path_list[-1][1] == j[0] and j not in path_list:
                path_list.append(j)
    return path_list


def explore_from2(graph: list,start_node: int,search_start: int,depth: int) -> list:
    """This function finds the first path in a list of ordered nodes.\n
    Starting from the value of the second input."""
    path_list = [graph[start_node]]
    for j in graph[search_start:]:
        if path_list[-1][1] == j[0] and j not in path_list and len(path_list) <= depth:
           path_list.append(j)
    return path_list


def list_indexer(input_list: list, list_index: int) -> list:
    """
    This function accepts a list and a number to index it with.\n 
    Storing it and its index in a list where the first entrt is the\n
    list input, and the second is the index input
    """
    return [input_list,list_index]


def path_finder(graph: list) -> list:
    """Finds all of them"""
    upper_bound = len(graph)
    return_list = []
    i = 0
    index = []
    while i <= upper_bound:
        index.append(i)
        i += 1
    for q in index:
        for j in index:
            for k in index:
                try:
                    if explore_from2(graph,q,j,k) not in return_list:
                        return_list.append(explore_from2(graph,q,j,k))
                except IndexError:
                    pass
    return return_list


def cartesian_product(List1: set, List2: set) -> set:
    """Takes the cartesian product of two sets"""
    cartesian_set = set()
    for i in List1:
        for j in List2:
            cartesian_set.add(tuple([i, j]))
    return cartesian_set


def cartesian_product_for_listy_lists(List1: list, List2: list) -> list:
    """Takes the cartesian product of two listy lists."""
    cartesian_list = []
    for i in List1:
        for j in List2:
            cartesian_list += [[i,j]]
    return cartesian_list


def rev_slice(word: str) -> str:
    """Reverses the letters in a string"""
    reversedWord = ""
    for i in range(len(word)):
        reversedWord += f"{word[-i-1]}"
    return reversedWord


def count_zeroes(num) -> int:
    """Counts the number of zeroes which show up in a number"""
    if len(str(num)) == 1 and str(num)[-1] != '0':
        return 0
    elif str(num)[0] == "0" and len(str(num)) > 1:
        return 1 + count_zeroes((str(num)[1:]))
    elif len(str(num)) == 1 and str(num)[-1] == '0':
        return 1
    return count_zeroes((str(num)[1:]))


def digit_sum(num) -> int:
    """Adds the digits in a number"""
    if len(str(num)) == 0:
        return 0
    return int(str(((num)))[0]) + digit_sum((str(num))[1:])


def subsets(nums, path = []):
    """Takes all \"Subsets\" of a list"""
    return_list = []
    return_list.append(path)
    for i in range(len(nums)):
        sub_results = subsets(nums[i+1:], path + [nums[i]] )
        return_list.extend(sub_results)
    return return_list


def subsets_of_size(nums, size: int) -> list:
    """Takes all \"Subsets\" of a list of specified size"""
    return_list = []
    for i in subsets(nums):
        if len(i) == size:
            return_list.append(i)

    return return_list


def nearest_10(num) -> int:
    """rounds"""
    last_digit = abs(num) % 10
    sgn = num / abs(num)
    if sgn == 1:
        if last_digit < 5:
            return num - last_digit
        elif last_digit >= 5:
            return num + last_digit
    elif sgn == -1:
        if last_digit < 5:
            return num + last_digit
        elif last_digit >= 5:
            return num - last_digit
    else:
        raise ValueError("Unkown error on line 99999")


def count_item_in_list(item, lst) -> int:
    """Finds how many items of a given kind are in a list"""
    len_list = [x for x in lst if x == item]
    

    return len(len_list)


def count_itemS_in_list(items: list, lst: list) -> int:
    items_count = 0
    for i in items:
        items_count += count_item_in_list(i, lst)

    return items_count


def count_itemS_in_list(items: list, lst: list) -> int:
    items_count = 0
    for i in items:
        items_count += count_item_in_list(i, lst)

    return items_count


def score_eval_BJ(cards: list) -> int:
    card_value = 0
    new_cards = []
    for card in cards:
        new_cards.append(card.split("_")[0])

    amount_of_aces = new_cards.count("ace")
    print(amount_of_aces)

    for card in cards:
        try:
            if 'ace' not in new_cards and card[:2] != '10':
                card_value += int(card[0])

            elif 'ace' not in new_cards and card[:2] == '10':
                card_value += 10
            
            elif 'ace' in new_cards and card[:2] == '10':
                if card_value + 10 <= 21:
                    card_value += 10
                else:
                    card_value += 0
            
            else:
                if card_value + int(card[0]) > 21 and amount_of_aces > 0:
                    card_value += int(card[0]) - 10
                    amount_of_aces -= 1
                else:
                    card_value += int(card[0])
        except (TypeError, ValueError):
            #print(f"Error on int based card from {card}")
            pass
        card_name = card.split('_')[0]
        try:
            if 'ace' not in new_cards:
                if card_name == 'king' or card_name == 'queen' or card_name == 'jack':
                    card_value += 10
            else:
                if card_name == 'king' or card_name == 'queen' or card_name == 'jack' and card_value + 10 <= 21:
                    card_value += 10
                
                elif card_name == 'ace':
                    if card_value + 11 <= 21:
                        card_value += 11
                    else:
                        card_value += 1
                else:
                    card_value += 0
        except TypeError:
            print("Oh fuck")
    if card_value <= 21:
        return card_value
    
    elif amount_of_aces > 0 and card_value > 21: #I know that checking card value here is not needed but it's intuitive
        for i in range(1,amount_of_aces):
            if (card_value - i * 10) <= 21:
                return card_value - i * 10

    else:
        return "Thats a buss"


def lettre_indexer(lettre: str) -> int:
    """Since lettres are used in chess\n
    it is desirable to have a way to facilement change them\n
    into a useable index for a listylist. \n
    Starts at 0 for a. \n
    Be careful with capital entries when using this function for other projects."""
    return ord(lettre) - ord('a')


class chess:
    """A class for organising chess specific functions."""
    def __init__(self):
        """Pass"""
        pass
    

    def find_index_abiguous_in_list(lst: list, item: list) -> int:
        """Docstring almost as ambiguous as the function!!!\n."""
        index = 0
        for itemss in lst:
            if itemss[0] == item[0] and item[1] == itemss[1]:
                return index
            else:
                index += 1
        return 0


    def get_diagonal_from_square_list(x_entry: int, y_entry: int, direction: str, size: int, lst: list) -> list: #I do not think that this funciton works so dont use it
        """Made for the chess program. Make sure that the list is sorta squarey\n
        This is really going to need to be changed if you don't want it to be exclusively\n
        useful for the chess program \n
        THIS FUNCTION DOES NOT WORK""" #It's hip to be square
        diagonal_list = []
        diagonal_counter = -size
        starting_point = int(f"{x_entry - 1}{y_entry - 1}")
        print(starting_point)
        if direction == 'downwards_left_diagonal':
            while diagonal_counter < len(lst):
                try:
                    diagonal_list.append(lst[starting_point + diagonal_counter])
                    diagonal_counter += size + 1
                except IndexError:
                    diagonal_counter += size + 1
        elif direction == "downwards_right_diagonal":

            pass
        elif direction == "upwards_right_diagonal": #Was orignally supposed to be downwards left but it ended up doing this :)
            diagonal_counter = len(lst) + size
            starting_point = int(f"{x_entry}{y_entry}")
            while diagonal_counter > 0: #I literally just guessed at what values would work.
                try:
                    diagonal_list.append(lst[starting_point + diagonal_counter])
                    diagonal_counter -= size + 1
                except IndexError:
                    diagonal_counter -= size + 1

        return diagonal_list


    def find_diag_in_list2(row_value: int, col_value: int, direction: str, size: int, lst: list) -> list: #Only put square lists
        """SQUARE LISTS ONLY. Directions are named as follows, their functions will be clear by name, \n
        downwards_right , downwards_left , upwards_right , upwards_left \n
        Name us such becuase this is my second attempt to do this.\n
        Remember to add 1.
        """
        better_list = [] #Will have proper rowey rows
        diagonals = []
        row = 0
        while row <= len(lst) / size - 1: #Makes the better lists rows
            better_list.append(lst[row*size:(row + 1)*size - 0])
            row += 1 #This list will make the code bearable to look at

        if direction == "downwards_right": #Absurdly efficient way to find the diagonals. Ignore the excessive indentation.
            for row_index in range(size):  #At least there's no try blocks.
                if row_index >= row_value - 1: #this makes it go downwards
                    for column_index in range(size):
                        if (column_index - col_value) == (row_index - row_value):
                            diagonals.append(better_list[row_index][column_index])

        elif direction == "downwards_left":
            for row_index in range(size):
                if row_index >= row_value - 1: #This makes it go downwards
                    for column_index in range(size):
                        if -(column_index - col_value) == (row_index - row_value) + 2:
                            diagonals.append(better_list[row_index][column_index])

        elif direction == "upwards_right":
            for row_index in range(size):
                if row_index <= row_value - 1: #This makes it go upwards
                    for column_index in range(size):
                        if (column_index - col_value) + 2 == -(row_index - row_value):
                            diagonals.append(better_list[row_index][column_index])
            diagonals = list_flipper(diagonals)

        elif direction == "upwards_left":
            for row_index in range(size):
                if row_index <= row_value - 1: #This makes it go upwards
                    for column_index in range(size):
                        if (column_index - col_value) == (row_index - row_value):
                            diagonals.append(better_list[row_index][column_index])
            diagonals = list_flipper(diagonals) #For looks. Has no effect on iteration when used

        return diagonals


    def find_diag_in_list2_jusqua(row_value: int, row_end: int, col_value: int, direction: str, size: int, lst: list) -> list: #Only put square lists
        """SQUARE LISTS ONLY.\n
           Directions are named as follows, their functions will be clear by name, \n
           downwards_right , downwards_left , upwards_right , upwards_left \n
           Name is such becuase this is my second attempt to do this.\n
           Remember to add 1. \n
           Goes jusqu'a the row specified \n
           Again the entries are like pygame but 1,1 is the start and all are positive integers\n
           The row end is the literal row end i.e. the one which counting down from the top starting at one is inputted as the second argument\n
        """
        better_list = [] #Will have proper rowey rows
        diagonals = []
        row = 0

        while row <= len(lst) / size - 1: #Makes the better lists rows
            better_list.append(lst[row*size:(row + 1)*size - 0])
            row += 1 #This list will make the code bearable to look at

        if direction == "downwards_right": #Absurdly efficient way to find the diagonals. Ignore the excessive indentation.
            for row_index in range(size):  #At least there's no try blocks.
                if row_index >= row_value - 1 and row_index < row_end: #this makes it go downwards
                    for column_index in range(size):
                        if (column_index - col_value) == (row_index - row_value):
                            diagonals.append(better_list[row_index][column_index])

        elif direction == "downwards_left":
            for row_index in range(size):
                if row_index >= row_value - 1 and row_index < row_end: #This makes it go downwards
                    for column_index in range(size):
                        if -(column_index - col_value) == (row_index - row_value) + 2:
                            diagonals.append(better_list[row_index][column_index])

        elif direction == "upwards_right":
            for row_index in range(size):
                if row_index <= row_value - 1 and row_index >= row_end - 1: #This makes it go upwards
                    for column_index in range(size):
                        if (column_index - col_value) + 2 == -(row_index - row_value):
                            diagonals.append(better_list[row_index][column_index])
            diagonals = list_flipper(diagonals)

        elif direction == "upwards_left":
            for row_index in range(size):
                if row_index <= row_value - 1 and row_index >= row_end - 1: #This makes it go upwards
                    for column_index in range(size):
                        if (column_index - col_value) == (row_index - row_value):
                            diagonals.append(better_list[row_index][column_index])
            diagonals = list_flipper(diagonals) #For looks. Has no effect on iteration when used

        return diagonals


    def move_type_checker(cur_pos: list, new_pos: list) -> str:
        """Checks the type of move for the bishop in chess.\n
        Returns are: \n
        downwards_right , downwards_left , upwards_right , upwards_left \n
        Only enter double lists."""
        # lists look like [(lettre from a to h), (number from one to 8)]
        if lettre_indexer(cur_pos[0]) < lettre_indexer(new_pos[0]) and int(cur_pos[1]) > int(new_pos[1]):
            return "downwards_right"
        elif lettre_indexer(cur_pos[0]) > lettre_indexer(new_pos[0]) and int(cur_pos[1]) > int(new_pos[1]):
            return "downwards_left"
        elif lettre_indexer(cur_pos[0]) < lettre_indexer(new_pos[0]) and int(cur_pos[1]) < int(new_pos[1]):
            return "upwards_right"
        elif lettre_indexer(cur_pos[0]) > lettre_indexer(new_pos[0]) and int(cur_pos[1]) < int(new_pos[1]):
            return "upwards_left"
        return "Big old buffer"


    def get_horiz_lst(lst: list, size: int, row: int) -> list:
        """Gets the horiz in list \n
        Starts row index at 1"""
        return lst[(row - 1) *(size): row * size]


    def get_vert_lst(lst: list, size: int, column_idx: int) -> list:
        """Gets the desired column of a list. \n
        Column idx can start at 0"""
        x_index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return list_flipper([square for square in lst if square[0] == x_index_list[column_idx]])


    def get_horizzy_range(chessboard: list, pos: list) -> list:
        """Gets the range for horizzy peices"""
        rangey = []
        for entry in chess.get_horiz_lst(chessboard, 8, 9 - int(pos[1])) + chess.get_vert_lst(chessboard, 8 , lettre_indexer(pos[0])):
            rangey += [entry[:2]]

        return rangey


    def get_diag_range(chessboard: list, pos: list) -> list:
        """Gets the diag range"""
        better_list = [] #Will have proper rowey rows
        row_value = 8 - int(pos[1])
        lst = chessboard
        col_value = lettre_indexer(pos[0])
        diagonals = []
        row = 0
        while row <= len(lst) / 8 - 1: #Makes the better lists rows
            better_list.append(lst[row*8:(row + 1)*8 - 0])
            row += 1 #This list will make the code bearable to look at

        for row_index in range(8):  #At least there's no try blocks.
            if row_index >= row_value - 1: #this makes it go downwards
                for column_index in range(8):
                    if (column_index - col_value) == (row_index - row_value):
                        diagonals.append(better_list[row_index][column_index])

        for row_index in range(8):
            if row_index <= row_value - 1: #This makes it go upwards
                for column_index in range(8):
                    if (column_index - col_value) == (row_index - row_value):
                        diagonals.append(better_list[row_index][column_index])
        diagonals = list_flipper(diagonals) #For looks. Has no effect on iteration when used
        return [x[:2] for x in diagonals] + [x[:2] for x in chess.find_diag_in_list2(9- int(pos[1]), lettre_indexer(pos[0]) + 1, "upwards_right", 8, chessboard)] + [x[:2] for x in chess.find_diag_in_list2(9- int(pos[1]), lettre_indexer(pos[0]) + 1, "downwards_left", 8, chessboard)]


    def lettre_indexer(lettre: str) -> int:
        """Since lettres are used in chess\n
        it is desirable to have a way to facilement change them\n
        into a useable index for a listylist"""
        return ord(lettre) - ord('a')


    def check_vertical_entries(chessboard: list, current_y: str, new_y: str, x_value: str) -> bool:
        """Checks the vertical entries for a chess move in chess \n
        Positional return goes (bool), (string containing move information i.e 'attack' or 'moved') \n
        Check in code to make sure the attacked peice is not that of the one making the move \n
        Also check that attacked peice is in that position moved to"""
        x_index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        x_value = x_index_list[lettre_indexer(x_value)]

        vertical_list = chess.get_vert_lst(chessboard, 8, lettre_indexer(x_value))
        if int(current_y) < int(new_y):
            if all(x[2] == '' for x in vertical_list[int(current_y):int(new_y)-1]) and (chessboard[chess.find_index_abiguous_in_list(chessboard, [x_value, str(new_y)])][2] == '' or chessboard[chess.find_index_abiguous_in_list(chessboard, [x_value, str(new_y)])][2].isupper()):
                return True
        elif int(current_y) > int(new_y) and all(x[2] == '' for x in vertical_list[int(new_y):int(current_y)-1]) and (chessboard[chess.find_index_abiguous_in_list(chessboard, [x_value, str(new_y)])][2] == '' or chessboard[chess.find_index_abiguous_in_list(chessboard, [x_value, str(new_y)])][2].isupper()):
            return True
        if int(current_y) < int(new_y):
            if all(x[2] == '' for x in vertical_list[int(current_y):int(new_y)-1]) and (chessboard[chess.find_index_abiguous_in_list(chessboard, [x_value, str(new_y)])][2] == '' or chessboard[chess.find_index_abiguous_in_list(chessboard, [x_value, str(new_y)])][2].islower()):
                return True
        elif int(current_y) > int(new_y) and all(x[2] == '' for x in vertical_list[int(new_y):int(current_y)-1]) and (chessboard[chess.find_index_abiguous_in_list(chessboard, [x_value, str(new_y)])][2] == '' or chessboard[chess.find_index_abiguous_in_list(chessboard, [x_value, str(new_y)])][2].islower()):
            return True

        return False


    def check_horizontal_entries(chessboard: list, current_x: str, new_x: str, y_value) -> bool:  # Unbroken
        """Checks the horizontal entries for a chess move in chess \n
        Positional return goes (bool), (string containing move information i.e 'attack' or 'moved') \n
        Check in code to make sure the attacked peice is not that of the one making the move \n
        Also check that attacked peice is in that position moved to"""
        horizontals = chess.get_horiz_lst(chessboard, 8, 8 - int(y_value) + 1)
        if all(x[2] == '' for x in horizontals[lettre_indexer(new_x) + 1:lettre_indexer(current_x)]) and lettre_indexer(current_x) > lettre_indexer(new_x):
            return True

        elif all(x[2] == '' for x in horizontals[lettre_indexer(current_x) + 1:lettre_indexer(new_x)]) and lettre_indexer(current_x) < lettre_indexer(new_x):
            return True

        return False


    def get_king_range(chessboard: list, king_pos: list) -> list:
        """Gets the range of spots the king can move to \n
        Will be useful for mate checking"""
        position_list = []
        for positions in chessboard:
            if positions[0] == king_pos[0] and (int(positions[1]) + 1 == int(king_pos[1]) or int(positions[1]) - 1 == int(king_pos[1])): #Above or below
                position_list.append(positions)
            elif positions[1] == king_pos[1] and (lettre_indexer(positions[0]) + 1 == lettre_indexer(king_pos[0]) or lettre_indexer(positions[0]) - 1 == lettre_indexer(king_pos[0])): #left or right
                position_list.append(positions)
            elif abs(lettre_indexer(king_pos[0]) - lettre_indexer(positions[0])) == abs(int(king_pos[1]) - int(positions[1])) and ((lettre_indexer(positions[0]) + 1 == lettre_indexer(king_pos[0]) or lettre_indexer(positions[0]) - 1 == lettre_indexer(king_pos[0])) or ((int(positions[1]) + 1 == int(king_pos[1]) or int(positions[1]) - 1 == int(king_pos[1])))): #on a diagonal
                position_list.append(positions)

        return position_list


    def get_column(lst: list, size: int, column_idx: int) -> list:
        """Gets a column from a list \n
        Column index starts at 1"""
        if len(lst) < size:
            return []
        return [lst[column_idx - 1]] + chess.get_column(lst[size:], size, column_idx)


    def list_rower(lst: list, size: int) -> list:
        """Returns a rowed up version of a list"""
        row_counter = 1
        rowed_list = []
        while row_counter <= len(lst):
            rowed_list.append(lst[row_counter - 1: row_counter - 1 + size])
            lst = lst[size - 1:]
            row_counter += 1
        return rowed_list


    def list_colummer(lst: list, size: int) -> list:
        """Returns a colummed up version of a list"""
        colummy_list = []
        for column_idx in range(1,size + 1):
            colummy_list.append(chess.get_column(lst,size,column_idx))
        return colummy_list


    def matrix_entry_finder(matrix: list, entry, width: int, height: int) -> list:
        """Finds the entry value of a matrix in conventional notaion; \n
        that is, (1,1) is the top left posision. \n
        Note it returns 0 if the entry is not in the matrix. \n
        Nakey lists only. A list of rows or columns will not do \n
        the items must be in the order desired with no extra listystuff going on."""
        rows = chess.list_rower(matrix, width)
        columns = chess.list_colummer(matrix, height)
        entry_idx = 1
        entry_idx_col = 1
        for row in rows: #for the row index
            if entry in matrix: #Checks if the entry is even in the list given
                if entry in row: #If the row is found where the entry is, then no more iteration is needed
                    break
                else: 
                    entry_idx += 1
            else: #If the entry is not in the list, both of these will return as zero making the type mahem that was my other game project a thing of the past.
                entry_idx = 0
                break
        for column in columns: #for the column index
            if entry in matrix:
                if entry in column:
                    break
                else: 
                    entry_idx_col += 1
            else:
                entry_idx_col = 0
                break
        return entry_idx, entry_idx_col


    def manhattan_distance(lst: list,idx1: list, idx2: list, width=8, height=8) -> list:
        """Finds the manhattan distance for square lists"""

        return tuple(list_flipper([abs(chess.matrix_entry_finder(lst, idx1, width, height)[0] - chess.matrix_entry_finder(lst, idx2, width, height)[0]), abs(chess.matrix_entry_finder(lst, idx1, width, height)[1] - chess.matrix_entry_finder(lst, idx2, width, height)[1])]))


    def knight_move_legal(chessboard: list, current_pos: list, new_pos: list) -> bool:
        """Checks if the knight move is legal. \n 
        Returns true if so and false if not"""
        if [current_pos[0], current_pos[1], 'n'] in chessboard:
            current_pos_friendly_time = chess.matrix_entry_finder(chessboard, [current_pos[0], current_pos[1], 'n'], 8, 8)
        elif [current_pos[0], current_pos[1], 'N'] in chessboard:
            current_pos_friendly_time = chess.matrix_entry_finder(chessboard, [current_pos[0], current_pos[1], 'N'], 8, 8)
        new_pos_entry = chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2]
        new_pos_friendly_time = chess.matrix_entry_finder(chessboard, [new_pos[0], new_pos[1], new_pos_entry], 8, 8)
        if (abs(current_pos_friendly_time[0] - new_pos_friendly_time[0]) == 2 and 1 == abs(current_pos_friendly_time[1] - new_pos_friendly_time[1])) or (abs(current_pos_friendly_time[1] - new_pos_friendly_time[1]) == 2 and 1 == abs(current_pos_friendly_time[0] - new_pos_friendly_time[0])):
            return True
        return False
    

    def get_knight_range(chessboard: list, current_pos: list) -> list:
        """Gets the knights range"""
        x_index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        rangey = []
        if lettre_indexer(current_pos[0]) + 1 < 8 and int(current_pos[1]) + 2 <= 8:

            rangey.append([x_index_list[(lettre_indexer(current_pos[0]) + 1)], f"{int(current_pos[1]) + 2}"])

        if lettre_indexer(current_pos[0]) + 1 < 8 and int(current_pos[1]) - 2 <= 8:

            rangey.append([x_index_list[(lettre_indexer(current_pos[0]) + 1)], f"{int(current_pos[1]) - 2}"])

        if lettre_indexer(current_pos[0]) - 1 < 8 and int(current_pos[1]) + 2 <= 8:

            rangey.append([x_index_list[(lettre_indexer(current_pos[0]) - 1)], f"{int(current_pos[1]) + 2}"])

        if lettre_indexer(current_pos[0]) - 1 < 8 and int(current_pos[1]) - 2 <= 8:

            rangey.append([x_index_list[(lettre_indexer(current_pos[0]) - 1)], f"{int(current_pos[1]) - 2}"])

        if lettre_indexer(current_pos[0]) + 2 < 8 and int(current_pos[1]) + 1 <= 8:

            rangey.append([x_index_list[(lettre_indexer(current_pos[0]) + 2)], f"{int(current_pos[1]) + 1}"])

        if lettre_indexer(current_pos[0]) + 2 < 8 and int(current_pos[1]) - 1 <= 8:

            rangey.append([x_index_list[(lettre_indexer(current_pos[0]) + 2)], f"{int(current_pos[1]) - 1}"])

        if lettre_indexer(current_pos[0]) - 2 < 8 and int(current_pos[1]) + 1 <= 8:

            rangey.append([x_index_list[(lettre_indexer(current_pos[0]) - 2)], f"{int(current_pos[1]) + 1}"])

        if lettre_indexer(current_pos[0]) - 2 < 8 and int(current_pos[1]) - 1 <= 8:

            rangey.append([x_index_list[(lettre_indexer(current_pos[0]) - 2)], f"{int(current_pos[1]) - 1}"])

        return rangey


    def findpeice(chessboard: list, peice_pos: list) -> str:
        """Finds the peice where it is"""
        return chessboard[chess.find_index_abiguous_in_list(chessboard, peice_pos)][2]


    def get_pawn_range(chessboard: list, pawn_pos: list) -> list:
        """Gets the pawn range"""
        x_index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        pawn_range = []
        pawn_type = chess.findpeice(chessboard, pawn_pos)
        if pawn_type.lower() != 'p':
            return []

        if pawn_type.islower():
            pawn_range.append([pawn_pos[0], str(int(pawn_pos[1]) + 1)])
        elif pawn_type.isupper():
            pawn_range.append([pawn_pos[0], str(int(pawn_pos[1]) - 1)])

        #For white here.
        if pawn_type == 'p' and pawn_pos[0] == 'h':
            if pawn_pos[1] == '2':
                pawn_range.append([pawn_pos[0], str(int(pawn_pos[1]) + 2)])
                pawn_range.append(['g', str(int(pawn_pos[1]) + 1)])
            else:
                pawn_range.append(['g', str(int(pawn_pos[1]) + 1)])
        elif pawn_type == 'p' and pawn_pos[0] == 'a':
            if pawn_pos[1] == '2':
                pawn_range.append([pawn_pos[0], str(int(pawn_pos[1]) + 2)])
                pawn_range.append(['b', str(int(pawn_pos[1]) + 1)])
            else:
                pawn_range.append(['b', str(int(pawn_pos[1]) + 1)])
        elif pawn_type == 'p':
            if pawn_pos[1] == '2':
                pawn_range.append([pawn_pos[0], str(int(pawn_pos[1]) + 2)])
                pawn_range.append([x_index_list[x_index_list.index(pawn_pos[0]) - 1], str(int(pawn_pos[1]) + 1)])
                pawn_range.append([x_index_list[x_index_list.index(pawn_pos[0]) + 1], str(int(pawn_pos[1]) + 1)])
            else:
                pawn_range.append([x_index_list[x_index_list.index(pawn_pos[0]) - 1], str(int(pawn_pos[1]) + 1)])
                pawn_range.append([x_index_list[x_index_list.index(pawn_pos[0]) + 1], str(int(pawn_pos[1]) + 1)])
        #For black below
        if pawn_type == 'P' and pawn_pos[0] == 'h':
            if pawn_pos[1] == '7':
                pawn_range.append([pawn_pos[0], str(int(pawn_pos[1]) - 2)])
                pawn_range.append(['g', str(int(pawn_pos[1]) - 1)])
            else:
                pawn_range.append(['g', str(int(pawn_pos[1]) - 1)])
        elif pawn_type == 'P' and pawn_pos[0] == 'a':
            if pawn_pos[1] == '7':
                pawn_range.append([pawn_pos[0], str(int(pawn_pos[1]) - 2)])
                pawn_range.append(['b', str(int(pawn_pos[1]) - 1)])
            else:
                pawn_range.append(['b', str(int(pawn_pos[1]) - 1)])
        elif pawn_type == 'P':
            if pawn_pos[1] == '7':
                pawn_range.append([pawn_pos[0], str(int(pawn_pos[1]) - 2)])
                pawn_range.append([x_index_list[x_index_list.index(pawn_pos[0]) - 1], str(int(pawn_pos[1]) - 1)])
                pawn_range.append([x_index_list[x_index_list.index(pawn_pos[0]) + 1], str(int(pawn_pos[1]) - 1)])
            else:
                pawn_range.append([x_index_list[x_index_list.index(pawn_pos[0]) - 1], str(int(pawn_pos[1]) - 1)])
                pawn_range.append([x_index_list[x_index_list.index(pawn_pos[0]) + 1], str(int(pawn_pos[1]) - 1)])
    
        return pawn_range


    def possible_moves(chessboard: list, turn: str = 'white'):
        """Returns the possible moves for a player to make on their turn. \n
        Optimised to limit list size significantly. \n
        Size will likely never superceed 100."""
        diagonals = ['q', 'b']
        horizontals = ['r', 'q']
        possible_moves = []        
        for peice in chessboard:
            horizontal = False
            diagonal = False
            proper_turn = False
            if turn == 'white':
                proper_turn = bool(peice[2].islower())
            elif turn == 'black':
                proper_turn = bool(peice[2].isupper())
            if proper_turn:
                if turn == 'white' and proper_turn:
                    for peice2 in chessboard:
                        if peice[2].lower() in horizontals:
                            horizontal = bool(peice[1] == peice2[1] or peice[0] == peice2[0])
                        if peice[2].lower() in diagonals:
                            diagonal = bool(abs(lettre_indexer(peice[0]) - lettre_indexer(peice2[0])) == abs(int(peice[1]) - int(peice2[1])))
                        bad = bool(peice2[2].islower()) #No friendly fire
                        if peice[2] == 'p' and peice2[:-1] in chess.get_pawn_range(chessboard, peice) and not bad:
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'k' and peice2 in chess.get_king_range(chessboard, peice) and not bad:
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'n' and not bad and chess.knight_move_legal(chessboard, peice, peice2):
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'r' and not bad and horizontal:
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'b' and not bad and diagonal:
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'q' and not bad and (diagonal or horizontal):
                            possible_moves.append([peice, peice2])

                elif turn == 'black' and proper_turn:
                    for peice2 in chessboard:
                        if peice[2].lower() in horizontals:
                            horizontal = bool(peice[1] == peice2[1] or peice[0] == peice2[0])
                        if peice[2].lower() in diagonals:
                            diagonal = bool(abs(lettre_indexer(peice[0]) - lettre_indexer(peice2[0])) == abs(int(peice[1]) - int(peice2[1])))
                        bad = bool(peice2[2].isupper()) #No friendly fire
                        if peice[2] == 'P' and peice2[:-1] in chess.get_pawn_range(chessboard, peice) and not bad:
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'K' and peice2 in chess.get_king_range(chessboard, peice) and not bad:
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'N' and not bad and chess.knight_move_legal(chessboard, peice, peice2):
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'R' and not bad and horizontal:
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'B' and not bad and diagonal:
                            possible_moves.append([peice, peice2])
                        elif peice[2] == 'Q' and not bad and (diagonal or horizontal):
                            possible_moves.append([peice, peice2])
        return possible_moves


    def board_printer(board: list, x_index_list=[]) -> None:
        """It prints the whole chessboard no matter what state it is in.\n
        It prints it generatively becuase I like it that way :)"""
        print("8", end="   ")
        for entry in board:
            if entry[0] != 'h':
                if entry[2] == '':
                    print("□", end="    ", flush=True)
                    sleep(.01)

                else:
                    print(entry[2], end="    ", flush=True)
                    sleep(.01)
            else:
                if entry[2] == '':
                    print("□", end="\n \n", flush=True)
                    print(int(entry[1]) - 1, end="   ")
                    sleep(.01)

                else:
                    print(entry[2], end="\n \n", flush=True)
                    print(int(entry[1]) - 1, end="   ")
                    sleep(.01)

        print()
        print("    ", end="")
        for lettre in list_flipper(x_index_list):
            print(lettre, end="    ")
        print()


def lists_are_strongly_equal(*args):
    if all(len(x) == len(y) for x in args for y in args): #lists are at least all the same size
        starting_index = 0
        for lists in args:
            for checklist in args:
                while starting_index < len(args[0]):
                    if lists[starting_index] != checklist[starting_index]:
                        return False
                    starting_index += 1
            starting_index = 0
    else:
        return False

    return True


def randomhex():
    """Generates a random hexidecimal colour"""
    alphabet = ['a','b','d','e','f']
    alpha_or_num = randint(0,1)
    hex_code = ""
    while len(hex_code) < 6:
        if alpha_or_num == 0:
            hex_code += alphabet[randint(0,4)]
        else:
            hex_code += f"{randint(0,9)}"
    return f"#{hex_code}"


def nearest_10(num: int):
    """Returns the value of num rounded to the nearest multiple of 10.
    If the last digit in num is 5, it gets rounded to the multiple of 10 farther away from zero.
    """
    if num < 0:
        negative = True
        num = -num
    else:
        negative = False
    if not negative:
        if num % 10 <= 4:
            return num - (num % 10)
        elif num % 10 >= 6:
            return num + (10 - (num % 10))
        else:
            return num + 5
    elif negative:
        if num % 10 <= 4:
            return -(num - (num % 10))
        elif num % 10 >= 6:
            return -(num + (10 - (num % 10)))
        else:
            return -(num + 5)


def powerset(lst: list, currentset: list = None, powerset_: list = None) -> list:
    """Makes the powerset"""
    if powerset_ is None:
        powerset_ = []
        currentset = []
    if not lst:
        powerset_.append(currentset)
    for i in range(len(lst)):
        powerset(lst[i+1:], currentset + [lst[i]], powerset_)
    return powerset_


class superlist(list):
    """Lists with extra functionality"""
    def __init__(self, args= tuple()):
        super().__init__(args or [])
        self.args = args


    def __str__(self):
        return f"{list(self.args)}"
    

    def __getitem__(self, index: int):
        return self.args[index]
    

    def index(self, item) -> int:
        return self.args.index(item)


    def len(self):
        return len(self.args)


    def append(self, item):
        self.args = self.args + (item,)


    def replace(self, item1, item2):
        if item1 not in self:
            raise ValueError
        else:
            new = tuple()
            for i in self.args:
                if i == item1:
                    new += (item2,)
                else:
                    new += (i,)
        self.args = new  


    def what_there(self, pos: list):
        """Finds what is at a matrix valued entry in the list if the entries are like [i, j, val]"""

        for i in self.args:
            if i[:2] == pos:
                return i[2]
        return None #If entry not in the list.


class superdict(dict):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        super().__init__(kwargs or {})


    def __str__(self):
        return f"{self.kwargs}"
    

    def __getitem__(self, key):
        return self.kwargs[key]
    

    def addkey(self, key, val) -> None:
        if key in self.kwargs:
            raise KeyError("Cannot assign two values to one key")
        elif type(key) == list:
            raise TypeError("Type list is not hashable")
        else:
            self.kwargs[key] = val

    
    def __len__(self):
        return __builtins__.len(self.kwargs)


    def dictionary_inserter(dkt, idx: int, new_key, new_key_val) -> dict: #Super awesome function
        """Inserts a key into a dicitonary at a specific entry \n
        If a key exists at the index, it will be pushed up in the dictionary. Not down. \n
        Note indexes are programming indexes. Starting from 0 to be imputted first, 1 to be just after the first and so on.\n
        All index values superceeding the length of the dictionary will have the new key and its value placed at the end."""
        if len(dkt) + 1 <= idx: #Is just going to put the value at the end.
            idx = len(dkt)
        if type(new_key) == list: #To warn the coder that an illegal key was attempted to be inserted into the new dictionary
            raise TypeError("Unhashable type list cannot be made dictionary key.")

        listy_dict = list(dkt) #Gets a list of the keys
        if idx != 0 and idx != len(dkt):
            key_at_idx = listy_dict[idx] #The key at the index just before, since lists start at 0.
        new_dict = {}

        if idx != 0 and idx != len(dkt): #Place item in between
            for key, key_val in dkt.items():
                if key != key_at_idx:
                    new_dict[key] = key_val
                else:
                    new_dict[new_key] = new_key_val
                    new_dict[key] = key_val
        elif idx == 0: #Place item at the start
            new_dict[new_key] = new_key_val
            for key, key_val in dkt.items():
                new_dict[key] = key_val
        elif idx == len(dkt): #Place item at the end
            for key, key_val in dkt.items():
                new_dict[key] = key_val
            new_dict[new_key] = new_key_val

        return new_dict


    def key_swapper(dkt: dict, oldkey, newkey) -> dict: #As efficient as it gets
        """Swaps the keys for the same entry in a dict"""
        return superdict.dictionary_inserter(dkt, list(dkt).index(oldkey), newkey, dkt.pop(oldkey))


def dictionary_flipper(dkt: dict, new_dict = None) -> dict:
    """IT FLIPS THE DICT"""
    if new_dict is None:
        new_dict = {}

    if len(dkt) < 1:
        return new_dict

    new_dict[list(dkt)[-1]] = dkt[list(dkt)[-1]]

    del dkt[list(dkt)[-1]]
    return superdict.dictionary_flipper(dkt, new_dict)

def dictionary_inserter(dkt, idx: int, new_key, new_key_val) -> dict: #Super awesome function
    """Inserts a key into a dicitonary at a specific entry \n
    If a key exists at the index, it will be pushed up in the dictionary. Not down. \n
    Note indexes are programming indexes. Starting from 0 to be imputted first, 1 to be just after the first and so on.\n
    All index values superceeding the length of the dictionary will have the new key and its value placed at the end."""
    if len(dkt) + 1 <= idx: #Is just going to put the value at the end.
        idx = len(dkt)
    if type(new_key) == list: #To warn the coder that an illegal key was attempted to be inserted into the new dictionary
        raise TypeError("Unhashable type list cannot be made dictionary key.")

    listy_dict = list(dkt) #Gets a list of the keys
    if idx != 0 and idx != len(dkt):
        key_at_idx = listy_dict[idx] #The key at the index just before, since lists start at 0.
    new_dict = {}

    if idx != 0 and idx != len(dkt): #Place item in between
        for key, key_val in dkt.items():
            if key != key_at_idx:
                new_dict[key] = key_val
            else:
                new_dict[new_key] = new_key_val
                new_dict[key] = key_val
    elif idx == 0: #Place item at the start
        new_dict[new_key] = new_key_val
        for key, key_val in dkt.items():
            new_dict[key] = key_val
    elif idx == len(dkt): #Place item at the end
        for key, key_val in dkt.items():
            new_dict[key] = key_val
        new_dict[new_key] = new_key_val

    return new_dict


def key_swapper(dkt: dict, oldkey, newkey) -> dict: #As efficient as it gets
    """Swaps the keys for the same entry in a dict"""
    return superdict.dictionary_inserter(dkt, list(dkt).index(oldkey), newkey, dkt.pop(oldkey))


def dictionary_flipper(dkt: dict, new_dict = None) -> dict:
    """IT FLIPS THE DICT"""
    if new_dict is None:
        new_dict = {}

    if len(dkt) < 1:
        return new_dict

    new_dict[list(dkt)[-1]] = dkt[list(dkt)[-1]]

    del dkt[list(dkt)[-1]]
    return superdict.dictionary_flipper(dkt, new_dict)
