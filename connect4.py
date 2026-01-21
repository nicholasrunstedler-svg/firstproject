import pygame
from functions import *
import os
from time import sleep
cleanup_time()
pygame.init()


screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Connect 4")
menu_font = pygame.font.Font(None, 20)
win_font = pygame.font.Font(None, 50)
menu_button = pygame.rect.Rect(0, 0, 40, 20)
menu_text = menu_font.render("MENU!!!", True, "black")
reds_turn = True
wants_bot = False
hath_chosen = False
frm = pygame.time.Clock()
redwin = pygame.rect.Rect(0,0, 400, 200)
redwin.center = (400, 400)
redwin_txt = win_font.render("Red Wins!!!", True, 'black')
bot_or_not = win_font.render("To bot or not to bot\n that is the question.", True, 'black')
yes = menu_font.render("I want bot", True, 'black')
no = menu_font.render("I don't want bot", True, 'black')
yes_button = pygame.rect.Rect(0,0, 100, 30)
no_button = pygame.rect.Rect(0,0, 100, 30)
yes_centre = yes.get_rect(center=(400-60, 450))
no_centre = no.get_rect(center=((400+60, 450)))
yes_button.center = (400-60, 450)
no_button.center = (400 + 60, 450)
red_center = redwin_txt.get_rect(center=(400,400))
yellowwin = pygame.rect.Rect(0,0, 400, 200)
yellowwin.center = (400, 400)
yellowwin_txt = win_font.render("Yellow Wins!!!", True, 'black')
yellow_center = yellowwin_txt.get_rect(center=(400,400))
reset_button = pygame.image.load("reset_button.png")
winner = []
reset_button = pygame.transform.scale_by(reset_button, .2)
reset_rect = reset_button.get_rect(topright=(790,10))


def connect4_board() -> superlist:
    board_ = superlist()

    for i in range(1, 7):
        for j in range(1, 8):
            board_.append([i, j, ''])
    return board_
bored = connect4_board()


def generate_diagonal(lst: superlist, pos: list) -> list:
    """Generates the existent downwards diagonals from a position"""
    diagonals: list = []
    idx = lst.index(pos)
    if pos[0] <= 3 and pos[2]:
        if pos[1] == 4:
            for i in range(4):
                if lst[idx+ 8*i][2] == pos[2]:
                    diagonals.append(
                        lst[idx+ 8*i])
                else:  # If any empties on the diagonals, then the process is immediately halted and the empty list is returned
                    return []
            for i in range(4):
                if lst[idx+ 6*i][2] == pos[2]:
                    diagonals.append(
                        lst[idx+ 6*i])
                else:
                    return []
        elif pos[1] < 4:
            for i in range(0,4):
                if lst[idx+ 8*i][2] == pos[2]:
                    diagonals.append(
                        lst[idx+ 8*i])
                else: 
                    return []
        elif pos[1] > 4:
            for i in range(4):
                if lst[idx+ 6*i][2] == pos[2]:
                    diagonals.append(
                        lst[idx+ 6*i])
                else:
                    return []
        return diagonals
    else:
        return []


def dramatic_drop(col: int, screen: pygame.Surface, turn: str = 'red') -> None:
    """Drops the pieces, dramatically."""
    y = 100
    while y < 700:
        
        sleep(.01)


def reset() -> None:
    pygame.quit()
    os.system("python .\\connect4.py")



bored = superlist([
 [1, 1, ''], [1, 2, ''], [1, 3, ''], [1, 4, ''], [1, 5, ''], [1, 6, ''], [1, 7, ''],

 [2, 1, ''], [2, 2, ''], [2, 3, ''], [2, 4, ''], [2, 5, ''], [2, 6, ''], [2, 7, ''],

 [3, 1, ''], [3, 2, ''], [3, 3, ''], [3, 4, ''], [3, 5, ''], [3, 6, ''], [3, 7, ''],

 [4, 1, ''], [4, 2, ''], [4, 3, ''], [4, 4, ''], [4, 5, ''], [4, 6, ''], [4, 7, ''],

 [5, 1, ''], [5, 2, ''], [5, 3, ''], [5, 4, ''], [5, 5, ''], [5, 6, ''], [5, 7, ''],
 
 [6, 1, ''], [6, 2, ''], [6, 3, ''], [6, 4, ''], [6, 5, ''], [6, 6, ''], [6, 7, '']
 ])



