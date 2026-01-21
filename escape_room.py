"""This module is a beautiful single player adventure escape game in the making"""

from time import sleep
from os import system


def cleanup_time() -> None: # Apparently codeHS cannot access os
    system('cls')


long_message = True
# Will be True once the user gets to the point where they follow Thorn.
# Its here becuase I do not have time to go write out millions storylines, so all choices funnel the user into following Thorn.
answer_pillar1 = False
discovery_phase = True
first_time = True
final_phase = True
hollow_dialogue = True

inventory = []
clues_found = []
start_items = ['dagger','note','mirror']


def undertale_print(string: str) -> None:
    """Prints out messages in the generative style of undertale"""
    character = 0
    while character < len(string):
        if string[character] == " ":
            print(string[character], end="", flush=True)
            character += 1
        else:
            print(string[character], end="", flush=True)
            character += 1
            sleep(.05)
    print()


def undertale_print_customTime(string: str, time: float) -> None:
    """Prints out messages in the generative style of undertale"""
    character = 0
    while character < len(string):
        if string[character] == " ":
            print(string[character], end="", flush=True)
            character += 1
        else:
            print(string[character], end="", flush=True)
            character += 1
            sleep(time)
    print()


def undertale_print_Reg(string: str) -> None:
    """Prints out messages in the generative style of undertale according to a customised time"""
    character = 0
    while character < len(string):
        if string[character] == " ":
            print(string[character], end="", flush=True)
            character += 1
        else:
            print(string[character], end="", flush=True)
            character += 1
            sleep(.05)
    print()


"""
def check_inventory(item: str) -> bool:
    if item in inventory:
        return bool(1)
    else:
        return bool(0)
"""


def tunnel_crossroads():
    undertale_print("You see three ways\n"
                    "one, leading towards a prison like area.\n"
                    "The second, leading towards a mysterious tunnel.\n"
                    "The final (third), emitting the eerie echoe of trapped souls.")
    tunnel_choice = str(input("Make your move (1, 2, or 3) "))
    print("\x1b[2J\x1b[H", end="")
    return tunnel_choice


def return_to_start():
    """This function runs when the player returns to the start to pick up the items"""
    undertale_print("You return to the start for answers\n"
                    f"The {len(start_items)} original items rest: ")
    index = 1
    for i in start_items:
        print(f"{index}. {i}, " , end = "", flush = True)
        index += 1
        if index <= 3:
            sleep(.7)

    undertale_print("You are feeling starved from being in the prison so long\n"
                    "and can only take one item with you")
    item_choice = int(input("Which item will you take? "))
    if "memory of the king's silence" in inventory and len(inventory) <= 1:
        return item_choice
    elif "memory of the king's silence" not in inventory and len(inventory) == 0:
        return item_choice
    else:
        undertale_print("You are over encumbered.")
        undertale_print("You return back to the crossroads to make your next choice.")


def add_to_inventory(item):
    if item not in inventory:
        inventory.append(item)
        print(f"{item} added to your inventory.")
    else:
        print(f"You already have the {item}.")


def show_inventory():
    print("Your inventory contains:")
    for item in inventory:
        print(f"- {item}")


def chamber_choice(truthy_value: bool) -> str:
    """For when the user first looses sight of Thorn."""
    if truthy_value:
        undertale_print_Reg("You notice a breeze coming from a stone behind you.\n"
                            "Upon inspection, you notice a small crawlspace\n"
                            "leading to a hidden chamber")
        undertale_print_Reg("Inside the chamber\n"
                            "you notice a stone pedestal.")
        undertale_print_Reg("Upon inspection, you see three indentations:\n"
                            "mirror, dagger, note.")
        undertale_print_Reg("You turn around, ready to continue your search\n"
                            "when you notice a riddle etched into the wall")
        undertale_print_Reg(
            "It reads: \"\x1B[3mThe key is not held. It is known. Seek the third.\x1b[0m\"")
        undertale_print_Reg(
            "You feel the pedestal shift, revealing two paths.")
        undertale_print_Reg("1. Descend deeper into the dungeon.")
        undertale_print_Reg("2. Return to the start and search for answers.")
        chamber_answer = input("Make your move ")
    else:
        undertale_print_Reg("1. Descend deeper into the dungeon.")
        undertale_print_Reg("2. Return to the start and search for answers.")
        chamber_answer = input("Make your move ")
    return chamber_answer


