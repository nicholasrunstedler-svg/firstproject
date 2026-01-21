import sys
import pygame
from functions import cleanup_time



pygame.init()

WIDTH = 400
HEIGHT = 300
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
input_box = pygame.rect.Rect(50, 200, 200, 50)
ground = pygame.rect.Rect(0, 285, 400, 15)
assert type(ground) == pygame.Rect
polygon = [(0,0), (0, 20), (20, 20),(20,0)]
box_active = False
clock = pygame.time.Clock()
time_start = 10
font = pygame.font.Font(None, 48)
text = ''

def x_mover(points_list: list, x_val: float) -> list:
    """Moves the x's"""
    new_point = []
    for cord in points_list:
        new_point.append((cord[0] + x_val, cord[1]))
    return new_point

def y_mover(points_list: list, y_val: float) -> list:
    """Moves the y's"""
    new_point = []
    for cord in points_list:
        new_point.append((cord[0], y_val + cord[1]))
    return new_point

def gravity(points_list: list, y_val: float,time: float = 0) -> list:
    """Applies gravity to polygons"""
    new_point = []
    for cord in points_list:
        new_point.append((cord[0], y_val - 9.8 * time))
    return new_point

def jump(points_list: list, y_val,time: float = .1) -> list:
    """Jumps the square"""
    new_point = []
    for cord in points_list:
        new_point.append((cord[0], y_val/time))

sprite = pygame.image.load("Chess_spritemap.png")



while True:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            cleanup_time()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:   
            mouse = pygame.mouse.get_pos()
            print(mouse)
            if pygame.Rect.collidepoint(input_box, (mouse)) and not box_active:
                box_active = True
            else:
                box_active = False
        
        if box_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if text == "quit":
                        pygame.quit()
                        cleanup_time()
                        sys.exit()
                        
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

                else:
                    text += event.unicode

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[pygame.K_a]: #Moves the square
        polygon = x_mover(polygon, -2)
    elif keys_pressed[pygame.K_d]:
        polygon = x_mover(polygon, 2)
    if keys_pressed[pygame.K_w]:
        polygon = y_mover(polygon, -2)
    elif keys_pressed[pygame.K_s] and not pygame.Rect.colliderect(pygame.rect.Rect(polygon[0][0], polygon[0][1], abs(polygon[0][0] - polygon[2][0]), abs(polygon[0][1] - polygon[2][1])),  ground):
        polygon = y_mover(polygon, 2)        

    screen.fill("black")
    pygame.draw.polygon(screen, "blue", polygon)

    text_tile = font.render(text, True, "white", None)
    text_rect = text_tile.get_rect(midleft=((55,(200+250)/2)))
    input_box = pygame.rect.Rect(50, 200, max(200,50 + pygame.Surface.get_width(text_tile)), 50)

    if box_active:
        pygame.draw.rect(screen, "white", input_box,2)
    else:
        pygame.draw.rect(screen, "blue", input_box, 2)
    screen.blit(text_tile, text_rect)
    pygame.draw.rect(screen, "green", ground)


    screen.blit(sprite, (0,0))
    
    pygame.display.flip()
    clock.tick(30)