"""This module is torture."""
from functions import *
import pygame
cleanup_time()
pygame.init()

screen = pygame.display.set_mode((1000,1000))
board = pygame.image.load("Monopoly.png")
print(board.get_size())
die = pygame.image.load("Die_sptrites.png")
board = pygame.transform.scale_by(board, .7)
font = pygame.font.Font(None, 20)
frm = pygame.time.Clock()
turns = {}
colours = {}
peices = {}



def scissors(surf: pygame.surface, rectval: pygame.Rect) -> pygame.surface:
    """Scissors"""
    return pygame.Surface.subsurface(surf, rectval).copy()

tile_dkt = {}
tile_dkt["Go"] = [scissors(screen, pygame.Rect(868, 868, 131, 131)).copy(), -200, "corner"]

tile_dkt["silver_mine"] = [scissors(screen, pygame.Rect(868 -80, 868, 80, 131)).copy(), 60, "brown"]
tile_dkt["community_chest"] = [scissors(screen, pygame.Rect(868 - 160, 868, 80, 131)).copy(), 0, "community_chest"]
tile_dkt["gold_mine"] = [scissors(screen, pygame.Rect(868 -240, 868, 80, 131)).copy(), 60, "brown"]
tile_dkt["drainage"] = [scissors(screen, pygame.Rect(868 -80*4, 868, 80, 131)).copy(), "player_choice", "utility"]
tile_dkt["sante_fe_railroad"] = [scissors(screen, pygame.Rect(868 -80*5, 868, 80, 131)).copy(), 200, "railroad"]
tile_dkt["the_h.w._well"] = [scissors(screen, pygame.Rect(868 -80*6, 868, 80, 131)).copy(), 100, "light_blue"]
tile_dkt["chance1"] = [scissors(screen, pygame.Rect(868 -80*7, 868, 80, 131)).copy(), 0, "chance"]
tile_dkt["antelope_well"] = [scissors(screen, pygame.Rect(868 -80*8, 868, 80, 131)).copy(), 100, "light_blue"]
tile_dkt["coyote_hills"] = [scissors(screen, pygame.Rect(868 -80*9, 868, 80, 131)).copy(), 120, "light_blue"]

tile_dkt["church"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868, 131, 131)).copy(), 0, "tax"]

tile_dkt["signal_hills_discovery_well"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80, 131, 80)).copy(), 140, "pink"]
tile_dkt["telegraph"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*2, 131, 80)).copy(), 150, "pink"]
tile_dkt["signal_hills_spillage"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*3, 131, 80)).copy(), 140, "pink"]
tile_dkt["signal_hills_bankside"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*4, 131, 80)).copy(), 160, "orange"]
tile_dkt["southern_pacific"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*5, 131, 80)).copy(), 200, "railroad"]
tile_dkt["the_sunday_ranch"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*6, 131, 80)).copy(), 180, "orange"]
tile_dkt["community_chest2"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*7, 131, 80)).copy(), 0, "community_chest"]
tile_dkt["ac_maude"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*8, 131, 80)).copy(), 180, "orange"]
tile_dkt["blodget"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*9, 131, 80)).copy(), 200, "orange"]

tile_dkt["free_quail_hinting"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 -80*10 - 50, 131, 131)).copy(), 0, "corner"]

tile_dkt["redlic"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*1, 868 - 80*10.72, 80, 131)).copy(), 220, "red"]
tile_dkt["chance3"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*2, 868 - 80*10.72, 80, 131)).copy(), 0, "chance"]
tile_dkt["carr"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*3, 868 - 80*10.72, 80, 131)).copy(), 220, "red"]
tile_dkt["belvins"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*4, 868 - 80*10.72, 80, 131)).copy(), 240, "red"]
tile_dkt["bnsf_railway"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*5, 868 - 80*10.72, 80, 131)).copy(), 200, "railroad"]
tile_dkt["little_boston_derrick_1_marry"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*6, 868 - 80*10.72, 80, 131)).copy(), 260, "yellow"]
tile_dkt["little_boston_derrick_2"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*7, 868 - 80*10.72, 80, 131)).copy(), 0, "yellow"]
tile_dkt["pipe_line"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*8, 868 - 80*10.72, 80, 131)).copy(), 150, "utility"]
tile_dkt["little_boston_derrick_3"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*9, 868 - 80*10.72, 80, 131)).copy(), 280, "yellow"]

tile_dkt["goto_church"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 - 50, 131, 131)).copy(), -200, "corner"]