def chamber_choice_cont1(choice: str) -> str:
    """For the user to make the choice after they discover the\n
    chamber and the message on its wall"""
    if choice == '1':
        cont1_choice = tunnel_crossroads()
    elif choice == '2':
        cont1_choice = return_to_start()
    return cont1_choice


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
        door_choice = input("Make your move ")
        if door_choice.strip() == '1':
            undertale_print("You see a long and thin stone bridge,\n" \
            "and in front of it rests a steel statue of a knight guarding the bridge.")
            sleep(1)
            undertale_print("You approach the statue and just as you are to pass\n" \
            "to cross the bridge it comes alive and throws you back saying")
            did_player_win = The_Hollow_Guard()
            return did_player_win
    
    elif choice == 1 and len(start_items) >= 1:
        add_to_inventory(start_items[choice - 1])
        remove_item = start_items.index("dagger")
        start_items.pop(remove_item)
        undertale_print("You return back to the crossroads to make your next choice.")
        return '0'
    
    elif choice == 2 and len(start_items) >= 2:
        add_to_inventory(start_items[choice - 1])
        remove_item = start_items.index("note")
        start_items.pop(remove_item)
        undertale_print("You return back to the crossroads to make your next choice.")
        return '0'
    
    elif choice == 3 and len(start_items) == 3:
        add_to_inventory(start_items[choice - 1])
        remove_item = start_items.index("mirror")
        start_items.pop(remove_item)
        undertale_print("You return back to the crossroads to make your next choice.")
        return'0'


def forgotten_scribe(ask: str) -> None:
    """The function runs if the player decides to search the alcove\n
    near the sigil chamber"""
    if ask == '1':
        undertale_print("Upon your discovery of the secret chamber\n"
                        "in the hidden alcove\n"
                        "you see a prisoner.\n"
                        "Looking half starved\n"
                        "he looks up at you and says nothing")
        sleep(1)
        undertale_print("Your options are as follows:\n"
                        "1. Ask the prisoner his name\n"
                        "2. Leave the alcove and search for more clues.")
        scribe_answer = input("Make your move ")
        while True:
            if scribe_answer == '1':
                undertale_print("He smirks")
                sleep(1)
                undertale_print("You know you're never gonna get outta here.")
                sleep(1)
                undertale_print_customTime("Right?", .1)
                sleep(1)
                undertale_print("He speaks through short breaths\n"
                                "but eventually he tells you something about\n"
                                "the kings ritual. Something about a chamber of mirrors\n")
                sleep(1)
                undertale_print("Just before sleep takes him, he mutters:")
                undertale_print(
                    '"The merchant remembers what the king forgot..."')
                clues_found.append("merchant memory hint")
                break
            elif scribe_answer == '2':
                undertale_print("You leave the chamber\n"
                                "wondering if you're ever going to find your way out of this place")
                break


