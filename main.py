
story = {
    "Intro": "As dawn breaks, a weary radio transmission buzzes through: "
             "\n'Survivors, find shelter. Trust no one.' The once bustling \n"
             "city lies in ruins; the undead roam freely. Your choices now "
             "will \nshape your destiny and perhaps that of humanity.\n",
    "Narratives": {
        "1": "Your safe-house, a small apartment on the 3rd floor, "
             "is \ncompromised. The scent of fresh blood has attracted a "
             "horde. \nYou're low on supplies and the noises downstairs "
             "suggest \n"
             "they're closing in.",
        "1A": "You carefully make your way down the back staircase. The alley \n"
              "is eerily quiet, save for distant screams.",
        "1B": "Using furniture, you barricade the door. The growling outside "
              "\nintensifies as shadows pass the window.",
        "1A-2A": "The supermarket's glass doors are shattered, but you can "
                 "spot \n canned food on the shelves. However, something "
                 "moves in the dark.",
        "1A-2B": "You discover an old warehouse. The heavy metal doors appear \n"
                 "secure. There's potential here.",
        "1B-2A": "Using a flashlight, you signal SOS. A faint light responds "
                 "\nfrom a distant building.",
        "1B-2B": "Hours feel like days. The growling diminishes but you can "
                 "\nhear them lurking.",
        "1A-2A-3A": "You hurriedly grab cans, but a noise stops you. It's a "
                    "\ncat. Relieved, you prepare to leave, when a soft voice \n"
                    "asks for help.",
        "1A-2A-3B": "As you approach, you're ambushed! It's not zombies, "
                    "but \ndesperate survivors. They demand your supplies.",
        "1A-2B-3A": "You set traps and create lookout points. The warehouse "
                    "\nbecomes a fortress, but at the cost of drawing "
                    "attention.",
        "1A-2B-3B": "You find a group of survivors. They share tales of a "
                    "\nsafe haven up north.",
        "1B-2A-3A": "The responding light is from a group of survivors. "
                    "\nThey're well-armed but friendly and offer shelter.",
        "1B-2A-3B": "At dawn, the streets are clearer. You begin your "
                    "journey, \nbut the undead are everywhere.",
        "1B-2B-3A": "You discover medical supplies. But as you pocket them, "
                    "\nthe door slams shut. You're not alone.",
        "1B-2B-3B": "Jumping out, you land in an alley. You're safe, but lost."
    },
    "Decisions": {
        "1": {"A": "Sneak out through the back.", "B": "Barricade and defend your position."},
        "1A-2": {"A": "Head to the supermarket for supplies.", "B": "Search for a new safe-house."},
        "1B-2": {"A": "Signal for help from the balcony.", "B": "Wait silently and hope they move on."},
        "1A-2A-3": {"A": "Grab food quickly and leave.", "B": "Investigate the movement."},
        "1A-2B-3": {"A": "Fortify the warehouse.", "B": "Scout the surrounding area."},
        "1B-2A-3": {"A": "Head towards the responding light.", "B": "Stay put and prepare to leave at first light."},
        "1B-2B-3": {"A": "Check other rooms for supplies.", "B": "Escape through the window."},
        "1A-2A-3A-4": {"A": "Help the stranger.", "B": "Exit immediately."},
        "1A-2A-3B-4": {"A": "Offer some supplies for peace.", "B": "Refuse and ready for a fight."},
        "1A-2B-3A-4": {"A": "Stay and defend.", "B": "Abandon the warehouse."},
        "1A-2B-3B-4": {"A": "Join them to the safe haven.", "B": "Continue on your own."},
        "1B-2A-3A-4": {"A": "Join their group.", "B": "Decline and continue alone."},
        "1B-2A-3B-4": {"A": "Find a vehicle.", "B": "Travel by foot."},
        "1B-2B-3A-4": {"A": "Confront the intruder.", "B": "Find another exit."},
        "1B-2B-3B-4": {"A": "Use your map to navigate.", "B": "Search for high ground."}
    },
    "Endings": {
        "1A-2A-3A-4A": "You and the stranger form a bond, but 1 week later "
                       "you \nwake up to the stranger turned into a zombie. "
                       "She bites you. \nYou have died.",
        "1A-2A-3A-4B": "You don't trust anyone, Alone, you find an "
                       "\nunderground shelter, hiding until the apocalypse ends."
                       "\nYou survived, but die of old age, still alone.",
        "1A-2A-3B-4A": "The survivors respect you, and together you find a "
                       "\nquiet town to rebuild.",
        "1A-2A-3B-4B": "Betrayed, you're left for dead, with no supplies and "
                       "surrounded\nby zombies you only last a few days. \nYou "
                       "have died",
        "1A-2B-3A-4A": "The warehouse becomes a beacon of hope, thriving "
                       "against odds.\n You welcome in other lost people and "
                       "live through the apocalypse.",
        "1A-2B-3A-4B": "On the road, you last for as long as your supplies go but"
                       "\n with no supplies and no where to go you starve to "
                       "death.",
        "1A-2B-3B-4A": "The safe haven exists, but it has been overrun, "
                       "\nwith no where to go the undead begin to slowly "
                       "\novertake your group one by one until your turn. "
                       "\nYou have died.",
        "1A-2B-3B-4B": "Alone, you find solace in the wilderness, living "
                       "\noff-grid. Some other survivors stumble onto your camp "
                       "\nand you welcome them in, together you live a long "
                       "life.",
        "1B-2A-3A-4A": "With the group, you create a bustling community to "
                       "\nlive out the apocalypse together.",
        "1B-2A-3A-4B": "Alone, you become a legend, saving many but "
                       "\neventually you end up dying in an attempt to save a "
                       "\ngroup of stuck survivors.",
        "1B-2A-3B-4A": "With a vehicle, you journey far finding supplies on "
                       "\nthe way. after months you travel to a major city and "
                       "\nfind that a local scientist has found a cure.",
        "1B-2A-3B-4B": "Walking, you inspire others to form a massive convoy, \n"
                       "moving to safety.",
        "1B-2B-3A-4A": "The intruder is a scientist who claims to have a "
                       "\npotential cure. After weeks you start to question the "
                       "\nscientist and find that he was the one who started "
                       "\nthe plague. He knows you know and intentionally "
                       "\npoisons you.",
        "1B-2B-3A-4B": "Escaping, you stumble upon an untouched village. You "
                       "\nset up shop and people slowly stumble upon you. "
                       "\neventually you have an entire safe community to "
                       "\nsurvive the apocalypse.",
        "1B-2B-3B-4A": "From high ground, you spot a military base and signal them."
                       "\nThey give you information about a safe zone establish about "
                       "\ntwo miles north. You make it there and live out the "
                       "\napocalypse.",
        "1B-2B-3B-4B": "Lost and alone you make it until your supplies run "
                       "\nout and then you starve to death."
    }
}