class board(superlist):
    """A class to hold all methods specifically intended for the connect 4 game."""
    # Args can be any iterable for versatility.
    def __init__(self, args=tuple()):
        super().__init__(args)


    def __str__(self):
        return f"{self.args}"


    def drop_peice(self, column: int, turn: str = 'red') -> None:
        for pos in self.args:
            if pos[1] == column and all(poses[2] != '' for poses in self.args if poses[1] == column and poses[0] > pos[0]):
                self.replace(pos, [pos[0], pos[1], turn])
                return  # Exit loop


    def check_for_win(self, turn: str = 'red') -> bool:
        for piece in self.args:
            if piece[2] == turn and piece[0] <= 3:
                diagonal = generate_diagonal(self.args, piece)
                if  diagonal:
                    return True
            if piece[2] == turn and piece[1] <= 4:
                if self.what_there([piece[0], piece[1]]) == turn and self.what_there([piece[0]+1, piece[1]]) == turn and self.what_there([piece[0]+2, piece[1]]) == turn and self.what_there([piece[0]+3, piece[1]]) == turn:
                    return True
            if piece[1] <= 4:
                if self.what_there([piece[0], piece[1]]) == turn and self.what_there([piece[0], piece[1]+1]) == turn and self.what_there([piece[0], piece[1]+2]) == turn and self.what_there([piece[0], piece[1]+3]) == turn:
                    return True
        return False
    

    def print(self, screen: pygame.Surface) -> None:
        for piece in self.args:
            if not piece[2]:
                pygame.draw.circle(screen, 'white', (piece[1]*100, piece[0]*100 + 100), 40)
            elif piece[2] == 'red':
                pygame.draw.circle(screen, 'darkred', (piece[1]*100, piece[0]*100 + 100), 40)
                pygame.draw.circle(screen, 'red', (piece[1]*100, piece[0]*100 + 100), 30)
            elif piece[2] == 'yellow':
                pygame.draw.circle(screen, (180, 140, 0), (piece[1]*100, piece[0]*100 + 100), 40)
                pygame.draw.circle(screen, 'yellow', (piece[1]*100, piece[0]*100 + 100), 30)
bored = board(bored)


def bot(lst: board) -> board:
    lst.drop_peice(randint(1,7), 'yellow')
    return lst


while True:
    mouse = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cleanup_time()
            exit(0)

        if wants_bot and not reds_turn and not winner:
            bored = bot(bored)
            if bored.check_for_win('yellow'):
                winner = ['yellow']
            reds_turn = True

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not winner and hath_chosen:
                col = number_theory.round_to_100(mouse[0]) // 100
                try:
                    if reds_turn:
                        bored.drop_peice(col, 'red')
                        reds_turn = False
                        if bored.check_for_win('red'):
                            winner = ['red']
                    else:
                        bored.drop_peice(col, 'yellow')
                        reds_turn = True
                        if bored.check_for_win('yellow'):
                            winner = ['yellow']
                except ValueError: #The player tried to go over the threshold for the peices.
                    pass
                
            
            
            if pygame.Rect.collidepoint(menu_button, mouse):
                pygame.quit()
                os.system("python .\\multigame.py")
            elif pygame.Rect.collidepoint(reset_rect, mouse):
                reset()
            elif pygame.Rect.collidepoint(yes_button, mouse):
                hath_chosen = True
                wants_bot = True
            elif pygame.Rect.collidepoint(no_button, mouse):
                hath_chosen = True
                wants_bot = False

    screen.fill("blue")
    screen.blit(menu_text, menu_button)
    bored.print(screen)
    screen.blit(reset_button, reset_rect)
    if reds_turn:
        pygame.draw.circle(screen, "darkred", (mouse[0], 100), 40)
        pygame.draw.circle(screen, 'red', (mouse[0], 100), 30)
    else:
        pygame.draw.circle(screen, (180, 140, 0), (mouse[0], 100), 40)
        pygame.draw.circle(screen, 'yellow', (mouse[0], 100), 30)
    if winner:
        if winner[0] == 'red':
            pygame.draw.rect(screen, 'red', redwin)
            screen.blit(redwin_txt, red_center)
        elif winner[0] == 'yellow':
            pygame.draw.rect(screen, 'yellow', yellowwin)
            screen.blit(yellowwin_txt, yellow_center)

    if not hath_chosen:
        pygame.draw.rect(screen, 'green', yes_button)
        pygame.draw.rect(screen, 'red', no_button)
        screen.blit(yes, yes_centre)
        screen.blit(no, no_centre)
    
    pygame.display.flip()
    frm.tick(30)
