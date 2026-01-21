"""This module is a stimulation of blackjack"""
import pygame
from time import sleep
import sys
from random import randint
pygame.init()
deck = dict()


def black_jack_round(deck: dict,screen: pygame.display, back_ground: pygame.Surface, user = '', dealer_cards = [], player_cards = [], cards = 0, bet = 0, first_loop = True, player_monies = 0, stay = False) -> int:
    """Stimulates one round of blackjack. The return value is the amount of player monies after the round has been played out."""
    global round_in_progress
    round_in_progress = True
    hashable_dict = list(deck)
    dealer_cards = []
    player_cards = []
    cards = 0
    cards_to_play_out = []
    screen.blit((back_ground), (0,0))
    pygame.display.update()
    centre = 450
    dealer_start_print = centre - (len(dealer_cards) * 54)
    player_start_print = centre - (len(player_cards) * 54)

    if len(user) >= 3:
        while cards < 4: #this while loop gets the list of starting cards to play out ready. 
            #No user input will be taken until these cards appear on the screen.
            try:
                card_num = randint(0,51)
                card_to_try = hashable_dict[card_num]
                if deck[card_to_try] != 0:
                    cards_to_play_out.append(card_to_try)
                    deck[card_to_try] - 1
                    cards += 1

            except KeyError:
                pass
            



        if score_eval_BJ(player_cards) != "Thats a buss":
            if user.lower().strip() != "stay":
                #If the user is feeling lucky. Or if they screwed up their input.
                #This while loop will make the variable names for the images which will be assigned to the dealers and users cards
                counter = 0
                counter4 = 0
                dealer_counter = 0
                player_counter = 0
                dealer_variable_list = []
                player_variable_list = []

                while counter < len(dealer_cards) + len(player_cards):

                    if dealer_counter < len(dealer_cards):
                        dealer_variable_list.append(f"{counter}_dealerCard")

                        counter += 1
                        dealer_counter += 1

                    else:
                        player_variable_list.append(f"{counter4}_playerCard")

                        counter4 += 1
                        player_counter += 1

                counter2 = 0
                picture_list_dealer = []
                picture_list_player = []




                if first_loop:
                    num = 0
                    for card in cards_to_play_out:
                        if num <= 1:
                            dealer_cards.append(card)
                            num += 1
                        else:
                         player_cards.append(card)
                    first_loop = False

                for name in dealer_variable_list:
                    name = pygame.image.load(f"{dealer_cards[counter2]}.png")
                    picture_list_dealer.append(name)
                    counter2 += 1

                counter3 = 0

                for name in player_variable_list:
                    name = pygame.image.load(f"{player_cards[counter3]}")
                    picture_list_player.append(name)

                    counter3 += 1

                #for name in picture_list_dealer:
                #    screen.blit(name, (100,50)) 
                #for name in picture_list_player:
                #    screen.blit(name, (200,200)) 

                for card in picture_list_dealer:
                    screen.blit(card, (dealer_start_print,20))
                    dealer_start_print += 54
                    pygame.display.flip()
                    print("Got this far")

                for card in picture_list_player:
                    screen.blit(card, (player_start_print, 450))
                    player_start_print += 54
                    pygame.display.flip()

                for event in pygame.event.get():
                    if event == pygame.KEYDOWN:
                        if event == pygame.K_RETURN:
                            if user.lower().strip() == "hit":
                                #If the user wants another card
                                try:
                                    #Easiest solution. It dosen't need to be fast, so its not a huge deal
                                    #Talk about indentation.
                                    new_card_num = randint(0,51)
                                    player_cards.append(hashable_dict[new_card_num])
                                    deck[hashable_dict[new_card_num]] -= 1
                                    return black_jack_round(deck, dealer_cards, player_cards = player_cards, cards= 4,user='', bet= bet, first_loop=False, player_monies=player_monies) #Bruh.
                                except KeyError:
                                    return black_jack_round(deck, user='hit', dealer_cards= dealer_cards, player_cards=player_cards, cards=4, bet=bet, first_loop= False, player_monies=player_monies)

                            elif user.lower().strip() == 'double':
                                #If the user wants another card, and is feelin' lucky.
                                try:
                                    new_card_num = randint(0,51)
                                    player_cards.append(hashable_dict[new_card_num])
                                    deck[hashable_dict[new_card_num]] -= 1
                                    if bet*2 <= player_monies:
                                        return black_jack_round(deck, dealer_cards, player_cards = player_cards, cards= 4,user='hit', first_loop=False, bet = 2*bet, player_monies=player_monies, stay=True) #Bruh.
                                    else:
                                        #Insert case here for you can't do that (parce que ne pas assez argents) but in a pygameish way ya' know.
                                        undertale_print_pygame("You dont have assez argents bud")
                                        return black_jack_round(deck, dealer_cards, player_cards = player_cards, cards = 4, user = '', first_loop=False, bet = bet, player_monies=player_monies)

                                except KeyError:
                                    return black_jack_round(deck, user='double', dealer_cards= dealer_cards, player_cards=player_cards, cards=4, bet=bet, first_loop= False, player_monies=player_monies)

                            elif user.lower().strip() == 'stay':
                                return black_jack_round(deck, dealer_cards, player_cards = player_cards, cards= 4,user='stay', first_loop=False, bet = 2*bet, player_monies=player_monies, stay=True) #Bruh.



                        elif event == pygame.K_BACKSPACE:
                            return black_jack_round(deck, user[:-1], dealer_cards, player_cards, cards = 4, first_loop=False, bet = bet )
            elif stay and user == 'stay':
                pass

        else:
            undertale_print_pygame("You busted")
            undertale_print_pygame("Dealers cards were")
            for card in dealer_cards:
                undertale_print_pygame(f"{card}")
            return player_monies - bet
    else:
        return 0








    return 0

