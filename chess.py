"""This module stimulates janky af chess in the python terminal"""
import copy
from time import sleep
from functions import undertale_print, cartesian_product_for_listy_lists, lists_are_strongly_equal, chess
from experiments import list_flipper, item_replacer
from random import randint
import traceback
x_index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
y_index_list = ['1', '2', '3', '4', '5', '6', '7', '8']
x_index_list = list_flipper(x_index_list)
blk_start_row = ['r', 'k', 'b', 'q', 'k', 'b', 'k', 'r']
castling_poses_b = [['c', '8'], ['g', '8']]
castling_poses_w = [['c', '1'], ['g', '1']]
wht_start_row = (blk_start_row.copy())
these_functions_are_useful = False
player_king_moved = False
bot_king_moved = False
user_move = 'quit'  # Change this to start the game


def lettre_indexer(lettre: str) -> int:
    """Since lettres are used in chess\n
    it is desirable to have a way to facilement change them\n
    into a useable index for a listylist"""
    return ord(lettre) - ord('a')


def cleanup_time() -> None:
    print("\x1b[2J\x1b[H", end="")
cleanup_time()


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


def check_diagonal_entries(chessboard: list, current_pos: list, new_pos: list) -> bool:
    """Checks the diagonal entries of the chessboard between one spot and another"""
    if abs(lettre_indexer(current_pos[0]) - lettre_indexer(new_pos[0])) == abs(int(current_pos[1]) - int(new_pos[1])):
        if move_type_checker(current_pos, new_pos)[:8] == "downwards":
            diagonal_to_check = chess.find_diag_in_list2_jusqua(8 - int(current_pos[1]) + 1, 8 - int(
                new_pos[1]) + 1, lettre_indexer(current_pos[0]) + 1, move_type_checker(current_pos, new_pos), 8, chessboard)
        else:
            diagonal_to_check = chess.find_diag_in_list2_jusqua(8 - int(current_pos[1]) + 1, 8 - int(
                new_pos[1]) + 1, lettre_indexer(current_pos[0]) + 1, move_type_checker(current_pos, new_pos), 8, chessboard)
        if all(x[2] == '' for x in diagonal_to_check[1:-1]):
            return True
        else:
            return False
    return False


def is_castling(chessboard: list, first_pos: list, new_pos: list) -> bool:
    """Checks if the move is a castle, and if the king is there etc \n
    Completely auxilary castle check. \n
    \n.\nDO NOT ENTER THE FULL PEICE. ONLY THE FIRST TWO COORDINATES!!! \n.\n"""
    # For player
    # print("Castling function called. Poses are", first_pos, new_pos)
    if first_pos[1] == new_pos[1] == '8' or first_pos[1] == new_pos[1] == '1':
        if not player_king_moved:  # If the player hasn't moved his king
            # Specifically lowercase
            if chessboard[chess.find_index_abiguous_in_list(chessboard, first_pos)][2] == 'k' and first_pos[0] == 'e' and first_pos[1] == '1' == new_pos[1]:
                # Checks the horizontal entries
                if check_horizontal_entries(chessboard, first_pos[0], new_pos[0], first_pos[1]):
                    if new_pos == ['c', '1']:  # Left side castle
                        # The rook is where he must to be.
                        if chessboard[chess.find_index_abiguous_in_list(chessboard, ['a', '1'])][2] == 'r':
                            return True

                    elif new_pos == ['g', '1']:  # Right side castle
                        # The rook is where he needs to be
                        if chessboard[chess.find_index_abiguous_in_list(chessboard, ['h', '1'])][2] == 'r':
                            return True  # I love indentation
        if not bot_king_moved:
            # Specifically lowercase
            if chessboard[chess.find_index_abiguous_in_list(chessboard, first_pos)][2] == 'K' and first_pos[0] == 'e' and first_pos[1] == '8' == new_pos[1]:
                # Checks the horizontal entries
                if check_horizontal_entries(chessboard, first_pos[0], new_pos[0], first_pos[1]):
                    if new_pos == ['c', '8']:  # Left side castle

                        # The rook is where he must to be.
                        if chessboard[chess.find_index_abiguous_in_list(chessboard, ['a', '8'])][2] == 'R':
                            return True

                    elif new_pos == ['g', '8']:  # Right side castle
                        # The rook is where he needs to be
                        if chessboard[chess.find_index_abiguous_in_list(chessboard, ['h', '8'])][2] == 'R':
                            return True  # I love indentation

    return False


def add_standard_space() -> None:  # This function is used once
    return "    "


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


def board_maker(xs: list, ys: list) -> list:
    """Makes a triple indexed list for the board positions \n
    Uses the same positionings as a regular chess board."""
    board = []
    current_row = []
    for y_index in ys:
        for x_index in xs:
            current_row.append([x_index, y_index, ''])

        board.append(current_row)

    # I have no idea why it makes the chessboard so many times :)
    return list_flipper(board[0])


def starting_board_maker(indexed_board: list) -> list:  # It just makes the board
    """Makes the starting board for chess"""

    # Gets something like [string, numbered index (type string), '']
    for index in range(len(indexed_board)):
        entry = indexed_board[index]
        if (entry[0] == 'a' or entry[0] == 'h') and (entry[1] == '1' or entry[1] == '8'):
            # I made this function. It's sooper cool
            indexed_board = item_replacer(
                indexed_board, [entry[0], entry[1], 'r'], index + 1)

        elif (entry[0] == 'b' or entry[0] == 'g') and (entry[1] == '1' or entry[1] == '8'):
            indexed_board = item_replacer(
                indexed_board, [entry[0], entry[1], 'n'], index + 1)

        elif (entry[0] == 'c' or entry[0] == 'f') and (entry[1] == '1' or entry[1] == '8'):
            indexed_board = item_replacer(
                indexed_board, [entry[0], entry[1], 'b'], index + 1)

        elif (entry[0] == 'd') and (entry[1] == '1' or entry[1] == '8'):
            indexed_board = item_replacer(
                indexed_board, [entry[0], entry[1], 'q'], index + 1)

        elif (entry[0] == 'e') and (entry[1] == '1' or entry[1] == '8'):
            indexed_board = item_replacer(
                indexed_board, [entry[0], entry[1], 'k'], index + 1)

        elif entry[1] == '2' or entry[1] == '7':
            indexed_board = item_replacer(
                indexed_board, [entry[0], entry[1], 'p'], index + 1)

        else:
            pass

    return indexed_board