def Merchant_of_Echoes():
    """This NPC is a mysterious figure who will offer\n
    memories for items"""
    sleep(.2)
    undertale_print("You make your way down the mysterious passage\n" \
    "and find yourself facing a strange man behind a counter\n" \
    "draped in a ragged cloth.")
    sleep(1)
    undertale_print("The Merchant of Echoes gestures to a shelf of empty bottles.\n" \
    '"I sell what was forgotten," he rasps. But I have a price')
    sleep(1)
    undertale_print(
    "Show me my soul and look into the past\n" 
    "Make me bleed, and see what came last\n" 
    "Let me read, and discover the knights breed.")
    item_for_merchant = input("What will you give to the merchant (1. dagger 2. mirror 3. note)? ")
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
        undertale_print("You return back to the crossroads to make your next choice.")

    elif item_for_merchant == '1' and 'dagger' in inventory:
        undertale_print("The knife is hidden to cover the kings bloody deed,\n" \
        "but a memory is missing if you want what you need.")
        pop_item = inventory.index("dagger")
        inventory.pop(pop_item)
        undertale_print("You return back to the crossroads to make your next choice.")

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
        pop_item = inventory.index("mirror")
        inventory.pop(pop_item)
        undertale_print("You return back to the crossroads to make your next choice.")


    elif item_for_merchant == '3' and 'note' in inventory:
        undertale_print("Heres a special token\n" \
        "readable only by the broken.\n" \
        "It's a map.\n" \
        "You wouldn't of noted given you're only human,\n" \
        "but it says the bars are the key to finding the knights memory,\n" \
        "and the echoes of the souls is where he hides.")
        pop_item = inventory.index("note")
        inventory.pop(pop_item)
        undertale_print("You return back to the crossroads to make your next choice.")
    
    else: 
        undertale_print("You have not the item you say you do.")
        undertale_print("You return back to the crossroads to make your next choice.")


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
            global mystery_time
            mystery_time = False
            return bool(1)
            
        else:
            undertale_print_Reg("You're a liar. Leave and never come back.")
            undertale_print("You return back to the crossroads to make your next choice.")
            return bool(0)


def player_wins():
    undertale_print_Reg("Escaping into the light of the world\n" \
    "you feel confident that no mysteries of the dungeon remain.")


super_dramatic_opening = """
You awaken in darkness.
The air is damp, thick with the scent of mildew and stone. A single torch flickers on the far wall, casting long shadows across the jagged floor.
You're lying on cold flagstone, your wrists sore from iron shackles that are now mysteriously unlocked.
You don't remember how you got here—only fragments: a banquet, a scream, a flash of steel.
You're in a dungeon beneath Castle Viremoor, a place whispered about in taverns and feared by locals.
Legends say no one escapes its depths—not because of the chains, but because of what lurks in the layers below.
A rusted door creaks open behind you. Footsteps echo. Someone—or something—is coming.
"""


prisoner_dialogue_choose1 = """
The prisoner flinches as you step from the shadows.
His eyes are wild, darting between you and the corridor behind him.
He clutches a broken chain in one hand and a scrap of parchment in the other.
"You're not one of them... are you?" he whispers.
He speaks in riddles at first, but slowly reveals that he's been trapped here for years—not by chains, but by a curse tied to the castle's foundation.
He claims the dungeon is alive, shifting its walls and hiding its secrets from those who don't belong.
"""


undertale_print_customTime(super_dramatic_opening, .02)
continue_input = input(
    "Warning, before you start the game,\n"
    "it is not forgiving, (most of the time) so be careful as to\n"
    "how you input your answers and avoid spacing if possible.\n"
    "Press any key to continue, or type 'exit,' to quit: ")


def literally_just_the_game(first_answer):
    first_choice = chamber_choice_cont1(first_answer)
    second_choice = chamber_choice_cont2(first_choice)
    try:
        if second_choice == True:
            player_wins()
    except NameError:
        pass
    try:
        if second_choice == '1':
            forgotten_scribe('1')
    except NameError:
        pass


if continue_input.lower().strip() == "exit":
    exit(0)


undertale_print_customTime(
    "Your choices: \nHide behind the pillar and wait to see who enters. (press 1)\nGrab the torch and prepare to confront whatever approaches. (press 2)\nSearch the room for anything useful before you're discovered.(press 3)", .01)