def print_narrative(narrative_spot, level):
    print(story["Narratives"][narrative_spot])
    printed_story.write(story["Narratives"][narrative_spot])
    level += 1
    return narrative_spot + "-{}".format(level), level


def handle_decision(decision):
    print("A: {}".format(story["Decisions"][decision]["A"]))
    printed_story.write("\nA: {}".format(story["Decisions"][decision]["A"]))
    print("B: {}".format(story["Decisions"][decision]["B"]))
    printed_story.write("\nB: {}".format(story["Decisions"][decision]["B"]))
    while True:
        chosen_path = input()
        if chosen_path.lower() == "a" or chosen_path.lower() == 'b':
            printed_story.write("\nYou chose: {}\n".format(chosen_path.upper()))
            return chosen_path.upper()
        else:
            print("Please enter one of the following to choose a path: A, a, "
                  "B, b")


print("Welcome to \"Choose your own story, Undead Edition\" a game where you \n"
      "decide where the story takes you, do you have what it takes to "
      "survive?\n")
print("Here is how it works. you are going to be taken through the story\n"
      "and you will be given decisions, it's up to you to make the right \n"
      "decisions and survive to tell the tale. To make a decision \ntype in A "
      "or B to make your decision.\n")
input("Press [Enter] to continue.\n")

while True:
    clear_file = open("ZombieAdventure.txt", 'w')
    clear_file.close()
    printed_story = open("ZombieAdventure.txt", 'a+')
    print(story["Intro"])
    printed_story.write(story["Intro"])
    input("Press [Enter] to continue.\n")
    current_spot = "1"
    print(story["Narratives"][current_spot])
    printed_story.write(story["Narratives"][current_spot])
    current_spot = "{}{}".format(current_spot, handle_decision(current_spot))
    current_level = 1
    while True:
        current_spot, current_level = print_narrative(current_spot,
                                                      current_level)
        current_spot = "{}{}".format(current_spot, handle_decision(
            current_spot))
        if current_level == 4:
            break
    print(story["Endings"][current_spot])
    printed_story.write(story["Endings"][current_spot])
    print("\n\nYour story has been printed to the file ZombieAdventure.txt\n"
          "if you would like to keep that story please rename the file, \n"
          "otherwise it will be overwritten next time you play.")
    printed_story.close()
    while True:
        player_input = input("Would you like to play again (Y/N): ")
        if player_input.lower() == 'y':
            break
        elif player_input.lower() == 'n':
            exit(0)
        else:
            print("Please enter one of the following: Y, y, N, n")