def starting_board_fixer(indexed_board: list) -> list:  # Capitalises black peices
    """Fixes the board for differentiation between blacks and whites"""
    for entry_index in range(len(indexed_board)):
        entry = indexed_board[entry_index]
        if entry[1] == '8' or entry[1] == '7':
            # print(f"Entry is {entry}")
            indexed_board = item_replacer(
                indexed_board, [entry[0], entry[1], entry[2].upper()], entry_index + 1)
            # print(indexed_board[entry_index])

    return indexed_board
chessboard = (board_maker(x_index_list, y_index_list))
chessboard = starting_board_maker(chessboard)


chessboard = (starting_board_fixer(chessboard))  # chessboard finalized here
previous_board_state = copy.deepcopy(chessboard)
board_states = [previous_board_state]

clefted_board = []
for peice in chessboard:
    clefted_board.append(peice[:2])

clefted_board2 = clefted_board.copy()

all_possible_moves_to_make = cartesian_product_for_listy_lists(
    clefted_board, clefted_board2)  # Ith for the bot

def findpeice(chessboard: list, peice_pos: list) -> str:
    """Finds the peice where it is"""
    return chessboard[chess.find_index_abiguous_in_list(chessboard, peice_pos)][2]



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


def move_the_pawn(index: list,  place_to_move_her: list, chessboard: list) -> list:
    """SHE MOVES THE PAWN\n
    OH YEAH\n
    Careful with the input of strings since the ord function differentiates capital vs lowercase """
    x_index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                    # Buffer may not be needed after some bug fixes but Idunno, I think I'm gonna keep it just in case
                    'buffer at index 8']
    # Makes everything list-coordinate friendly.
    current_x = lettre_indexer(index[0])
    # These are proper indexes, not intuitive ones.
    new_x = ord(place_to_move_her[0]) - ord("a")
    # Inconsistent use of the lettre_indexer function for funsies #Very useful line comment about the line comment
    if place_to_move_her in chess.get_pawn_range(chessboard, index):
        # If the peice at the current spot is of the players kind
        if chessboard[chess.find_index_abiguous_in_list(chessboard, [index[0], index[1]])][2] == 'p':
            # print([chess.find_index_abiguous_in_list(chessboard, [index[0], index[1]])])
            # Now we get to try and move the peices and see if I actually know what I am doing or not
            if chessboard[chess.find_index_abiguous_in_list(chessboard, [place_to_move_her[0], place_to_move_her[1]])][2] == '' and new_x == current_x and ((int(index[1]) + 1 == int(place_to_move_her[1])) or (index[1] == '2' and place_to_move_her[1] == '4' and chessboard[chess.find_index_abiguous_in_list(chessboard, [index[0], '3'])][2] == '')):
                # print([chess.find_index_abiguous_in_list(chessboard, [place_to_move_her[0], place_to_move_her[1]])])

                chessboard = item_replacer(chessboard, [place_to_move_her[0], place_to_move_her[1], 'p'], chess.find_index_abiguous_in_list(
                    chessboard, [place_to_move_her[0], place_to_move_her[1]]) + 1)
                chessboard = item_replacer(chessboard, [index[0], index[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [index[0], index[1]]) + 1)

            elif int(index[1]) + 1 <= 8 and int(place_to_move_her[1]) - 1 == int(index[1]) and (x_index_list[x_index_list.index(index[0]) + 1] == place_to_move_her[0] or x_index_list[x_index_list.index(index[0]) - 1] == place_to_move_her[0]):  # Diagonal
                if index[0] != 'h':  # For captures
                    if (chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) + 1], f"{int(index[1]) + 1}"])][2] != '' or chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) + 1}"])][2] != '') and ((chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) + 1], f"{int(index[1]) + 1}"])][2].isupper() and place_to_move_her == [x_index_list[x_index_list.index(index[0]) + 1], f"{int(index[1]) + 1}"]) or chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) + 1}"])][2].isupper() and place_to_move_her == [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) + 1}"]):  # Auto formatter didn't even know what to do with this
                        chessboard = item_replacer(chessboard, [place_to_move_her[0], place_to_move_her[1], 'p'], chess.find_index_abiguous_in_list(
                            chessboard, [place_to_move_her[0], place_to_move_her[1]]) + 1)
                        chessboard = item_replacer(chessboard, [index[0], index[1], ''], chess.find_index_abiguous_in_list(
                            chessboard, [index[0], index[1]]) + 1)
                        return chessboard
                elif chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) + 1}"])][2] != '' and chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) + 1}"])][2].isupper() and index[0] == 'h':
                    chessboard = item_replacer(chessboard, [place_to_move_her[0], place_to_move_her[1], 'p'], chess.find_index_abiguous_in_list(
                        chessboard, [place_to_move_her[0], place_to_move_her[1]]) + 1)
                    chessboard = item_replacer(chessboard, [index[0], index[1], ''], chess.find_index_abiguous_in_list(
                        chessboard, [index[0], index[1]]) + 1)
                    return chessboard
                #En passant
                if place_to_move_her[1] == '6' and ([place_to_move_her[0], '5', 'P'] not in board_states[-2]) and (([place_to_move_her[0], '5', 'P'] in board_states[-1])):
                    chessboard = item_replacer(chessboard, [place_to_move_her[0], place_to_move_her[1], 'p'], chess.find_index_abiguous_in_list(
                        chessboard, [place_to_move_her[0], place_to_move_her[1]]) + 1)
                    chessboard = item_replacer(chessboard, [index[0], index[1], ''], chess.find_index_abiguous_in_list(
                        chessboard, [index[0], index[1]]) + 1)
                    chessboard = item_replacer(chessboard, [place_to_move_her[0], '5', ''], chess.find_index_abiguous_in_list(
                        chessboard, [place_to_move_her[0], '5']) + 1)
                    return chessboard

        # BOT TURN STARTS HERE!!!!!!!!!!!
        elif chessboard[chess.find_index_abiguous_in_list(chessboard, [index[0], index[1]])][2] == 'P':
            if chessboard[chess.find_index_abiguous_in_list(chessboard, [place_to_move_her[0], place_to_move_her[1]])][2] == '' and new_x == current_x and ((int(index[1]) - 1 == int(place_to_move_her[1])) or (index[1] == '7' and place_to_move_her[1] == '5' and chessboard[chess.find_index_abiguous_in_list(chessboard, [index[0], '6'])][2] == '')):
                chessboard = item_replacer(chessboard, [place_to_move_her[0], place_to_move_her[1], 'P'], chess.find_index_abiguous_in_list(
                    chessboard, [place_to_move_her[0], place_to_move_her[1]]) + 1)
                chessboard = item_replacer(chessboard, [index[0], index[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [index[0], index[1]]) + 1)

            elif int(index[1]) - 1 >= 0 and int(place_to_move_her[1]) + 1 == int(index[1]) and (x_index_list[x_index_list.index(index[0]) + 1] == place_to_move_her[0] or x_index_list[x_index_list.index(index[0]) - 1] == place_to_move_her[0]):
                if index[0] != 'h':
                    if (chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) + 1], f"{int(index[1]) - 1}"])][2] != '' or chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) - 1}"])][2] != '') and ((chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) + 1], f"{int(index[1]) - 1}"])][2].islower() and place_to_move_her == [x_index_list[x_index_list.index(index[0]) + 1], f"{int(index[1]) - 1}"]) or (chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) - 1}"])][2].islower() and place_to_move_her == [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) - 1}"])):
                        chessboard = item_replacer(chessboard, [place_to_move_her[0], place_to_move_her[1], 'P'], chess.find_index_abiguous_in_list(
                            chessboard, [place_to_move_her[0], place_to_move_her[1]]) + 1)
                        chessboard = item_replacer(chessboard, [index[0], index[1], ''], chess.find_index_abiguous_in_list(
                            chessboard, [index[0], index[1]]) + 1)
                        return chessboard
                elif chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) - 1}"])][2] != '' and chessboard[chess.find_index_abiguous_in_list(chessboard, [x_index_list[x_index_list.index(index[0]) - 1], f"{int(index[1]) - 1}"])][2].islower():
                    chessboard = item_replacer(chessboard, [place_to_move_her[0], place_to_move_her[1], 'P'], chess.find_index_abiguous_in_list(
                        chessboard, [place_to_move_her[0], place_to_move_her[1]]) + 1)
                    chessboard = item_replacer(chessboard, [index[0], index[1], ''], chess.find_index_abiguous_in_list(
                        chessboard, [index[0], index[1]]) + 1)
                    return chessboard
                #En passant
                if place_to_move_her[1] == '3' and ([place_to_move_her[0], '4', 'p'] not in board_states[-2]) and (([place_to_move_her[0], '4', 'p'] in board_states[-1])):
                    chessboard = item_replacer(chessboard, [place_to_move_her[0], place_to_move_her[1], 'P'], chess.find_index_abiguous_in_list(
                        chessboard, [place_to_move_her[0], place_to_move_her[1]]) + 1)
                    chessboard = item_replacer(chessboard, [index[0], index[1], ''], chess.find_index_abiguous_in_list(
                        chessboard, [index[0], index[1]]) + 1)
                    chessboard = item_replacer(chessboard, [place_to_move_her[0], '4', ''], chess.find_index_abiguous_in_list(
                        chessboard, [place_to_move_her[0], '4']) + 1)
                    return chessboard

    return chessboard