while True:  # This loop waits until the user inputs something reasonable, like a choice, and then prints more dialogue for the continuation of the storyline.
    continue_input = input("Make your move ")
    if continue_input == str(1):  # If the user chose to hide behind the pillar
        undertale_print_Reg("What will you do next?")
        undertale_print_Reg(
            "1. Reveal yourself and speak to the cloaked prisoner.")
        undertale_print_Reg(
            "2. Follow him silently as he limps deeper into the dungeon.")
        undertale_print_Reg("3. Search the area he just came from.")
        pillar_choice = input("Make your move ")
        search_choice = 0
        torch_choice = 0
        break
    elif continue_input == str(2):  # If the user chose to grab the torch
        undertale_print_Reg("What will you do next?")
        undertale_print_Reg("1. Confront the gaoler and demand answers.")
        undertale_print_Reg("2. Extinguish the torch and try to sneak past.")
        torch_choice = input("Make your move ")
        pillar_choice = 0
        search_choice = 0
        break
    elif continue_input == str(3):  # If the user chose to search the room
        undertale_print_Reg("What will you take?")
        undertale_print_Reg("1. Take the dagger—prepare for combat.")
        undertale_print_Reg(
            "2. Take the mirror—perhaps it reveals hidden truths.")
        undertale_print_Reg(
            "3. Take the note—maybe it's a clue to the dungeon's secrets.")
        search_choice = input("Make your move ")
        pillar_choice = 0
        torch_choice = 0
        break
    elif continue_input.upper().strip() == "exit".upper():
        exit(0)
    else:
        undertale_print_Reg("Invalid user input")
print("\x1b[2J\x1b[H", end="")


