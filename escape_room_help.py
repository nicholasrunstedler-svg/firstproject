from functions import undertale_print, undertale_print_customTime 
from time import sleep
from escape_room import add_to_inventory, undertale_print_Reg
inventory = []
clues_found = []

def check_inventory(item: str) -> bool:
    if item in inventory:
        return bool(1)
    else:
        return bool(0)

def chamber_choice_cont1(choice: str) -> str:
    """For the user to make the choice after they discover the\n
    chamber and the message on its wall"""
    if choice == '1':
        cont1_choice = tunnel_crossroads()
    elif choice == '2':
        cont1_choice = return_to_start()
    return cont1_choice

def forgotten_scribe() -> None:
    """The function runs if the player decides to search the alcove\n
    near the sigil chamber"""
    undertale_print("Upon your discovery of the secret chamber\n"
                    "in the hidden alcove\n" \
                    "you see a prisoner.\n" \
                    "Looking half starved\n" \
                    "he looks up at you and says nothing")
    sleep(1)
    undertale_print("Your options are as follows:" \
    "1. Ask the prisoner his name\n" \
    "2. Leave the alcove and search for more clues.\n")
    scribe_answer = input()
    while True:
        if scribe_answer == '1':
            undertale_print("He smirks")
            sleep(1)
            undertale_print("You know you're never gonna get outta here.")
            sleep(1)
            undertale_print_customTime("Right?",.1)
            sleep(1)
            undertale_print("He speaks through short breaths\n" \
            "but eventually he tells you something about\n" \
            "the kings ritual. Something about a chamber of mirrors\n")
            sleep(1)
            undertale_print("Just before sleep takes him, he mutters:")
            undertale_print('"The merchant remembers what the king forgot..."')
            clues_found.append("merchant memory hint")

        elif scribe_answer == '2':
            undertale_print("You leave the chamber\n" \
            "wondering if you're ever going to find your way out of this place")

def The_Hollow_Guard() -> bool:
    """The function runs if the player speaks to the Hollow Guard\n
    blocking the passage to the bridge"""
    undertale_print_Reg("I am the Hollow Guard\n" \
    "I guard the bridge from any tespassers who might wish to cross\n" \
    "Are you a trespasser? (yes, or no)")
    sleep(1)
    guard_question1 = input("")
    if guard_question1.strip().lower() == 'yes':
        undertale_print_Reg("Well then begone fool\n" \
        "you shall never pass these gates\n" \
        "while the Hollow guard is here")
        sleep(1)
        undertale_print_Reg("And with that\n" \
        "you run off like a sissy")
    elif guard_question1.strip().lower() == 'no':
        undertale_print_Reg("And what prove have you of such gall to your name?")
        sleep(1)
        if "memory of the king's silence" in inventory:
            undertale_print_Reg("You give the guard the bottle memory,\n" \
            "and a flash of light fills the chamber\n" \
            "you are both brought back to a grand chamber.\n" \
            "You witness the third ritual of the king,\n" \
            "and you see the knight bore witness.")
            sleep(1.5)
            undertale_print_Reg("That is why he is in the dungeon.\n" 
            "He carried an unbearable guilt for not stopping the ritual,\n" \
            "and so locked himself and all witnesses in the dungeon\n" \
            "sealing the memory.")
            sleep(1.5)
            undertale_print_Reg("But after the ritual, he sealed away his memory\n" \
            "forgetting that you were the one who tried to stop the king,\n" \
            "you were the third witness.")
            sleep(1)
            undertale_print_Reg("With that, he apoligises for his deeds, turns, and jumps into the hollow depths.")
            return bool(1)
        else:
            undertale_print_Reg("You're a liar. Leave and never come back.")
            return bool(0)
        
def player_wins():
    undertale_print_Reg()