def undertale_print_pygame(string: str) -> None:
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


def score_eval_BJ(cards: list) -> int:
    """Evaluates the value of a hand in blackjack."""
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


suits = ['hearts', 'diamonds', 'clubs', 'spades']
ranks = ['2', '3', '4', '5', '6', '7', '8',
         '9', '10', 'jack', 'queen', 'king', 'ace']

var_list = []

for suit in suits:
    for rank in ranks:
        # Gets the list for the images ready with their proper names
        var_list.append(f"{rank}_{suit}")

card_imaged = {}

for name in var_list:
    # Redeclares them for easy access in showing the images
    image = pygame.image.load(f"{name}.png")
    card_imaged[name] = image
    print(f"image for {name} created")


back_ground = pygame.image.load("Background_photo.png")
back_ground = pygame.transform.scale(back_ground, (1000, 600))


for rank in ranks:
    for suit in suits:
        deck.update({
            f"{rank}_{suit}": 1
        })

player_monies = 1000
print("\x1b[2J\x1b[H", end="")


# number_of_decks = int(input("How many decks would you like to play with? "))
# cut_card = int(input("How many decks do you want to play out? "))

running = True


image = pygame.image.load("All_cards.png")
screen = pygame.display.set_mode((1000, 600))
clock = pygame.time.Clock()
pygame.display.set_caption("Show an image")

font = pygame.font.Font(None, 48)
input_box = pygame.Rect(250, 500, 500, 50)
BJ_input_box = pygame.Rect(250, 500, 500, 50)
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive

active = False
round_in_progress = False
typing = False
BJ_text = ''
text = ''


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            color = color_active if active else color_inactive

        elif event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN and text.lower().strip() != "quit" and text.lower().strip() != "play":
                    undertale_print_pygame(text)
                    print("User types:", text)
                    try:
                        image = card_imaged[text.lower().strip()]
                        screen.blit(image, (490, 400))
                        pygame.display.flip()
                        sleep(4)
                    except (TypeError, SyntaxError, KeyError):
                        print("Error occured")
                        print(type(text))
                    text = ''
                elif text.lower().strip() == "play":
                    round_in_progress = True
                    while round_in_progress:

                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                mouse = pygame.mouse.get_pos()
                                if BJ_input_box.collidepoint(mouse):
                                    typing = not typing

                            elif event.type == pygame.KEYDOWN and typing:
                                if event.key == pygame.K_RETURN:
                                    player_monies += black_jack_round(deck, screen, back_ground, BJ_text, player_monies=player_monies)
                                    BJ_text = ''
                                elif event.key == pygame.K_BACKSPACE:
                                    BJ_text = BJ_text[:-1]
                                else:
                                    BJ_text += event.unicode

                        screen.blit(back_ground, (0,0))
                        BJ_txt_surface = font.render(BJ_text, True, color)
                        BJ_width = max(500, BJ_txt_surface.get_width()+10)
                        BJ_input_box.w = BJ_width
                        print(BJ_text)
                        screen.blit(BJ_txt_surface, (BJ_input_box.x + 5, BJ_input_box.y + 5))

                        pygame.draw.rect(screen, color, BJ_input_box)
                        pygame.display.flip()

                        clock.tick(30)
                elif text.lower().strip() == 'quit':
                    undertale_print_pygame("Quit sequence initialised.")
                    pygame.QUIT
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                elif text.lower().strip() == "play":

                    pass
                else:
                    text += event.unicode

    
    

    screen.fill((255, 255, 255))

    screen.blit(back_ground, (0, 0))

    txt_surface = font.render(text, True, color)

    width = max(500, txt_surface.get_width()+10)
    input_box.w = width

    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    pygame.draw.rect(screen, color, input_box, 2)

    score = font.render(f"{player_monies}", True, 'Black')
    screen.blit(score, (50,20))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
sys.exit()

while round_in_progress:
    typing = False
    screen.blit(back_ground)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            BJ_text = ''
            mouse = pygame.mouse.get_pos()[0]
            if BJ_input_box.collidepoint(mouse):
                typing = not typing

        if event.key == pygame.KEYDOWN:
            if typing:
                if event.key == pygame.K_RETURN:
                    player_monies += black_jack_round(deck, screen, back_ground, BJ_text, player_monies=player_monies)

                elif event.key == pygame.K_BACKSPACE:
                    BJ_text = BJ_text[:-1]

                else:
                    BJ_text += event.unicode

    BJ_txt_surface = font.render(BJ_text, True, "Black")
    BJ_width = max(500, BJ_txt_surface.get_width()+10)
    BJ_input_box.w = BJ_width

    screen.blit(BJ_txt_surface, (BJ_input_box.x + 5, BJ_input_box.y + 5))

    pygame.draw.rect(screen, color, BJ_input_box, 2)
    pygame.display.update()

    clock.tick(30)