while True:  # This part of the story funnels all choices into the user discovering the secret chamber
    if pillar_choice == '1':
        undertale_print_Reg(prisoner_dialogue_choose1)

        while not answer_pillar1:
            ask_pillar1 = input(
                "You are left with more questions than answers and so you decide to inquire further.\n"
                "1. Ask the prisoner his name\n"
                "2. Ask the prisoner why he's in the dungeon too: "
            )

            if ask_pillar1 == '1':
                undertale_print_Reg(
                    "I call myself Thorn. I was a scribe for the king. Once.")

            elif ask_pillar1 == '2':
                undertale_print_Reg(
                    "I was a scribe for the throne, but I discovered something.")
                undertale_print_Reg(
                    "Nevermind about that. What do you want from me?")

                ask_pillar1_2 = input(
                    "You still have questions.\n"
                    "Your options are as follows:\n"
                    "1. Inquire further about what he discovered\n"
                    "2. Ask him where he's going\n"
                )

                if ask_pillar1_2 == '1':
                    undertale_print_Reg("I told you not to mind about that.")

                elif ask_pillar1_2 == '2':
                    undertale_print_Reg("Why don't you come along?")
                    undertale_print_Reg("And take that torch with you,\n"
                                        "you'll need it")
                    undertale_print_Reg(
                        "With your curiosity for the mysteries of the cave expanding, you decide to follow Thorn deeper into the dungeon.")
                    answer_pillar1 = True  # Exit the inner loop
        break  # Exit the outer while loop once the pillar path is complete

    elif pillar_choice == '2':
        undertale_print_Reg(
            f"You begin to follow the mysterious prisoner, but you acidentally kick a rock.\nHe turns around and says \n{prisoner_dialogue_choose1}")
        while not answer_pillar1:
            ask_pillar1 = input(
                "You are left with more questions than answers and so you decide to inquire further.\n"
                "1. Ask the prisoner his name\n"
                "2. Ask the prisoner why he's in the dungeon too: "
            )

            if ask_pillar1 == '1':
                undertale_print_Reg(
                    "I call myself Thorn. I was a scribe for the king. Once.")

            elif ask_pillar1 == '2':
                undertale_print_Reg(
                    "I was a scribe for the throne, but I discovered something.")
                undertale_print_Reg(
                    "Nevermind about that. What do you want from me?")

                ask_pillar1_2 = input(
                    "You still have questions.\n"
                    "Your options are as follows:\n"
                    "1. Inquire further about what he discovered\n"
                    "2. Ask him where he's going\n"
                )

                if ask_pillar1_2 == '1':
                    undertale_print_Reg("I told you not to mind about that.")

                elif ask_pillar1_2 == '2':
                    undertale_print_Reg("Why don't you come along?")
                    undertale_print_Reg("And take that torch with you,\n"
                                        "you'll need it")
                    undertale_print_Reg(
                        "With your curiosity for the mysteries of the cave expanding, you decide to follow Thorn deeper into the dungeon.")
                    answer_pillar1 = True  # Exit the inner loop
        break

    elif pillar_choice == '3':
        undertale_print_Reg(
            "You search the area but find nothing. You decide to follow the mysterious prisoner")
        while not answer_pillar1:
            ask_pillar1 = input(
                "You are left with more questions than answers and so you decide to inquire further.\n"
                "1. Ask the prisoner his name\n"
                "2. Ask the prisoner why he's in the dungeon too: "
            )

            if ask_pillar1 == '1':
                undertale_print_Reg(
                    "I call myself Thorn. I was a scribe for the king. Once.")

            elif ask_pillar1 == '2':
                undertale_print_Reg(
                    "I was a scribe for the throne, but I discovered something.")
                undertale_print_Reg(
                    "Nevermind about that. What do you want from me?")

                ask_pillar1_2 = input(
                    "You still have questions.\n"
                    "Your options are as follows:\n"
                    "1. Inquire further about what he discovered\n"
                    "2. Ask him where he's going\n"
                )

                if ask_pillar1_2 == '1':
                    undertale_print_Reg("I told you not to mind about that.")

                elif ask_pillar1_2 == '2':
                    undertale_print_Reg("Why don't you come along?")
                    undertale_print_Reg("And take that torch with you,\n"
                                        "you'll need it")
                    undertale_print_Reg(
                        "With your curiosity for the mysteries of the cave expanding, you decide to follow Thorn deeper into the dungeon.")
                    answer_pillar1 = True  # Exit the inner loop
        break

    elif torch_choice == '1':
        undertale_print_Reg(
            f"You confront the prisoner, and he says {prisoner_dialogue_choose1}")
        while not answer_pillar1:
            ask_pillar1 = input(
                "You are left with more questions than answers and so you decide to inquire further.\n"
                "1. Ask the prisoner his name\n"
                "2. Ask the prisoner why he's in the dungeon too: "
            )

            if ask_pillar1 == '1':
                undertale_print_Reg(
                    "I call myself Thorn. I was a scribe for the king. Once.")

            elif ask_pillar1 == '2':
                undertale_print_Reg(
                    "I was a scribe for the throne, but I discovered something.")
                undertale_print_Reg(
                    "Nevermind about that. What do you want from me?")

                ask_pillar1_2 = input(
                    "You still have questions.\n"
                    "Your options are as follows:\n"
                    "1. Inquire further about what he discovered\n"
                    "2. Ask him where he's going\n"
                )

                if ask_pillar1_2 == '1':
                    undertale_print_Reg("I told you not to mind about that.")

                elif ask_pillar1_2 == '2':
                    undertale_print_Reg("Why don't you come along?")
                    undertale_print_Reg("And take that torch with you,\n"
                                        "you'll need it")
                    undertale_print_Reg(
                        "With your curiosity for the mysteries of the cave expanding, you decide to follow Thorn deeper into the dungeon.")
                    answer_pillar1 = True  # Exit the inner loop
        break

    elif torch_choice == '2':
        undertale_print_Reg(
            f"You rush to put out the torch but kick a rock.\nIt really hurts so you whimper a little.\nThe prisoner notices you and says {prisoner_dialogue_choose1}")
        while not answer_pillar1:
            ask_pillar1 = input(
                "You are left with more questions than answers and so you decide to inquire further.\n"
                "1. Ask the prisoner his name\n"
                "2. Ask the prisoner why he's in the dungeon too: "
            )

            if ask_pillar1 == '1':
                undertale_print_Reg(
                    "I call myself Thorn. I was a scribe for the king. Once.")

            elif ask_pillar1 == '2':
                undertale_print_Reg(
                    "I was a scribe for the throne, but I discovered something.")
                undertale_print_Reg(
                    "Nevermind about that. What do you want from me?")

                ask_pillar1_2 = input(
                    "You still have questions.\n"
                    "Your options are as follows:\n"
                    "1. Inquire further about what he discovered\n"
                    "2. Ask him where he's going\n"
                )

                if ask_pillar1_2 == '1':
                    undertale_print_Reg("I told you not to mind about that.")

                elif ask_pillar1_2 == '2':
                    undertale_print_Reg("Why don't you come along?")
                    undertale_print_Reg("And take that torch with you,\n"
                                        "you'll need it")
                    undertale_print_Reg(
                        "With your curiosity for the mysteries of the cave expanding, you decide to follow Thorn deeper into the dungeon.")
                    answer_pillar1 = True  # Exit the inner loop
        break

    elif search_choice == '1':  # The player is very cruel
        undertale_print_Reg("You grab the dagger, and as soon as the prisoner sees you, he turns around and starts whimpering.\n"
                            f"Feeling bad, you comfort him and ask him what he's doing in the dungeon. He says {prisoner_dialogue_choose1}")
        while not answer_pillar1:
            ask_pillar1 = input(
                "You are left with more questions than answers and so you decide to inquire further.\n"
                "1. Ask the prisoner his name\n"
                "2. Ask the prisoner why he's in the dungeon too: "
            )

            if ask_pillar1 == '1':
                undertale_print_Reg(
                    "I call myself Thorn. I was a scribe for the king. Once.")

            elif ask_pillar1 == '2':
                undertale_print_Reg(
                    "I was a scribe for the throne, but I discovered something.")
                undertale_print_Reg(
                    "Nevermind about that. What do you want from me?")

                ask_pillar1_2 = input(
                    "You still have questions.\n"
                    "Your options are as follows:\n"
                    "1. Inquire further about what he discovered\n"
                    "2. Ask him where he's going\n"
                )

                if ask_pillar1_2 == '1':
                    undertale_print_Reg("I told you not to mind about that.")

                elif ask_pillar1_2 == '2':
                    undertale_print_Reg("Why don't you come along?")
                    undertale_print_Reg("And take that torch with you,\n"
                                        "you'll need it")
                    undertale_print_Reg(
                        "With your curiosity for the mysteries of the cave expanding, you decide to follow Thorn deeper into the dungeon.")
                    answer_pillar1 = True  # Exit the inner loop
        break

    elif search_choice == '2':  # If the user chose to take the mirror
        undertale_print_Reg(
            "It turns out that it's just an ordinary mirror so you decide to follow the prisoner.")
        undertale_print_Reg(
            f"Whilst you are following him, you kick on a rock, and it really hurts so you start to whimper.\n The prisoner turns around and says\n{prisoner_dialogue_choose1}")
        while not answer_pillar1:
            ask_pillar1 = input(
                "You are left with more questions than answers and so you decide to inquire further.\n"
                "1. Ask the prisoner his name\n"
                "2. Ask the prisoner why he's in the dungeon too: "
            )

            if ask_pillar1 == '1':
                undertale_print_Reg(
                    "I call myself Thorn. I was a scribe for the king. Once.")

            elif ask_pillar1 == '2':
                undertale_print_Reg(
                    "I was a scribe for the throne, but I discovered something.")
                undertale_print_Reg(
                    "Nevermind about that. What do you want from me?")

                ask_pillar1_2 = input(
                    "You still have questions.\n"
                    "Your options are as follows:\n"
                    "1. Inquire further about what he discovered\n"
                    "2. Ask him where he's going\n"
                )

                if ask_pillar1_2 == '1':
                    undertale_print_Reg("I told you not to mind about that.")

                elif ask_pillar1_2 == '2':
                    undertale_print_Reg("Why don't you come along?")
                    undertale_print_Reg("And take that torch with you,\n"
                                        "you'll need it")
                    undertale_print_Reg(
                        "With your curiosity for the mysteries of the cave expanding, you decide to follow Thorn deeper into the dungeon.")
                    answer_pillar1 = True  # Exit the inner loop
        break
    elif search_choice == '3':  # The user chose to take the note
        undertale_print_Reg(
            "The prisoner sees you as you are searching. You turn around and demand answers.")
        undertale_print_Reg("The prisoner says " + prisoner_dialogue_choose1)
        while not answer_pillar1:
            ask_pillar1 = input(
                "You are left with more questions than answers and so you decide to inquire further.\n"
                "1. Ask the prisoner his name\n"
                "2. Ask the prisoner why he's in the dungeon too: "
            )

            if ask_pillar1 == '1':
                undertale_print_Reg(
                    "I call myself Thorn. I was a scribe for the king. Once.")

            elif ask_pillar1 == '2':
                undertale_print_Reg(
                    "I was a scribe for the throne, but I discovered something.")
                undertale_print_Reg(
                    "Nevermind about that. What do you want from me?")

                ask_pillar1_2 = input(
                    "You still have questions.\n"
                    "Your options are as follows:\n"
                    "1. Inquire further about what he discovered\n"
                    "2. Ask him where he's going\n"
                )

                if ask_pillar1_2 == '1':
                    undertale_print_Reg("I told you not to mind about that.")
                    answer_pillar1 = False
                elif ask_pillar1_2 == '2':
                    undertale_print_Reg("Why don't you come along?")
                    undertale_print_Reg("And take that torch with you,\n"
                                        "you'll need it")
                    undertale_print_Reg(
                        "With your curiosity for the mysteries of the cave expanding, you decide to follow Thorn deeper into the dungeon.")
                    answer_pillar1 = True  # Exit the inner loop
        break