def move_the_rook(current_pos: list, new_pos: list, chessboard: list) -> list:
    """It moves the rook, gently.\n
    I love this function"""
    if chessboard[chess.find_index_abiguous_in_list(chessboard, [current_pos[0], current_pos[1]])][2] == 'r':
        # print(current_pos[1])
        # print(check_vertical_entries(chessboard, current_pos[1], new_pos[1], current_pos[0]))
        # print(check_horizontal_entries(chessboard, current_pos[1], new_pos[1], current_pos[0]))
        if (check_vertical_entries(chessboard, current_pos[1], new_pos[1], current_pos[0]) and current_pos[0] == new_pos[0]) or (check_horizontal_entries(chessboard, current_pos[0], new_pos[0], current_pos[1]) and current_pos[1] == new_pos[1]):
            if chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2].isupper() or chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2] == '':
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'r'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
    elif chessboard[chess.find_index_abiguous_in_list(chessboard, [current_pos[0], current_pos[1]])][2] == 'R':
        # print(current_pos[1])
        # print(check_vertical_entries(chessboard, current_pos[1], new_pos[1], current_pos[0]))
        # print(check_horizontal_entries(chessboard, current_pos[1], new_pos[1], current_pos[0]))
        if (check_vertical_entries(chessboard, current_pos[1], new_pos[1], current_pos[0]) and current_pos[0] == new_pos[0]) or (check_horizontal_entries(chessboard, current_pos[0], new_pos[0], current_pos[1]) and current_pos[1] == new_pos[1]):
            if chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2].islower() or chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2] == '':
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'R'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
    return chessboard


