import pygame
from functions import cleanup_time
import os
cleanup_time()
pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Pygame Checkers")
frm = pygame.time.Clock()
initialise = True
pressed = False
piece_active: dict = {}
selected_key = None
turn = "red"   # red starts
must_continue = None   # piece that must keep capturing
menu_button = pygame.rect.Rect(0, 0, 36, 10)
menu_font = pygame.font.Font(None, 20)
M = menu_font.render("Menu", True, "black")


def print_board(screen: pygame.display, piece_poses: dict = None, initialise = True) -> dict:
    if piece_poses is None:
        piece_poses: dict = {}
    x: int = 0
    y: int = 0

    while y != 800:
        if (int(str(x)[0]) % 2 == 0):
            if (int(str(y)[0]) % 2 == 0):
                if initialise:
                    if y == 500 or y == 700:
                        if int(str(x)[0]) % 2 == 0:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'red', False]
                    elif y == 600:
                        if int(str(x)[0]) % 2 == 1:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'red', False]
                    elif y == 0 or y == 200:
                        if int(str(x)[0]) % 2 == 1:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'green', False]
                    elif y == 100:
                        if int(str(x)[0]) % 2 == 0:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'green', False]
                pygame.draw.rect(screen, "white", pygame.rect.Rect(x,y,100,100))
            else:
                if initialise:
                    if y == 500 or y == 700:
                        if int(str(x)[0]) % 2 == 0:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'red', False]
                    elif y == 600:
                        if int(str(x)[0]) % 2 == 1:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'red', False]
                    elif y == 0 or y == 200:
                        if int(str(x)[0]) % 2 == 1:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'green', False]
                    elif y == 100:
                        if int(str(x)[0]) % 2 == 0:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'green', False]
                pygame.draw.rect(screen, "black", pygame.rect.Rect(x,y,100,100))
        else:
            if (int(str(y)[0]) % 2 != 0):
                if initialise:
                    if y == 500 or y == 700:
                        if int(str(x)[0]) % 2 == 0:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'red', False]
                    elif y == 600:
                        if int(str(x)[0]) % 2 == 1:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'red', False]
                    elif y == 0 or y == 200:
                        if int(str(x)[0]) % 2 == 1:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'green', False]
                    elif y == 100:
                        if int(str(x)[0]) % 2 == 0:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'green', False]
                pygame.draw.rect(screen, "white", pygame.rect.Rect(x,y,100,100))
            else:
                if initialise:
                    if y == 500 or y == 700:
                        if int(str(x)[0]) % 2 == 0:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'red', False]
                    elif y == 600:
                        if int(str(x)[0]) % 2 == 1:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'red', False]
                    elif y == 0 or y == 200:
                        if int(str(x)[0]) % 2 == 1:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'green', False]
                    elif y == 100:
                        if int(str(x)[0]) % 2 == 0:
                            piece_poses[(x,y)] = [pygame.rect.Rect(x,y,100,100), 'green', False]
                pygame.draw.rect(screen, "black", pygame.rect.Rect(x,y,100,100))

        if x != 700:
            x += 100
        else:
            x = 0
            y += 100

    for k in piece_poses:
        pygame.draw.circle(screen, f"dark{piece_poses[k][1]}", (piece_poses[k][0][0] + 50, piece_poses[k][0][1] + 50), 35)
        pygame.draw.circle(screen, piece_poses[k][1], (piece_poses[k][0][0] + 50, piece_poses[k][0][1] + 50), 30)

    return piece_poses


piece_poses = print_board(screen)


