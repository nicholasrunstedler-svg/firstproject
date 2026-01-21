from theorem_testing_functions import *
import traceback
from functions import cleanup_time
import pygame
pygame.init()
cleanup_time()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Nigga")
FRM = pygame.time.Clock()
Origin = pygame.Rect(0, 0, 20, 20)
Origin.center = (800/2 , 800/2)

e1 = Vector3(1,0,0)
e2 = Vector3(0,1,0)
e3 = Vector3(0,0,1)


class pygameVector(Vector3):
    def __init__(self, *args):
        super().__init__(*args)
        self.pyx = 800/2 + (self.x) * 100 #Arbitrary scalar
        self.pyy = 800/2 - (self.y) * 100
        self.pyz = 800/2 - (self.z) * 100

    def cast_to_xy(self):
        pass


M = pygameVector(1, 0, 1.0)
O = pygameVector(0, 0, 0)

def polygon(screen: pygame.display,vec1: pygameVector, vec2: Vector3) -> None:
    """pass"""
    vec = []
    t = 0
    while t < 1:
        pygame.draw.rect(screen, "black", (t*vec1.pyx + (1-t)*vec2.pyx, t*vec1.pyz + (1-t)*vec2.pyz, 2, 2))
        vec.append(pygame.Rect(t*vec1.pyx + (1-t)*vec2.pyx, t*vec1.pyz + (1-t)*vec2.pyz, 150, 150))
        t += .01
    return vec

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if any(pygame.Rect.collidepoint(rec, mouse) for rec in vec):
                new = (M.Rot(math.pi/4, 'z'))
                M = pygameVector(new[0], new[1], new[2])


    
    screen.fill("gray")
    pygame.draw.rect(screen, "white", Origin)
    vec = polygon(screen, M, O)
    pygame.draw.aaline(screen, "black", (800/2,800), (800/2, 0), 2)
    pygame.draw.aaline(screen, "black", (800,800/2), (0, 800/2), 2)
    pygame.draw.aaline(screen, "black", (200, 600), (600, 200), 2)
    pygame.display.flip()
    FRM.tick(10)