def move_the_bishop(chessboard: list, current_pos: list, new_pos: list) -> list:
    """Moves the Bishop, audaciously"""
    # current_pos = [current x coordinate, current y coordinate]
    # new_pos =     [desired x coordinate, desired y coordinate]
    # Always remember that both are strs, and x is a lettre from a to h.
    # Note lettre_indexer sets the position of a equal to 0 which may need to be changed for item_replacer

    if chessboard[chess.find_index_abiguous_in_list(chessboard, [current_pos[0], current_pos[1]])][2] == 'b':

        # An extremely compact way to check if the new and old position are on the same diagonal
        if abs(int(current_pos[1]) - int(new_pos[1])) == abs(lettre_indexer(current_pos[0]) - lettre_indexer(new_pos[0])):

            # Does two jobs in one
            if check_diagonal_entries(chessboard, current_pos, new_pos) and (chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2].isupper() or chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2] == ''):
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'b'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)

    # For when the bot plays.
    elif chessboard[chess.find_index_abiguous_in_list(chessboard, [current_pos[0], current_pos[1]])][2] == 'B':

        # An extremely compact way to check if the new and old position are on the same diagonal
        if abs(int(current_pos[1]) - int(new_pos[1])) == abs(lettre_indexer(current_pos[0]) - lettre_indexer(new_pos[0])):

            # Does two jobs in one
            if check_diagonal_entries(chessboard, current_pos, new_pos) and (chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2].islower() or chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2] == ''):
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'B'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
    return chessboard


def move_the_queen(chessboard: list, current_pos: list, new_pos: list) -> list:
    """Moves the queen, regularily"""
    if chessboard[chess.find_index_abiguous_in_list(chessboard, [current_pos[0], current_pos[1]])][2] == 'q':
        if (check_vertical_entries(chessboard, current_pos[1], new_pos[1], current_pos[0]) and current_pos[0] == new_pos[0]) or (check_horizontal_entries(chessboard, current_pos[0], new_pos[0], current_pos[1]) and current_pos[1] == new_pos[1]) or check_diagonal_entries(chessboard, current_pos, new_pos):
            # print(f"Vert is {check_vertical_entries(chessboard, current_pos[1], new_pos[1], current_pos[0])}", f"Horiz is {check_horizontal_entries(chessboard, current_pos[0], new_pos[0], current_pos[1])}", f"Diag is {check_diagonal_entries(chessboard, current_pos, new_pos)}")
            if chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2].isupper() or chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2] == '':
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'q'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
    elif chessboard[chess.find_index_abiguous_in_list(chessboard, [current_pos[0], current_pos[1]])][2] == 'Q':
        if (check_vertical_entries(chessboard, current_pos[1], new_pos[1], current_pos[0]) and current_pos[0] == new_pos[0]) or (check_horizontal_entries(chessboard, current_pos[0], new_pos[0], current_pos[1]) and current_pos[1] == new_pos[1]) or check_diagonal_entries(chessboard, current_pos, new_pos):
            # print(f"Vert is {check_vertical_entries(chessboard, current_pos[1], new_pos[1], current_pos[0])}", f"Horiz is {check_horizontal_entries(chessboard, current_pos[0], new_pos[0], current_pos[1])}", f"Diag is {check_diagonal_entries(chessboard, current_pos, new_pos)}")
            if chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2].islower() or chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2] == '':
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'Q'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
    return chessboard


def move_the_king(chessboard: list, current_pos: list, new_pos: list) -> list:
    """Moves the King, ferociously."""
    global player_king_moved
    global bot_king_moved
    king_range = chess.get_king_range(chessboard, current_pos)
    special_peice = new_pos + [findpeice(chessboard, new_pos)]
    if not is_castling(chessboard, current_pos, new_pos) and special_peice in chess.get_king_range(chessboard, current_pos):
        if chessboard[chess.find_index_abiguous_in_list(chessboard, current_pos)][2] == 'k':
            if king_range[chess.find_index_abiguous_in_list(king_range, new_pos)][2].isupper() or king_range[chess.find_index_abiguous_in_list(king_range, new_pos)][2] == '':
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'k'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
                player_king_moved = True
        elif chessboard[chess.find_index_abiguous_in_list(chessboard, current_pos)][2] == 'K' and new_pos in king_range:
            if king_range[king_range.index(new_pos)][2].islower() or king_range[(king_range.index(new_pos))][2] == '':
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'K'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
                bot_king_moved = True
    else:  # Is castling
        if new_pos == ['c', '1']:
            chessboard = item_replacer(chessboard, [
                                       'e', '1', ''], chess.find_index_abiguous_in_list(chessboard, ['e', '1']) + 1)
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'k'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [
                                       'd', '1', 'r'], chess.find_index_abiguous_in_list(chessboard, ['d', '1']) + 1)
            chessboard = item_replacer(chessboard, [
                                       'a', '1', ''], chess.find_index_abiguous_in_list(chessboard, ['a', '1']) + 1)
            player_king_moved = True

        elif new_pos == ['g', '1']:
            chessboard = item_replacer(chessboard, [
                                       'e', '1', ''], chess.find_index_abiguous_in_list(chessboard, ['e', '1']) + 1)
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'k'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [
                                       'f', '1', 'r'], chess.find_index_abiguous_in_list(chessboard, ['f', '1']) + 1)
            chessboard = item_replacer(chessboard, [
                                       'h', '1', ''], chess.find_index_abiguous_in_list(chessboard, ['h', '1']) + 1)
            player_king_moved = True
        # Same thing but for the bot
        if new_pos == ['c', '8']:
            chessboard = item_replacer(chessboard, [
                                       'e', '8', ''], chess.find_index_abiguous_in_list(chessboard, ['e', '8']) + 1)
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'K'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [
                                       'd', '8', 'R'], chess.find_index_abiguous_in_list(chessboard, ['d', '8']) + 1)
            chessboard = item_replacer(chessboard, [
                                       'a', '8', ''], chess.find_index_abiguous_in_list(chessboard, ['a', '8']) + 1)
            bot_king_moved = True

        elif new_pos == ['g', '8']:
            chessboard = item_replacer(chessboard, [
                                       'e', '8', ''], chess.find_index_abiguous_in_list(chessboard, ['e', '8']) + 1)
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'K'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [
                                       'f', '8', 'R'], chess.find_index_abiguous_in_list(chessboard, ['f', '8']) + 1)
            chessboard = item_replacer(chessboard, [
                                       'h', '8', ''], chess.find_index_abiguous_in_list(chessboard, ['h', '8']) + 1)
            bot_king_moved = True

    return chessboard