def Merchant_of_Echoes():
    """This NPC is a mysterious figure who will offer\n
    memories for items"""
    undertale_print("The Merchant of Echoes gestures to a shelf of empty bottles.\n" \
    '"I sell what was forgotten," he rasps. But I have a price')
    sleep(1)
    undertale_print(
    "Show me my soul and look into the past\n" 
    "Make me bleed, and see what came last\n" 
    "Let me read, and discover the knights breed.")
    item_for_merchant = input("What will you give to the merchant (1. dagger 2. mirror 3. note? ")
    if item_for_merchant == '1' and 'dagger' in inventory and "merchant memory hint" in clues_found:
        undertale_print("Blood was the first vow.\n" \
        "The king offered it freely,\n" \
        "thinking it would bind the silence")
        sleep(1)
        print("The merchant turns the blade to the light and says")
        sleep(1.7)
        undertale_print("But blood is loud.\n" \
        "It stains\n" \
        "It speaks\n" \
        "And the third saw everything.\n")
        add_to_inventory("memory of the king's silence")
        undertale_print("This is what the king tried to bury.\n" \
        "The moment he chose silence over truth.")

    elif item_for_merchant == '1' and 'dagger' in inventory:
        undertale_print("The knife is hidden to cover the kings bloody deed,\n" \
        "but a memory is missing if you want what you need.")

    elif item_for_merchant == '2' and 'mirror' in inventory:
        undertale_print("The merchant takes the mirror\n" \
        "but instead of looking into it\n" \
        "he handles it carefully, trembling.\n" \
        "He uncorks a bottle and pours a\n" \
        "whisper into the air.")
        sleep(1)
        undertale_print("\x1B[3mBefore the silence, there was a vow.\n" \
        "the king stood before three-his blade, his voice, and his shadow.\n" \
        "He swore to protect the realm\n" \
        "but feared the truth.\n" \
        "So he shattered it.\x1B[0m")

    elif item_for_merchant == '3' and 'note' in inventory:
        undertale_print("Heres a special token\n" \
        "readable only by the broken.\n" \
        "It's a map.\n" \
        "You wouldn't of noted given you're only human,\n" \
        "but it says the bars are the key to finding the knights memory,\n" \
        "and the echoes of the souls is where he hides.")

def tunnel_crossroads():
    undertale_print("You see three ways\n" 
                    "one, leading towards a prison like area.\n" 
                    "The second, leading towards a mysterious tunnel.\n" 
                    "The final (third), emitting the eerie echoe of trapped souls.")
    tunnel_choice = str(input("Make your move (1, 2, or 3) "))
    return tunnel_choice

def return_to_start():
    """This function runs when the player returns to the start to pick up the items"""
    undertale_print("You return to the start for answers\n" 
                    "The three original items rest:" 
                    "dagger, note, mirror")
    sleep(1)
    undertale_print("You are feeling starved from being in the prison so long\n" 
                    "and can only take one item with you")
    undertale_print("Choose 1. dagger 2. note 3. mirror")
    item_choice = int(input(""))
    return item_choice


def chamber_choice_cont2(choice) -> str:
    """This function prompts the user, either to\n
    speak to one of the NPCs if they chose the tunnel or\n
    to take the item back to the tunnel crossroads\n
    type(choice) == str -> function corresponds to tunnel_crossroads final input.\n
    type(choice) == int -> function corresponds to return_to_start final input.\n
    Make sure that this function is at the highest level of the giga while loop."""
    if choice == '1':
        undertale_print("You go to the area an see\n" \
        "prison cells filled with bones but\n" \
        "behind one rests a starved looking man.\n")
        sleep(1)
        undertale_print("1. Speak to the prisoner 2. Leave")
        ask_prisoner = input("")
        if ask_prisoner == '1':
            return ask_prisoner
        
    elif choice == '2':
        Merchant_of_Echoes()
        return '0'

    elif choice == '3':
        undertale_print("You walk down the eerie path\n" \
        "lit by nothing but the gradually dimming flicker of your torch\n" \
        "you feel the air get thicker, but eventually you come upon a great wooden door")
        sleep(1)
        undertale_print("Your choices: 1. Go through the door 2. Return back to the crossroads")
        door_choice = input(undertale_print("Make your move "))
        if door_choice == '1':
            undertale_print("You see a long and thin stone bridge,\n" \
            "and in front of it rests a steel statue of a knight guarding the bridge.")
            sleep(1)
            undertale_print("You approach the statue and just as you are to pass\n" \
            "to cross the bridge it comes alive and throws you back saying")
            did_player_win = The_Hollow_Guard()
            return did_player_win
    
    elif choice == 1:
        add_to_inventory("dagger")
        return '0'
    
    elif choice == 2:
        add_to_inventory("note")
        return '0'
    
    elif choice == 3:
        add_to_inventory("mirror")
        return'0'


def literally_just_the_game(first_answer):
    first_choice = chamber_choice_cont1(first_answer)
    second_choice = chamber_choice_cont2(first_choice)
    try:
        if second_choice:
            player_wins()
            global mystery_time
            mystery_time = False
    except NameError:
        pass
    try:
        if second_choice == '1':
            forgotten_scribe()
    except NameError:
        pass

    