tile_dkt["bandy_tract_william_sr"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*1, 131, 80)).copy(), 300, "green"]
tile_dkt["bandy_tract_grandson"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*2, 131, 80)).copy(), 300, "green"]
tile_dkt["community_chest3"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*3, 131, 80)).copy(), 0, "community_chest"]
tile_dkt["vandy_tract_drainage"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*4, 131, 80)).copy(), 320, "green"]
tile_dkt["union_pacific_railroad"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*5, 131, 80)).copy(), 200, "railroad"]
tile_dkt["chance4"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*6, 131, 80)).copy(), 0, "chance"]
tile_dkt["church_of_the_third_revelation"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*7, 131, 80)).copy(), 350, "dark_blue"]
tile_dkt["derrick_fire"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*8, 131, 80)).copy(), 75, "tax"]
tile_dkt["plainview_estate"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*9, 131, 80)).copy(), 400, "dark_blue"]
#----------------------------------------------------------------------------------------------------------------------
rotated = {}

rotated["Go"] = [scissors(screen, pygame.Rect(868, 868, 131, 131)).copy(), -200, "corner"]

rotated["silver_mine"] = [scissors(screen, pygame.Rect(868 -80, 868, 80, 131)).copy(), 60, "brown"]
rotated["community_chest"] = [scissors(screen, pygame.Rect(868 - 160, 868, 80, 131)).copy(), 0, "community_chest"]
rotated["gold_mine"] = [scissors(screen, pygame.Rect(868 -240, 868, 80, 131)).copy(), 60, "brown"]
rotated["drainage"] = [scissors(screen, pygame.Rect(868 -80*4, 868, 80, 131)).copy(), "player_choice", "utility"]
rotated["sante_fe_railroad"] = [scissors(screen, pygame.Rect(868 -80*5, 868, 80, 131)).copy(), 200, "railroad"]
rotated["the_h.w._well"] = [scissors(screen, pygame.Rect(868 -80*6, 868, 80, 131)).copy(), 100, "light_blue"]
rotated["chance1"] = [scissors(screen, pygame.Rect(868 -80*7, 868, 80, 131)).copy(), 0, "chance"]
rotated["antelope_well"] = [scissors(screen, pygame.Rect(868 -80*8, 868, 80, 131)).copy(), 100, "light_blue"]
rotated["coyote_hills"] = [scissors(screen, pygame.Rect(868 -80*9, 868, 80, 131)).copy(), 120, "light_blue"]

rotated["church"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868, 131, 131)).copy(), 0, "tax"]

rotated["signal_hills_discovery_well"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80, 131, 80)).copy(), 140, "pink"]
rotated["telegraph"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*2, 131, 80)).copy(), 150, "pink"]
rotated["signal_hills_spillage"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*3, 131, 80)).copy(), 140, "pink"]
rotated["signal_hills_bankside"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*4, 131, 80)).copy(), 160, "orange"]
rotated["southern_pacific"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*5, 131, 80)).copy(), 200, "railroad"]
rotated["the_sunday_ranch"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*6, 131, 80)).copy(), 180, "orange"]
rotated["community_chest2"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*7, 131, 80)).copy(), 0, "community_chest"]
rotated["ac_maude"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*8, 131, 80)).copy(), 180, "orange"]
rotated["blodget"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 - 80*9, 131, 80)).copy(), 200, "orange"]

rotated["free_quail_hinting"] = [scissors(screen, pygame.Rect(868 - 80*10 -50, 868 -80*10 - 50, 131, 131)).copy(), 0, "corner"]

rotated["redlic"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*1, 868 - 80*10.72, 80, 131)).copy(), 220, "red"]
rotated["chance3"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*2, 868 - 80*10.72, 80, 131)).copy(), 0, "chance"]
rotated["carr"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*3, 868 - 80*10.72, 80, 131)).copy(), 220, "red"]
rotated["belvins"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*4, 868 - 80*10.72, 80, 131)).copy(), 240, "red"]
rotated["bnsf_railway"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*5, 868 - 80*10.72, 80, 131)).copy(), 200, "railroad"]
rotated["little_boston_derrick_1_marry"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*6, 868 - 80*10.72, 80, 131)).copy(), 260, "yellow"]
rotated["little_boston_derrick_2"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*7, 868 - 80*10.72, 80, 131)).copy(), 0, "yellow"]
rotated["pipe_line"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*8, 868 - 80*10.72, 80, 131)).copy(), 150, "utility"]
rotated["little_boston_derrick_3"] = [scissors(screen, pygame.Rect(868 - 80*10 + 80*9, 868 - 80*10.72, 80, 131)).copy(), 280, "yellow"]

rotated["goto_church"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 - 50, 131, 131)).copy(), -200, "corner"]