def move_the_knight(chessboard: list, current_pos: list, new_pos: list) -> list:
    """Moves the knight, clarivoyantly"""
    if chess.knight_move_legal(chessboard, current_pos, new_pos) and chessboard[chess.find_index_abiguous_in_list(chessboard, [current_pos[0], current_pos[1]])][2] == 'n':  # If player turn and peice moves is proper
        # only works for player turn
        if chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2].isupper() or chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2] == '':
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'n'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                chessboard, [current_pos[0], current_pos[1]]) + 1)
    # If bot turn and move is proper
    elif chess.knight_move_legal(chessboard, current_pos, new_pos) and chessboard[chess.find_index_abiguous_in_list(chessboard, [current_pos[0], current_pos[1]])][2] == 'N':
        # Is for the botty wotty
        if chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2].islower() or chessboard[chess.find_index_abiguous_in_list(chessboard, [new_pos[0], new_pos[1]])][2] == '':
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'N'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                chessboard, [current_pos[0], current_pos[1]]) + 1)

    return chessboard


def bot_turn(chessboard: list, all_possible_moves_to_make: list) -> list:
    """Sooper dooper sthmart bot"""
    from random import randint
    x_index_list: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    new_board: list = copy.deepcopy(chessboard)
    new_possible_moves: list = all_possible_moves_to_make.copy()

    while lists_are_strongly_equal(new_board, chessboard):
        if len(new_possible_moves) > 1:
            move_wombo_combo = new_possible_moves[randint(
                0, len(new_possible_moves) - 1)]
            bot_move = chessboard[chess.find_index_abiguous_in_list(
                chessboard, move_wombo_combo[0])]
            bot_movedd = chessboard[chess.find_index_abiguous_in_list(
                chessboard, move_wombo_combo[1])]
            new_possible_moves.remove(move_wombo_combo)

            if len(bot_move) >= 3 and bot_move[2].isupper():
                bot_move = bot_move[:2]
                bot_movedd = bot_movedd[:2]
                try:
                    new_board = move_the_pawn(bot_move, bot_movedd, chessboard)
                    if not lists_are_strongly_equal(chessboard, new_board):
                        break
                except Exception as e:
                    pass
                try:
                    new_board = move_the_rook(bot_move, bot_movedd, chessboard)
                    if not lists_are_strongly_equal(chessboard, new_board):
                        break
                except Exception as e:
                    pass

                try:
                    new_board = move_the_bishop(
                        chessboard, bot_move, bot_movedd)
                    if not lists_are_strongly_equal(chessboard, new_board):
                        break
                except Exception as e:
                    pass

                try:
                    new_board = move_the_queen(
                        chessboard, bot_move, bot_movedd)
                    if not lists_are_strongly_equal(chessboard, new_board):
                        break
                except Exception as e:
                    pass

                try:
                    new_board = move_the_king(chessboard, bot_move, bot_movedd)
                    if not lists_are_strongly_equal(chessboard, new_board):
                        break

                except Exception as e:
                    pass

                try:
                    new_board = move_the_knight(
                        chessboard, bot_move, bot_movedd)
                    if not lists_are_strongly_equal(chessboard, new_board):
                        break
                except Exception as e:
                    pass
        else:
            pass
            print("Uh oh")

    return new_board


def promotion_checker(chessboard: list) -> list:
    """Checks if any promotions must be made before moving on"""
    choices = ['b', 'n', 'q', 'r']
    user_choice = ''
    for peice in chessboard:
        if peice[1] == '8' and peice[2] == 'p':
            while user_choice not in choices:
                user_choice = input("Whadaya want? ")
                if user_choice in choices:
                    chessboard = item_replacer(chessboard, [peice[0], peice[1], f"{user_choice}"], chess.find_index_abiguous_in_list(
                        chessboard, [peice[0], peice[1]]) + 1)
                    break
        elif peice[1] == '1' and peice[2] == 'P':
            chessboard = item_replacer(chessboard, [peice[0], peice[1], choices[randint(
                0, 3)]], 1 + chess.find_index_abiguous_in_list(chessboard, [peice[0], peice[1]]))

    return chessboard


def the_game(user_move, user_movedd, chessboard):  # Sorta
    global board_states
    global player_king_moved
    global bot_king_moved
    if type(user_move) == type(user_movedd) == list and len(user_move) == len(user_movedd) >= 2:
        if findpeice(chessboard, user_move).lower() == 'p':
            chessboard = move_the_pawn(user_move, user_movedd, chessboard)
        elif findpeice(chessboard, user_move).lower() == 'r':
            chessboard = move_the_rook(user_move, user_movedd, chessboard)
        elif findpeice(chessboard, user_move).lower() == 'b':
            chessboard = move_the_bishop(chessboard, user_move, user_movedd)
        elif findpeice(chessboard, user_move).lower() == 'q':
            chessboard = move_the_queen(chessboard, user_move, user_movedd)
        elif findpeice(chessboard, user_move).lower() == 'k':
            chessboard = move_the_king(chessboard, user_move, user_movedd)
        elif findpeice(chessboard, user_move).lower() == 'n':
            chessboard = move_the_knight(chessboard, user_move, user_movedd)
    player_king_moved = True
    bot_king_moved = True
    return chessboard


