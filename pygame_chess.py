"""This module stimulates chess in pygame, complete with all rules of chess"""
import pygame
import sys
from chess import *
from functions import dictionary_flipper
import webbrowser
import os

pygame.init()
cleanup_time()

if True:
    chess_sprites = pygame.image.load("Chess_Pieces_Sprite.png")
    chessboard_image = pygame.image.load("chessboard.jpg")
    queshun = pygame.image.load("question_mark.png")
    queshun = pygame.transform.scale_by(queshun, .2)
    queshun_rect = queshun.get_rect(center=(0,0))
    chessboard_image = pygame.transform.scale_by(chessboard_image, 2)
    special_image = pygame.transform.scale_by(chessboard_image, .98)
    font = pygame.font.Font(None, 65)
    little_font = pygame.font.Font(None, 40)
    winsurface = pygame.rect.Rect(188, 266.7, 312, 156)
    white_win = False
    black_win = False
    insufficient_material_ = False
    stalemate = False
    three_fold = False
    need_to_check = True
    screen = pygame.display.set_mode((685, 685))
    queshun = queshun.convert_alpha()
    pygame.display.set_caption("Pygame Chess")
    FRAMERATE = pygame.time.Clock()
    time_to_check = pygame.time.get_ticks()
    pressed = False
    should_i_print_him = False
    is_blacks_turn = False
    in_testing = False
    can_move = True
    promotion_sprites_dkt = {}
    promotion_list = []
    promotion_choice = 'kitten'
    game_name = little_font.render("Pygame Chess", True, 'black')
    g_rect= game_name.get_rect(center=(685/2, 15))
    peices = ["k", "q", "b", "n", "r", "p"]
    colours = ["w", "b"]
    prev_board = chessboard
    proper_board = chessboard
    default = ['x', 'y', '']
    peice_rect_key = copy.deepcopy(default)
    legal_moves = copy.deepcopy(default)
    queens_legal_moves = copy.deepcopy(default)
    queens_dkt = {}
    board_states = [chessboard]
    last_peice = copy.deepcopy(default)
    x_index_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    y_index_list = ['1', '2', '3', '4', '5', '6', '7', '8']
    x_index_list = list_flipper(x_index_list)
    blk_start_row = ['r', 'k', 'b', 'q', 'k', 'b', 'k', 'r']
    castling_poses_b = [['c', '8'], ['g', '8']]
    castling_poses_w = [['c', '1'], ['g', '1']]
    wht_start_row = (blk_start_row.copy())
    player_king_moved = False
    bot_king_moved = False
    menu_button = pygame.rect.Rect(10,5,70,30)
    menu_lettres = little_font.render("Menu", True, "black")



    def rectmaker(rect_val: tuple) -> pygame.rect:
        """Makes a sprite with a location"""
        return pygame.rect.Rect(rect_val)
    queshun_r = rectmaker((660, 10, 20, 20))

    def peice_list_maker() -> list:
        """When you give coordinates and rects to the peices \n
        make sure that you add numbers for rank or profile so that all peices \n
        have a different rect associated to them."""
        name_list = []
        for peice_name in peices:
            for colour in colours:
                name_list.append(f"{peice_name}_{colour}")
        return name_list


    def many_rects() -> dict:
        """Many rects."""
        special_list = peice_list_maker()  # Contains peice names
        x = 7
        y = 7
        row = 1
        WIDTH = 55  # It works, so I'm not gonna change it :)
        HEIGHT = 54
        rect_dict = {}

        for peice_name in special_list:  # All the peicenames are in the special_list
            rect_dict.update({
                peice_name: rectmaker(tuple((x, y, WIDTH, HEIGHT)))
            }
            )
            if row == 2:
                x += WIDTH + 12
                y = 7
                row = 1
            else:
                row += 1
                y += 54 + 14
        return rect_dict


    def many_sprite_names() -> list:
        """Makes the sprite names"""
        special_list = peice_list_maker()
        specialer_list = []
        for peice_name in special_list:
            specialer_list.append(f"sprite_{peice_name}")
        return specialer_list


    def many_sprites(dkt: dict) -> dict:
        """Makes the sprites (not really) for the peices \n
           Returns them as a dict."""
        sprite_names = many_sprite_names()
        sprite_dict = {}

        for sprite_name in sprite_names:
            sprite_dict.update({
                sprite_name: chess_sprites.subsurface(dkt[sprite_name[7:]])
            })
        return sprite_dict


    def rect_getter(dictionary: dict, key: str, x: int, y: int) -> list[int, int]:
        """For the placing of peices convieniently.
        x,y will be for center=(x,y) on the rect"""
        return dictionary[key].get_rect(center=(x, y))


    def board_rekt(chessboard_list: list) -> dict:
        """Returns the board rects \n
        KEYS ARE TUPLES SINCE LISTS ARE NOT HASHABLE"""
        rect_dict = {}
        x = 32
        y = 32
        WIDTH = 78
        HEIGHT = 78
        column = 1

        for peice_list in chessboard_list:  # Peices are like ["a", "2", "p"]
            rect_dict.update({
                tuple(peice_list): rectmaker(tuple((x, y, WIDTH, HEIGHT)))
            })
            if column < 8:
                x += 80
                column += 1
            else:
                column = 1
                x = 32
                y += 80
        return rect_dict


    def board_imaged(dkt: dict) -> dict:
        """Outputs the dict of subsurfaces of the tiles. Tuples are the keys"""
        new_dict = {}
        for name in dkt:
            new_dict.update({
                name: chessboard_image.subsurface(dkt[name])
            })
        return new_dict


    def peice_duper(chessboard: list, dkt: dict) -> dict:
        """Returns a dictionary of the peices duped to their proper sprite.\n 
        The keys are tuples as are most of the created dicts. \n
        Dictionary is filled only with the tuples that have peices at them \n
        empty spots should be dealt with in board_printer"""
        dupe_dict = {}
        # dkt is the dict of surfaces taken from the spritesheet for the peices
        # The keys of dkt are unfortunately sprite_k_w and so on, so some checks need to be made
        # Chessboard entries are like ['a', '1', 'r'] and so on.
        for peice in chessboard:
            peice = tuple(peice)  # So that it can be used as a key
            if peice[2].isupper():
                name = f"sprite_{peice[2].lower()}_b"  # If its the black peices
                dupe_dict.update({
                    peice: dkt[name]
                })
            elif peice[2].islower():
                name = f"sprite_{peice[2]}_w"  # If its the white peices
                dupe_dict.update({
                    peice: dkt[name]
                })
            else:
                pass
        return dupe_dict



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


    def  is_castling(chessboard: list, first_pos: list, new_pos: list) -> bool:
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

    if True:  #Many funcs 
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


        def board_printer(chessboard: list, square_tiles: dict, screen: pygame.display, peice_images: dict = {}, flipped=False, peice_active = '', pos = tuple((0,0)), turn: str = 'white') -> dict:  # Pygame adjusted board_printer
            """Prints the board and the peices which are upon the tiles. \n
            Make sure that tile_images are in order when entered in the dict \n
            Also returns the dict of peice rectangles after they have been created for use of collidepoint"""
            # Chess board is just the list of the peices and positions
            # square_tiles is the dictionary of peice pos-es (as tuples).
            global legal_moves
            global player_king_moved
            global bot_king_moved
            global queens_legal_moves
            player_king_before = player_king_moved
            bot_king_before = bot_king_moved
            special_time = False
            new_dict = {}
            x = 32
            y = 32
            col = 1
            if flipped:
                square_tiles = dictionary_flipper(square_tiles)
                peice_images = dictionary_flipper(peice_images) #This will crash everything so dont use it

            for peice_name in chessboard:
                peice_name = tuple(peice_name)
                screen.blit(square_tiles[peice_name], (x, y))
                if peice_name in peice_images:  # The position has a peice here
                    peice_rect = rect_getter(peice_images, peice_name, x + 40, y + 40)
                    new_dict.update({  # This is for the usage of collidepoint down below
                        peice_name: peice_rect
                    })
                    screen.blit(peice_images[peice_name], peice_rect)
                if col == 8:
                    col = 1
                    x = 32
                    y += 78
                else:
                    x += 78
                    col += 1
            if peice_active != '':
                if legal_moves == default and peice_active.lower() != 'q':
                    legal_moves = []
                    if peice_active.lower() == 'p':
                        for position in chess.get_pawn_range(proper_board, list(pos)):
                            special_board = the_game2(list(pos), list(position), proper_board)
                            if proper_board != special_board:
                                if peice_active.islower() and turn == 'white' and not isincheck(special_board, 'white'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                                elif peice_active.isupper() and turn == 'black' and not isincheck(special_board, 'black'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                    elif peice_active.lower() == 'k':
                        for position in chess.get_king_range(proper_board, list(pos)):
                            if not player_king_moved and not special_time and not is_blacks_turn:
                                special_time = True
                            elif not bot_king_moved and not special_time and is_blacks_turn:
                                #print("Black king has not yet moved")
                                special_time = True
                            else:
                                special_time = False
                            if special_time and not is_blacks_turn:
                                player_king_moved = False
                                special_board = move_the_king2(proper_board, pos, position, True, 'white')
                            elif special_time and is_blacks_turn:
                                bot_king_moved = False
                                special_board = move_the_king2(proper_board, pos, position, True, 'black')
                            else:
                                special_board = move_the_king2(proper_board, pos, position, False)
                            if proper_board != special_board and True:
                                if peice_active.islower() and turn == 'white' and not isincheck(special_board, 'white'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                                elif peice_active.isupper() and turn == 'black' and not isincheck(special_board, 'black'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                        #Castling cases

                        for position2 in castling_poses_w + castling_poses_b:
                            if is_blacks_turn and peice_active.isupper():
                                bot_king_moved = bot_king_before
                            elif not is_blacks_turn and peice_active.islower():
                                player_king_before = player_king_before
                            #Manual check becuase the regular one is mysteriously broken.
                            if not isincheck(proper_board, turn): #Cannot castle through check
                                row = chess.get_horiz_lst(proper_board, 8, 9 - int(pos[1]))
                                start = lettre_indexer(pos[0])
                                end = lettre_indexer(position2[0])
                                if start < end and all(x[2] == '' for x in row[start + 1:end + 1]) and not is_blacks_turn and position2[1] == '1' and not player_king_before:
                                    special_board2 = move_the_king(proper_board, pos, position2) #Dangerous function
                                elif end < start and all(x[2] == '' for x in row[end:start]) and not is_blacks_turn and position2[1] == '1' and not player_king_before:
                                    special_board2 = move_the_king(proper_board, pos, position2) #Dangerous function
                                elif start < end and all(x[2] == '' for x in row[start + 1:end + 1]) and is_blacks_turn and position2[1] == '8' and not bot_king_before:
                                    special_board2 = move_the_king(proper_board, pos, position2) #Dangerous function
                                elif end < start and all(x[2] == '' for x in row[end:start]) and is_blacks_turn and position2[1] == '8' and not bot_king_before:
                                    special_board2 = move_the_king(proper_board, pos, position2) #Dangerous function
                                else:
                                    special_board2 = proper_board
                            else:
                                special_board2 = proper_board

                            if proper_board != special_board2:
                                if peice_active.islower() and turn == 'white' and not isincheck(special_board2, 'white'):
                                    legal_moves.append(position2)
                                    pygame.draw.circle(screen, 'white', (lettre_indexer(position2[0])*77 + 75,685 -  int(position2[1])*76 ), 10, 5, True, True, True, True)
                                elif peice_active.isupper() and turn == 'black' and not isincheck(special_board2, 'black') and pos[1] == '8':
                                    legal_moves.append(position2)
                                    pygame.draw.circle(screen, 'black', (lettre_indexer(position2[0])*77 + 75,685 -  int(position2[1])*76 ), 10, 5, True, True, True, True)

                    elif peice_active.lower() == 'n':
                        for position in chess.get_knight_range(proper_board, list(pos)):
                            special_board = the_game2(list(pos), list(position), proper_board)
                            if proper_board != special_board:
                                if peice_active.islower() and turn == 'white' and not isincheck(special_board, 'white'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                                elif peice_active.isupper() and turn == 'black' and not isincheck(special_board, 'black'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                    elif peice_active.lower() == 'r':
                        for position in chess.get_horizzy_range(proper_board, list(pos)):
                            special_board = the_game2(list(pos), list(position), proper_board)
                            if proper_board != special_board:
                                if peice_active.islower() and turn == 'white' and not isincheck(special_board, 'white'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                                elif peice_active.isupper() and turn == 'black' and not isincheck(special_board, 'black'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)

                    elif peice_active.lower() == 'b':
                        for position in chess.get_diag_range(proper_board, list(pos)):
                            special_board = the_game2(list(pos), list(position), proper_board)
                            if proper_board != special_board:
                                if peice_active.islower() and turn == 'white' and not isincheck(special_board, 'white'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                                elif peice_active.isupper() and turn == 'black' and not isincheck(special_board, 'black'):
                                    legal_moves.append(position)
                                    pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)


                elif peice_active.lower() == 'q' and tuple((pos[0], pos[1], peice_active)) not in queens_dkt:
                    special_list = []
                    for position in chess.get_horizzy_range(proper_board, list(pos)):
                        special_board = the_game2(list(pos), list(position), proper_board)
                        if proper_board != special_board:
                            if peice_active.islower() and turn == 'white' and not isincheck(special_board, 'white'):
                                special_list.append(position)
                                queens_dkt.update({
                                    tuple((pos[0], pos[1], peice_active)) : special_list
                                })
                                pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                            elif peice_active.isupper() and turn == 'black' and not isincheck(special_board, 'black'):
                                special_list.append(position)
                                queens_dkt.update({
                                    tuple((pos[0], pos[1], peice_active)) : special_list
                                })                        
                                pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                    for position in chess.get_diag_range(proper_board, list(pos)):
                        special_board = the_game2(list(pos), list(position), proper_board)
                        if proper_board != special_board:
                            if peice_active.islower() and turn == 'white' and not isincheck(special_board, 'white'):
                                special_list.append(position)
                                queens_dkt.update({
                                    tuple((pos[0], pos[1], peice_active)) : special_list
                                })        
                                pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                            elif peice_active.isupper() and turn == 'black' and not isincheck(special_board, 'black'):
                                special_list.append(position)
                                queens_dkt.update({
                                    tuple((pos[0], pos[1], peice_active)) : special_list
                                })    
                                pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)


                elif legal_moves != default and not is_blacks_turn:
                    for position in legal_moves:
                        pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                elif legal_moves != default and is_blacks_turn:
                    for position in legal_moves:
                        pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)

                if peice_active == 'q' and tuple((pos[0], pos[1], peice_active)) in queens_dkt and not is_blacks_turn:
                    val = queens_dkt[tuple((pos[0], pos[1], peice_active))]
                    for position in val:
                        pygame.draw.circle(screen, 'white', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)
                elif peice_active == 'Q' and tuple((pos[0], pos[1], peice_active)) in queens_dkt and is_blacks_turn:
                    val = queens_dkt[tuple((pos[0], pos[1], peice_active))]
                    for position in val:
                        pygame.draw.circle(screen, 'black', (lettre_indexer(position[0])*77 + 75,685 -  int(position[1])*76 ), 10, 5, True, True, True, True)





            player_king_moved = player_king_before
            bot_king_moved = bot_king_before
            if flipped: #Will ruin everything so dont use it.
                return dictionary_flipper(new_dict)
            return new_dict


        def promotion_checker(chessboard: list) -> bool:
            """Checks if any promotions must be made before moving on"""
            if any((peice[2] == 'p' and peice[1] == '8') or (peice[2] == 'P' and peice[1] == '1') for peice in chessboard):
                return True
            return False


        def promotion_choice_printer(pawn_pos: list, display: pygame.display, peicedkt: dict, turn: str = 'white') -> list:
            """Pass. Just make pawn_pos what its position is in the chessboard. \n
            The math to find the coordinates will be done in this function. \n
            Returns a dictionary with the peice rects for use of collidepoint."""
            dkt = {}
            choices = ['b', 'n', 'q', 'r']
            x = (lettre_indexer(pawn_pos[0])*74 + 64)
            y = 32
            coverer = pygame.rect.Rect(x, y, 60, 270)
            if turn == 'white':
                pygame.draw.rect(display, 'white', coverer, 60)
            elif turn == 'black':
                pygame.draw.rect(display, 'white', rectmaker(
                    tuple((x, 410 - y, 60, 270))), 60)
            for possibility in choices:
                if turn == 'white':
                    display.blit(peicedkt[f"sprite_{possibility}_w"], (x, y))
                    y += 64
                    dkt.update({
                        f"sprite_{possibility}_w": rectmaker(tuple((x, y - 64, 64, 64)))
                    })
                elif turn == 'black':
                    display.blit(
                        peicedkt[f"sprite_{possibility}_b"], (x, 685 - y - 64))
                    y += 64
                    dkt.update({
                        f"sprite_{possibility}_b": rectmaker(tuple((x, 685 - y, 64, 64)))
                    })

            return dkt


        def promotion_doer(chessboard: list, choice: str, turn: str = 'white'):
            """Does the promotion"""
            check = copy.deepcopy(chessboard)
            choices = ['b', 'n', 'q', 'r']
            if choice not in choices:
                return chessboard
            for peice in chessboard:
                if peice[1] == '8' and peice[2] == 'p' and turn == 'white':
                    chessboard = item_replacer(chessboard, [peice[0], peice[1], choice], chess.find_index_abiguous_in_list(
                        chessboard, [peice[0], peice[1]]) + 1)
                elif peice[1] == '1' and peice[2] == 'P' and turn == 'black':
                    chessboard = item_replacer(chessboard, [peice[0], peice[1], choice.upper(
                    )], chess.find_index_abiguous_in_list(chessboard, [peice[0], peice[1]]) + 1)
            if check != chessboard:
                global can_move
                global board_states
                board_states.append(chessboard)
                can_move = True
            return chessboard


    # The rectangles of the peices. Not really needed after the below.
    peice_rects = many_rects()
    # The sprites/subsurfaces of the peices.
    sprite_dict = many_sprites(peice_rects)
    # The rectangles of the board. Becomes extrodinarily important below
    square_rects = board_rekt(chessboard)
    # The subsurfaces for displaying to the screen
    square_tiles = board_imaged(square_rects)
    # New surface made for each individual peice so that they can be treated separately
    board_look = peice_duper(chessboard, sprite_dict)





    # -----------------------------
    #         GAME START
    # -----------------------------


    while True:
        if len(board_states) >= 2:
            prev_board = board_states[-1]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Normal practice for pygame in terminal
                pygame.quit()
                cleanup_time()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # If the player clicks the mouse
                mouse_pos = pygame.mouse.get_pos()  # Mouse coords

                if pygame.Rect.collidepoint(queshun_r, mouse_pos):
                    webbrowser.open("https://en.wikipedia.org/wiki/Chess")

                if can_move:
                    for peice_rect_key in current_peice_rects:
                        peice_rect = current_peice_rects[peice_rect_key]
                        if pygame.Rect.collidepoint(peice_rect, mouse_pos):
                            peice_touched = peice_rect_key
                            # Then we enlevons the peice from the chessboard so that it becomes a free agent.
                            proper_board = copy.deepcopy(chessboard)
                            chessboard = item_replacer(chessboard, [peice_touched[0], peice_touched[1], ''], chess.find_index_abiguous_in_list(
                                chessboard, [peice_touched[0], peice_touched[1]]) + 1)
                            # Now peice_touched must be prepared for movement!
                            peice_new_rect = board_look[peice_rect_key].get_rect(
                                center=(mouse_pos))
                            peice_being_moved = board_look[peice_rect_key]
                            last_peice = copy.deepcopy(peice_rect_key)
                            pressed = True
                            should_i_print_him = True
                            break

                for peice_rect_key2 in promotion_sprites_dkt:
                    if pygame.Rect.collidepoint(promotion_sprites_dkt[peice_rect_key2], mouse_pos):
                        promotion_choice = peice_rect_key2[-3]
                        break
                    else:
                        promotion_choice = ''
                
                if pygame.Rect.collidepoint(menu_button, mouse_pos):
                    pygame.quit()
                    cleanup_time()
                    
                    os.system("python .\\multigame.py")

            elif event.type == pygame.MOUSEBUTTONUP and pressed:
                cleanup_time()
                should_i_print_him = False
                mouse_pos = pygame.mouse.get_pos()
                pressed = False


                for square_rect in square_rects:
                    if pygame.Rect.collidepoint(square_rects[square_rect], mouse_pos):
                        break

                if not is_blacks_turn and peice_rect_key[2].islower():
                    check_board2 = copy.deepcopy(proper_board)
                    chessboard = the_game_veritablement([peice_rect_key[0], peice_rect_key[1]], [
                                                        square_rect[0], square_rect[1]], proper_board)
                    if check_board2 != chessboard:
                        for entry1 in check_board2:
                            for entry2 in chessboard:
                                if entry1 != entry2 and check_board2.index(entry1) == chessboard.index(entry2):
                                    special_entry = entry2
                                    promotion_list.append(special_entry)
                        is_blacks_turn = True
                        not_flipped = chessboard
                        queens_dkt = {}
                        #chessboard = list_flipper(chessboard)
                elif is_blacks_turn and peice_rect_key[2].isupper():
                    #print(bot_king_moved)
                    check_board2 = copy.deepcopy(proper_board)
                    chessboard = the_game_veritablement([peice_rect_key[0], peice_rect_key[1]], [
                                                        square_rect[0], square_rect[1]], proper_board, 'black')
                    if (check_board2 != chessboard):
                        for entry1 in check_board2:
                            for entry2 in chessboard:
                                if entry1 != entry2 and check_board2.index(entry1) == chessboard.index(entry2):
                                    special_entry = entry2
                                    promotion_list.append(special_entry)
                        is_blacks_turn = False
                        not_flipped = chessboard
                        queens_dkt = {}
                        #chessboard = list_flipper(chessboard)
                # The player was naughty
                elif not (is_blacks_turn or peice_rect_key[2].islower()) and not in_testing:
                    chessboard = proper_board
                # The other player was naughty
                elif not ((not is_blacks_turn) or peice_rect_key[2].isupper()) and not in_testing:
                    chessboard = proper_board

                peice_rect_key = copy.deepcopy(default)
                legal_moves = copy.deepcopy(default)

            if pressed:
                mouse_pos = pygame.mouse.get_pos()
                try:
                    peice_new_rect = peice_being_moved.get_rect(center=(mouse_pos))
                except Exception as e:
                    pass

        screen.blit(special_image, (0, 0))

        # --------------------------------------------------------------------------------------------
        # This is where all changes to the chessboard are cascaded down the important dictionaries
        square_rects = board_rekt(chessboard)
        square_tiles = board_imaged(square_rects)
        board_look = peice_duper(chessboard, sprite_dict)
        if not is_blacks_turn:
            current_peice_rects = board_printer(
                chessboard, square_tiles, screen, board_look, False, peice_rect_key[2], peice_rect_key[:2]) 
        else:
            current_peice_rects = board_printer(
                chessboard, square_tiles, screen, board_look, False, peice_rect_key[2], peice_rect_key[:2], 'black') 
        # This ^^^^^^^^ must happen after all necessary changes to dictionaries have been made
        # ---------------------------------------------------------------------------------------------
        if promotion_checker(chessboard):
            can_move = False
            if is_blacks_turn:
                promotion_sprites_dkt = promotion_choice_printer(
                    promotion_list[-2], screen, sprite_dict, 'white')
                chessboard = promotion_doer(chessboard, promotion_choice, 'white')
            else:
                promotion_sprites_dkt = promotion_choice_printer(
                    promotion_list[-2], screen, sprite_dict, 'black')
                chessboard = promotion_doer(chessboard, promotion_choice, 'black')

        #Mates
        if prev_board != board_states[-1] and can_move and need_to_check and mated3(board_states[-1], 'black'):
            need_to_check = False
            white_win = True
            can_move = False
        elif prev_board != board_states[-1] and can_move and need_to_check and mated3(board_states[-1]):
            need_to_check = False
            can_move = False
            black_win = True
        #Stalemate
        elif prev_board != board_states[-1] and is_blacks_turn and can_move and need_to_check and stalemated(board_states[-1], 'black'):
            need_to_check = False
            can_move = False
            stalemate = True
        elif prev_board != board_states[-1] and not is_blacks_turn and can_move and need_to_check and stalemated(board_states[-1]):
            need_to_check = False
            can_move = False
            stalemate = True
        #Insufficient material
        if prev_board != board_states[-1] and need_to_check and insufficient_material(board_states[-1]):
            need_to_check = False
            can_move = False
            insufficient_material_ = True
        #Three fold rule
        if prev_board != board_states[-1] and need_to_check and three_fold_rule(board_states):
            need_to_check = False
            can_move = False
            three_fold = True


        if white_win:
            pygame.draw.rect(screen, "black", winsurface)
            win_tile = font.render("White Wins!!!", True, 'white')
            screen.blit(win_tile, (200, 320))
        elif black_win:
            pygame.draw.rect(screen, "white", winsurface)
            win_tile = font.render("Black Wins!!!", True, 'black')
            screen.blit(win_tile, (200, 320))
        elif insufficient_material_:
            pygame.draw.rect(screen, "black", winsurface)
            stale_tile = little_font.render("Draw by", True, 'white')
            stale_rect1= stale_tile.get_rect(center = (685/2, 320))
            stale_tile2 = little_font.render("insufficient material.", True, 'white')
            stale_rect2 = stale_tile2.get_rect(center=(685/2, 360))
            screen.blit(stale_tile, stale_rect1)
            screen.blit(stale_tile2, stale_rect2)
        elif stalemate:
            pygame.draw.rect(screen, "black", winsurface)
            stale_tile = little_font.render("Stalemate", True, 'white')
            stale_rect1= stale_tile.get_rect(center = (685/2, 340))
            screen.blit(stale_tile, stale_rect1)
        elif three_fold:
            pygame.draw.rect(screen, "black", winsurface)
            stale_tile = little_font.render("Draw by", True, 'white')
            stale_rect1= stale_tile.get_rect(center = (685/2, 320))
            stale_tile2 = little_font.render("Repetition.", True, 'white')
            stale_rect2 = stale_tile2.get_rect(center=(685/2, 360))
            screen.blit(stale_tile, stale_rect1)
            screen.blit(stale_tile2, stale_rect2)

        screen.blit(queshun, queshun_r)
        screen.blit(game_name, g_rect)
        screen.blit(menu_lettres, menu_button)

        try:
            if should_i_print_him:
                screen.blit(peice_being_moved, peice_new_rect)
        except Exception as e:
            pass


        pygame.display.flip()
        time_to_check = pygame.time.get_ticks()
        FRAMERATE.tick(25)
