import pygame
from functions import cleanup_time
import os
pygame.init()
cleanup_time()

playing_chess = False
playing_checkers = False
playing_connect4 = False
game_vals = [playing_chess, playing_checkers, playing_connect4]
screen = pygame.display.set_mode((800,800))
font = pygame.font.Font(None, 48)
frm = pygame.time.Clock()

chess_icon = pygame.image.load("chess_icon.png")
chess_icon = pygame.transform.scale_by(chess_icon, .1)
checkers_icon = pygame.image.load("checkers_icon.png")
checkers_icon = pygame.transform.scale_by(checkers_icon, .15)
connect4_icon = pygame.image.load("connect4_icon.png")
connect4_icon = pygame.transform.scale_by(connect4_icon, .27)



chess_button = checkers_icon.get_rect(center=(800/6,400))
checkers_button = checkers_icon.get_rect(center=(800/2,400))
connect4_button = connect4_icon.get_rect(center=(800*5/6, 400))

class games:
    def __init__(self, name: str):
        self.name = name

    def play(self):
        pygame.quit()
        cleanup_time()
        os.system(f"python .\\{self.name}")

chess = games("pygame_chess.py")
checkers = games("pygame_checkers.py")
connect4 = games("connect4.py")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cleanup_time()
            pygame.quit()
            cleanup_time()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if pygame.Rect.collidepoint(chess_button, mouse):
                chess.play()
                playing_chess = True
            elif pygame.Rect.collidepoint(checkers_button, mouse):
                checkers.play()
                playing_checkers = True
            elif pygame.Rect.collidepoint(connect4_button, mouse):
                connect4.play()
                playing_connect4 = True
            


    if all(not x for x in game_vals):
        screen.blit(chess_icon, chess_button)
        screen.blit(checkers_icon, checkers_button)
        screen.blit(connect4_icon, connect4_button)

    
    pygame.display.flip()
    frm.tick(30)