def move_the_king2(chessboard: list, current_pos: list, new_pos: list, specialtime: bool = False, turn: str = 'white') -> list:
    """Moves the King, ferociously."""
    global player_king_moved
    global bot_king_moved
    #print(player_king_moved, "Avec", current_pos, new_pos)
    if specialtime:
        if turn == 'white':
            player_king_moved = False
        elif turn == 'black':
            bot_king_moved = False
    king_range = chess.get_king_range(chessboard, current_pos)
    peice_there = [new_pos[0], new_pos[1], findpeice(chessboard, new_pos)]
    if not is_castling(chessboard, current_pos, new_pos) and peice_there in king_range:
        if chessboard[chess.find_index_abiguous_in_list(chessboard, current_pos)][2] == 'k':
            if king_range[chess.find_index_abiguous_in_list(king_range, new_pos)][2].isupper() or king_range[chess.find_index_abiguous_in_list(king_range, new_pos)][2] == '':
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'k'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
                player_king_moved = True
        elif chessboard[chess.find_index_abiguous_in_list(chessboard, current_pos)][2] == 'K':
            if king_range[chess.find_index_abiguous_in_list(king_range, new_pos)][2].islower() or king_range[chess.find_index_abiguous_in_list(king_range, new_pos)][2] == '':
                chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'K'], chess.find_index_abiguous_in_list(
                    chessboard, [new_pos[0], new_pos[1]]) + 1)
                chessboard = item_replacer(chessboard, [current_pos[0], current_pos[1], ''], chess.find_index_abiguous_in_list(
                    chessboard, [current_pos[0], current_pos[1]]) + 1)
                bot_king_moved = True
    elif (not isincheck(chessboard, 'white') and chessboard[chess.find_index_abiguous_in_list(chessboard, current_pos)][2].islower()) and is_castling(chessboard, current_pos, new_pos):  # Is castling
        if new_pos == ['c', '1']:
            chessboard = item_replacer(chessboard, [
                                       'e', '1', ''], chess.find_index_abiguous_in_list(chessboard, ['e', '1']) + 1)
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'k'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [
                                       'd', '1', 'r'], chess.find_index_abiguous_in_list(chessboard, ['d', '1']) + 1)
            chessboard = item_replacer(chessboard, [
                                       'a', '1', ''], chess.find_index_abiguous_in_list(chessboard, ['a', '1']) + 1)
            player_king_moved = True

        elif new_pos == ['g', '1']:
            chessboard = item_replacer(chessboard, [
                                       'e', '1', ''], chess.find_index_abiguous_in_list(chessboard, ['e', '1']) + 1)
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'k'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [
                                       'f', '1', 'r'], chess.find_index_abiguous_in_list(chessboard, ['f', '1']) + 1)
            chessboard = item_replacer(chessboard, [
                                       'h', '1', ''], chess.find_index_abiguous_in_list(chessboard, ['h', '1']) + 1)
            player_king_moved = True

    elif (not isincheck(chessboard, 'black') and chessboard[chess.find_index_abiguous_in_list(chessboard, current_pos)][2].isupper()) and is_castling(chessboard, current_pos, new_pos):
        if new_pos == ['c', '8']:
            chessboard = item_replacer(chessboard, [
                                       'e', '8', ''], chess.find_index_abiguous_in_list(chessboard, ['e', '8']) + 1)
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'K'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [
                                       'd', '8', 'R'], chess.find_index_abiguous_in_list(chessboard, ['d', '8']) + 1)
            chessboard = item_replacer(chessboard, [
                                       'a', '8', ''], chess.find_index_abiguous_in_list(chessboard, ['a', '8']) + 1)
            bot_king_moved = True

        elif new_pos == ['g', '8']:
            chessboard = item_replacer(chessboard, [
                                       'e', '8', ''], chess.find_index_abiguous_in_list(chessboard, ['e', '8']) + 1)
            chessboard = item_replacer(chessboard, [new_pos[0], new_pos[1], 'K'], chess.find_index_abiguous_in_list(
                chessboard, [new_pos[0], new_pos[1]]) + 1)
            chessboard = item_replacer(chessboard, [
                                       'f', '8', 'R'], chess.find_index_abiguous_in_list(chessboard, ['f', '8']) + 1)
            chessboard = item_replacer(chessboard, [
                                       'h', '8', ''], chess.find_index_abiguous_in_list(chessboard, ['h', '8']) + 1)
            bot_king_moved = True
            #specialtime = False

    if specialtime:
        if turn == 'white':
            player_king_moved = False
        elif turn == 'black':
            bot_king_moved = False

    #print(bot_king_moved)
    return chessboard


def the_game2(user_move, user_movedd, chessboard):  # Sorta
    """Same as the game but with added restrictions on king castling."""
    global board_states
    if type(user_move) == type(user_movedd) == list and len(user_move) == len(user_movedd) >= 2:
        if findpeice(chessboard, user_move).lower() == 'p':
            chessboard = move_the_pawn(user_move, user_movedd, chessboard)
        elif findpeice(chessboard, user_move).lower() == 'r':
            chessboard = move_the_rook(user_move, user_movedd, chessboard)
        elif findpeice(chessboard, user_move).lower() == 'b':
            chessboard = move_the_bishop(chessboard, user_move, user_movedd)
        elif findpeice(chessboard, user_move).lower() == 'q':
            chessboard = move_the_queen(chessboard, user_move, user_movedd)
        elif findpeice(chessboard, user_move).lower() == 'k':
            chessboard = move_the_king2(chessboard, user_move, user_movedd)
        elif findpeice(chessboard, user_move).lower() == 'n':
            chessboard = move_the_knight(chessboard, user_move, user_movedd)

    return chessboard