rotated["bandy_tract_william_sr"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*1, 131, 80)).copy(), 300, "green"]
rotated["bandy_tract_grandson"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*2, 131, 80)).copy(), 300, "green"]
rotated["community_chest3"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*3, 131, 80)).copy(), 0, "community_chest"]
rotated["vandy_tract_drainage"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*4, 131, 80)).copy(), 320, "green"]
rotated["union_pacific_railroad"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*5, 131, 80)).copy(), 200, "railroad"]
rotated["chance4"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*6, 131, 80)).copy(), 0, "chance"]
rotated["church_of_the_third_revelation"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*7, 131, 80)).copy(), 350, "dark_blue"]
rotated["derrick_fire"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*8, 131, 80)).copy(), 75, "tax"]
rotated["plainview_estate"] = [scissors(screen, pygame.Rect(868, 868 - 80*10 + 80*9, 131, 80)).copy(), 400, "dark_blue"]

rotation_map = {
    "Go": 0,
    "silver_mine": 0,
    "community_chest": 0,
    "gold_mine": 0,
    "drainage": 0,
    "sante_fe_railroad": 0,
    "the_h.w._well": 0,
    "chance1": 0,
    "antelope_well": 0,
    "coyote_hills": 0,

    "church": 90,
    "signal_hills_discovery_well": 90,
    "telegraph": 90,
    "signal_hills_spillage": 90,
    "signal_hills_bankside": 90,
    "southern_pacific": 90,
    "the_sunday_ranch": 90,
    "community_chest2": 90,
    "ac_maude": 90,
    "blodget": 90,

    "free_quail_hinting": 180,
    "redlic": 180,
    "chance3": 180,
    "carr": 180,
    "belvins": 180,
    "bnsf_railway": 180,
    "little_boston_derrick_1_marry": 180,
    "little_boston_derrick_2": 180,
    "pipe_line": 180,
    "little_boston_derrick_3": 180,

    "goto_church": 270,
    "bandy_tract_william_sr": 270,
    "bandy_tract_grandson": 270,
    "community_chest3": 270,
    "vandy_tract_drainage": 270,
    "union_pacific_railroad": 270,
    "chance4": 270,
    "church_of_the_third_revelation": 270,
    "derrick_fire": 270,
    "plainview_estate": 270,
}


# 78 from left
# 129 from top
# 41 in between
# 37 up and down
# 260 X 250 for the dies
def get_die_faces(diesheet: pygame.surface) -> dict:
    die_dict = {}
    startx = 78
    starty = 129
    face = 1
    while face <= 6:
        die_dict.update({
            face : pygame.transform.scale_by(scissors(diesheet, pygame.Rect(startx, starty, 260, 250)), .5)
        })
        if startx >= 305*2:
            startx = 78
            starty += 41 + 250
        else:
            startx += 305
        face += 1
    return die_dict


class peice:
    global colours
    global turns
    def __init__(self, name: str, argents: int = 1500):
        self.name = name #Player's name
        colour_for_player = randomhex()

        colours.update({
            name : ["go", colour_for_player] #Default pos in first arg
        })
        turns.update({
            name : (True if len(turns) == 0 else False)
        })

die_dict = get_die_faces(die)
me = peice("nicho")
#her = peice("Elanor")
start = 0
die1 = 0  
die2 = 0     

#Cornerbox dimensions are 183 X 187
# Widths are 112 for spaces/ positions on the board

def board_cutter(screen: pygame.display, colours: dict = {}) -> dict: #We need colours for the poses
    """And printer"""


    x = 868
    y = 868
    #first row
    
    for key in list(tile_dkt)[:10]:
        screen.blit(tile_dkt[key][0],(x, 868))
        player_count = 0
        for name in colours:
            if colours[name][0] == key: #If player is on this spot
                player_count += 1
                

        x -= 80
        pass
        

# rotation amounts for each tile

    # apply rotation to each tile image
    for name, data in rotated.items():
        surf = data[0]
        angle = rotation_map[name]
        rotated[name][0] = pygame.transform.rotate(surf, angle)

    return tile_dkt, rotated


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            print(mouse)
            for name in peices:
                if turns[name]: #Boolean value
                    if pygame.Rect.collidepoint(peices[name], mouse):
                        die1 = randint(1,6)
                        die2 = randint(1,6)
                        turns[name] = False
                        names = list(turns.keys())
                        nameidx = names.index(name)
                        if nameidx < len(names) - 1:
                            turns[names[nameidx + 1]] = True
                        else:
                            turns[names[0]] = True
    
    screen.blit(board, (-10,-10))


    if die1 in die_dict:
        pos = die_dict[die1].get_rect(center=(1000/2 - 100,1000/2))
        screen.blit(die_dict[die1], pos)
        pos = die_dict[die2].get_rect(center=(1000/2 + 100,1000/2))
        screen.blit(die_dict[die2], pos)
    cutted = board_cutter(board, colours)[0]
    for key in cutted:
        screen.blit(cutted[key][0], (0,20))
    start = 0
    pygame.display.flip()
    frm.tick(10)