class piece:
    global piece_poses
    def __init__(self, screen: pygame.display, colour: str, position: tuple, is_king: bool = False):
        self.screen = screen
        self.position = position
        self.colour = colour
        self.is_king = is_king

    def legal_moves(self):
        global piece_poses
        x, y = self.position
        moves = []
        jumps = []

        directions = []
        if self.is_king:
            directions = [100, -100]
        else:
            if self.colour == "red":
                directions = [-100]
            else:
                directions = [100]

        # simple moves
        for dy in directions:
            for dx in (-100, 100):
                target = (x + dx, y + dy)
                if 0 <= target[0] <= 700 and 0 <= target[1] <= 700:
                    if target not in piece_poses:
                        moves.append(target)

        # jumps
        for dy in directions:
            for dx in (-100, 100):
                mid = (x + dx, y + dy)
                dest = (x + dx*2, y + dy*2)
                if 0 <= dest[0] <= 700 and 0 <= dest[1] <= 700:
                    if mid in piece_poses and dest not in piece_poses:
                        if piece_poses[mid][1] != self.colour:
                            jumps.append((dest, mid))

        return moves, jumps

    def moveto(self, newpos: tuple):
        global piece_poses
        rect, colour, is_king = piece_poses[self.position]
        rect = pygame.Rect(newpos[0], newpos[1], 100, 100)
        piece_poses[newpos] = [rect, colour, is_king]
        del piece_poses[self.position]
        self.position = newpos

        # kinging
        if not is_king:
            if self.colour == "red" and newpos[1] == 0:
                piece_poses[newpos][2] = True
                self.is_king = True
            elif self.colour == "green" and newpos[1] == 700:
                piece_poses[newpos][2] = True
                self.is_king = True


class board:
    def __init__(self, piece_poses: dict):
        self.piece_posed = piece_poses
checkers = board(piece_poses)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cleanup_time()
            pygame.quit()
            cleanup_time()
            exit(0)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            selected_key = None
            pressed = False
            piece_active.clear()

            for key in piece_poses:

                # forced multi-jump: only allow selecting that piece
                if must_continue is not None and key != must_continue:
                    continue

                if pygame.Rect.collidepoint(piece_poses[key][0], mouse):

                    # normal turn restriction
                    if must_continue is None and piece_poses[key][1] != turn:
                        break

                    pressed = True
                    selected_key = key
                    piece_active[key] = [
                        piece_poses[key][0].copy(),
                        piece_poses[key][1],
                        piece_poses[key][2]
                    ]
                    break
            if pygame.Rect.collidepoint(menu_button, mouse):
                pygame.quit()
                os.system("python .\\multigame.py")
                exit(0) #It wont get this far, but its a safety.

        elif event.type == pygame.MOUSEBUTTONUP:
            if selected_key is not None and selected_key in piece_active:
                mouse = pygame.mouse.get_pos()
                newx = (mouse[0] // 100) * 100
                newy = (mouse[1] // 100) * 100
                newpos = (newx, newy)

                old_rect, colour, is_king = piece_active[selected_key]
                p = piece(screen, colour, selected_key, is_king)
                moves, jumps = p.legal_moves()

                legal = False
                captured_mid = None

                # simple move only allowed if not forced to continue
                if must_continue is None and newpos in moves:
                    legal = True

                # capture moves
                for dest, mid in jumps:
                    if newpos == dest:
                        legal = True
                        captured_mid = mid
                        break

                if legal:
                    # remove captured piece
                    if captured_mid is not None and captured_mid in piece_poses:
                        del piece_poses[captured_mid]

                    # move piece
                    piece_poses[selected_key] = [old_rect, colour, is_king]
                    p.moveto(newpos)

                    # check for additional jumps
                    new_p = piece(screen, colour, newpos, piece_poses[newpos][2])
                    _, new_jumps = new_p.legal_moves()

                    if captured_mid is not None and len(new_jumps) > 0:
                        must_continue = newpos
                    else:
                        must_continue = None
                        turn = "green" if turn == "red" else "red"

                else:
                    piece_poses[selected_key] = piece_active[selected_key]

            pressed = False
            selected_key = None
            piece_active.clear()

        if pressed and selected_key is not None:
            mouse = pygame.mouse.get_pos()
            piece_poses[selected_key][0] = pygame.Rect(mouse[0]-50, mouse[1]-50, 100, 100)

    

    print_board(screen, piece_poses, False)
    screen.blit(M, menu_button)
    pygame.display.flip()
    frm.tick(30)