print("\x1b[2J\x1b[H", end="")


while long_message:
    print()
    undertale_print_Reg("Thorn leads you through a narrow passage lit only by the flicker of the torch\n"
                        "The air grows colder. You descend a spiral staircase carved into the stone\n"
                        "until you reach a sealed door etched with a glowing sigil"
                        )
    print()
    undertale_print_Reg(
        "Thorn tells you that he's been trying to open the door for years but to no avail .")
    undertale_print_Reg(
        "Apparently, there is a key hidden somewhere in the depths of the dungeon")
    undertale_print_Reg("promising to reveal the secrets behind the door.")
    undertale_print_Reg(
        "He says something about a third something, or someone")
    undertale_print_Reg(
        "and before you realise it, Thorn is nowhere to be found.")
    break
print("\x1b[2J\x1b[H", end="")

while discovery_phase:  # Setting up for the gigaloop
    undertale_print_Reg("Left alone, facing the sealed door\n"
                        "You look around for clues.\n"
                        "What will you do\n")
    undertale_print_Reg("1. Search the area for clues.")
    undertale_print_Reg("2. Call out for Thorn.")
    undertale_print_Reg("3. Try to open the door yourself.\n")

    discovery_phase_choice = input("Make your move ")
    if discovery_phase_choice == '1':
        mystery_time = True
        discovery_phase = False
    elif discovery_phase_choice == '2':
        undertale_print_Reg("With no answer but the silent echo of your voice,\n"
                            "you decide the atempt was in vain and attempt to search the cave")
        mystery_time = True
        discovery_phase = False
    elif discovery_phase_choice == '3':
        undertale_print_Reg("Just as Thorn said, the door cannot be opened")
        undertale_print_Reg(
            "Feeling a little pathetic, you decide to search the chamber")
        mystery_time = True
        discovery_phase = False


while mystery_time:
    if first_time:
        chamber_answer = chamber_choice(first_time)
        first_time = False
    else:
        chamber_answer = chamber_choice(bool(0))

    literally_just_the_game(chamber_answer)
    sleep(1)
    print("\x1b[2J\x1b[H", end = "")