def isincheck(chessboard: list, turn: str, testing: bool = False) -> bool:
    """Checks if the king is in check when he is making his turn \n"""
    if testing:
        return False

    global player_king_moved
    global bot_king_moved
    player_king_before = player_king_moved
    bot_king_before = bot_king_moved
    if turn == 'white':
        all_possible_moves = chess.possible_moves(
            chessboard, 'black')
    else: 
        all_possible_moves = chess.possible_moves(
            chessboard, 'white')
    giga_list = []

    for possible_move in all_possible_moves:
        giga_list.append(
            the_game2(possible_move[0][:2], possible_move[1][:2], chessboard))

    if turn == 'white' and any(all(x[2] != 'k' for x in y) for y in giga_list):
        player_king_moved = player_king_before
        bot_king_moved = bot_king_before
        return True
    if turn == 'black' and any(all(x[2] != 'K' for x in y) for y in giga_list):
        player_king_moved = player_king_before
        bot_king_moved = bot_king_before
        return True
    player_king_moved = player_king_before
    bot_king_moved = bot_king_before
    return False

def isincheck2(chessboard: list, turn: str) -> bool:
    """Checks if the king is in check when he is making his turn \n"""
    global player_king_moved
    global bot_king_moved
    player_king_before = player_king_moved
    bot_king_before = bot_king_moved
    if turn == 'white':
        all_possible_moves = chess.possible_moves(
            chessboard, 'black')
    else: 
        all_possible_moves = chess.possible_moves(
            chessboard, 'white')
    giga_list = []

    for possible_move in all_possible_moves:
        giga_list.append(
            the_game2(possible_move[0][:2], possible_move[1][:2], chessboard))

    if turn == 'white' and all(any(x[2] == 'k' for x in y) for y in giga_list):
        player_king_moved = player_king_before
        bot_king_moved = bot_king_before
        return False
    if turn == 'black' and all(any(x[2] == 'K' for x in y) for y in giga_list):
        player_king_moved = player_king_before
        bot_king_moved = bot_king_before
        return False
    player_king_moved = player_king_before
    bot_king_moved = bot_king_before
    return True



def mated3(chessboard: list, player: str = 'white') -> bool:
    """Hopefully checks for mate properly"""
    #We are to check if white is mated
    global player_king_moved
    global bot_king_moved
    player_king_before = player_king_moved
    bot_king_before = bot_king_moved
    if isincheck(chessboard, player): #Is the player even in check?
        posssible_moves1 = chess.possible_moves(chessboard, player)

        for move in posssible_moves1:
            if len(move[0]) > 2:
                move[0] = move[0][:2]
                move[1] = move[1][:2]

            new_board = the_game2(move[0], move[1], chessboard)
            if chessboard != new_board and not isincheck(new_board, player):
                player_king_moved = player_king_before
                bot_king_moved = bot_king_before
                return False #The moment a board state is found making the player not in check the function returns true.
            
        return True #If all checks are passed then the player is mated
    player_king_moved = player_king_before
    bot_king_moved = bot_king_before
    return False


def peice_count(chessboard: list, peice: str) -> bool:
    """Counts how many peices of a given type are on the board and belong to the given player \n
    Make sure to enter the peice capitalised if you want to count how many black has and lowercase for white."""
    count = 0
    for peices in chessboard:
        if peices[2] == peice:
            count += 1
    return count


def stalemated(chessboard: list, turn: str = 'white') -> bool:
    """Checks for the horrible outcome of stalemate"""
    global player_king_moved
    global bot_king_moved
    player_king_before = player_king_moved
    bot_king_before = bot_king_moved
    if not isincheck(chessboard, turn): 
        posssible_moves1 = chess.possible_moves(chessboard, turn)
        for move in posssible_moves1:
            new_board = the_game2(move[0], move[1], chessboard)
            if chessboard != new_board and not isincheck(new_board, turn):
                player_king_moved = player_king_before
                bot_king_moved = bot_king_before
                return False #The moment a board state is found making the player not in check the function returns true.
        return True #If all checks are passed then the player cannot move
    player_king_moved = player_king_before
    bot_king_moved = bot_king_before
    return False


def insufficient_material(chessboard: list) -> bool:
    """Checks for insufficient material mate"""
    material = ['r', 'b', 'q', 'n', 'p']
    sans_bishop = ['r', 'q', 'n', 'p']
    sans_knight = ['r', 'b', 'q', 'p']
    sans_both = ['r', 'q', 'p']
    if all(peice_count(chessboard, peice) == peice_count(chessboard, peice.upper()) == 0 for peice in material) and peice_count(chessboard, 'r') == peice_count(chessboard, 'R') == peice_count(chessboard, 'q') == peice_count(chessboard, 'Q') == 0:
        return True
    elif all(peice_count(chessboard, peice) == peice_count(chessboard, peice.upper()) == 0 for peice in sans_bishop) and (((peice_count(chessboard, 'B') == 1 and peice_count(chessboard, 'b') == 0) or (peice_count(chessboard, 'b') == 1 and peice_count(chessboard, 'B') == 0)) or (peice_count(chessboard, 'B') == 1 == peice_count(chessboard, 'b'))) and peice_count(chessboard, 'r') == peice_count(chessboard, 'R') == peice_count(chessboard, 'q') == peice_count(chessboard, 'Q') == 0:
        return True
    elif all(peice_count(chessboard, peice) == peice_count(chessboard, peice.upper()) == 0 for peice in sans_knight) and (((peice_count(chessboard, 'N') == 1 and peice_count(chessboard, 'n') == 0) or (peice_count(chessboard, 'n') == 1 and peice_count(chessboard, 'N') == 0)) or ((peice_count(chessboard, 'N') == 2 and 0 == peice_count(chessboard, 'n'))) or (peice_count(chessboard, 'N') == 0 and 2 == peice_count(chessboard, 'n'))) and peice_count(chessboard, 'r') == peice_count(chessboard, 'R') == peice_count(chessboard, 'q') == peice_count(chessboard, 'Q') == 0:
        return True
    elif all(peice_count(chessboard, peice) == peice_count(chessboard, peice.upper()) == 0 for peice in sans_both) and ((peice_count(chessboard, 'N') == peice_count(chessboard, 'b') == 1) or (peice_count(chessboard, 'n') == peice_count(chessboard, 'B') == 1)) and peice_count(chessboard, 'r') == peice_count(chessboard, 'R') == peice_count(chessboard, 'q') == peice_count(chessboard, 'Q') == 0:
        return True
    return False


def the_game_veritablement(user_move: list, user_movedd: list, chessboard: list, turn: str = 'white') -> list:
    """It is veritablement the game bro."""
    global board_states
    check1 = copy.deepcopy(chessboard)
    if turn == "white":
        # Assuming we move the peice as is
        special_board = the_game2(user_move, user_movedd, chessboard)
        if not isincheck(special_board, 'white'):
            chessboard = special_board
            if check1 != chessboard:
                previous_board_state = copy.deepcopy(chessboard)
                board_states.append(previous_board_state)

    elif turn == "black":
        # Assuming we move the peice as is
        special_board = the_game2(user_move, user_movedd, chessboard)
        if not isincheck(special_board, 'black'):
            chessboard = special_board
            if check1 != chessboard:
                previous_board_state = copy.deepcopy(chessboard)
                board_states.append(previous_board_state)

    return chessboard


def three_fold_rule(board_states: list) -> bool:
    """Checks if the same position has ocurred three times in a row \n
    If so, then the game will result in a draw"""
    if len(board_states) >= 9:
        if lists_are_strongly_equal(board_states[-9],board_states[-5], board_states[-1]) or lists_are_strongly_equal(board_states[-8], board_states[-4], board_states[-0]):
            return True
    return False

chessboard = [
['a', '8', 'R'], ['b', '8', 'N'], ['c', '8', 'B'], ['d', '8', 'Q'], ['e', '8', 'K'], ['f', '8', 'B'], ['g', '8', 'N'], ['h', '8', 'R'], 

['a', '7', 'P'], ['b', '7', 'P'], ['c', '7', 'P'], ['d', '7', 'P'], ['e', '7', 'P'], ['f', '7', 'P'], ['g', '7', 'P'], ['h', '7', 'P'], 

['a', '6', ''],  ['b', '6', ''],  ['c', '6', ''],  ['d', '6', 'n'],  ['e', '6', ''],  ['f', '6', ''],  ['g', '6', ''],  ['h', '6', ''], 

['a', '5', ''],  ['b', '5', ''],  ['c', '5', ''],  ['d', '5', ''],  ['e', '5', ''],  ['f', '5', ''],  ['g', '5', ''],  ['h', '5', ''], 

['a', '4', ''],  ['b', '4', ''],  ['c', '4', ''],  ['d', '4', ''],  ['e', '4', ''],  ['f', '4', ''],  ['g', '4', ''],  ['h', '4', ''], 

['a', '3', ''],  ['b', '3', ''],  ['c', '3', ''],  ['d', '3', ''],  ['e', '3', ''],  ['f', '3', ''],  ['g', '3', ''],  ['h', '3', ''], 

['a', '2', 'p'], ['b', '2', 'p'], ['c', '2', 'p'], ['d', '2', 'p'], ['e', '2', 'p'], ['f', '2', 'p'], ['g', '2', 'p'], ['h', '2', 'p'], 

['a', '1', 'r'], ['b', '1', 'n'], ['c', '1', 'b'], ['d', '1', 'q'], ['e', '1', 'k'], ['f', '1', 'b'], ['g', '1', 'n'], ['h', '1', 'r']
]


# -----------------

#print(chessboard)

# undertale_print("Welcome to python terminal chess. \n"
#                "Type help to get help, and quit to quit. \n"
#                "These inputs should be placed in the first question i.e. \n"
#                "once you chose a peice to move, you better want to move it.")
#board_printer(chessboard, x_index_list)
while user_move != 'quit':  # This wont even exit it. Isn't that funny?

    user_move = (input("What peice would you like to move: "))

    if user_move != 'quit' and user_move != 'help':  # Plays the game
        user_move = user_move.split()
        user_movedd = (input("Where to? ")).split()
        check1 = chessboard.copy()
        chessboard = the_game_veritablement(
            user_move, user_movedd, chessboard, "white")

        if check1 != chessboard:
            # Gets the state of the board after the bot's move
            previous_board_state = copy.deepcopy(chessboard)
            board_states.append(previous_board_state)

        board_printer(chessboard, x_index_list)

    elif user_move == 'quit':
        cleanup_time()
        exit(0)

    elif user_move == 'help':
        undertale_print(
            "Welcome to python terminal chess. \n"
            "To play is a simple folly. \n"
            "Enter the coordiantes of the peice, starting with the letter, and then the number. \n"
            "then enter, in the same way as before, the coordinates of where you would like to move the peice. \n"
            "If the move is legal, then the program will move your peice as demanded. \n"
            "For clarity, a proper coordinate here will look like: a 2 \n"
            "with nothing else surrounding it, just the letter (first) then the number (second). \n"
            "Have fun!")
        sleep(2)
        cleanup_time()
