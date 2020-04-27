# imports
from random import seed
from random import randint
import time


class Room:
    def __init__(self, name, description, examine):
        self.name = name
        self.description = description
        self.examine = examine
        self.next_location = []
        self.items = []
        self.characters = []
    def __repr__(self):
        return self.description


class Item:
    def __init__(self, name, inven_name, description, examine, weight):
        self.name = name
        self.inven_name = inven_name
        self.description = description
        self.examine = examine
        self.weight = weight
        self.amount = 1

    def __repr__(self):
        return self.description


class Character:
    def __init__(self, name, description, examine, health, location):
        self.name = name
        self.description = description
        self.examine = examine
        self.health = health
        self.location = location

    def __repr__(self):
        return self.description


class Inventory:
    def __init__(self):
        self.items = []
        self.health = 8
        self.deaths = 0

    def __repr__(self):
        if not self.items:
            return "You're not carrying anything at the moment!"
        else:
            ret_string = "You have: \n"
            for i in range(len(self.items)):
                if i < (len(self.items) - 1):
                    ret_string = ret_string + " - " + str(self.items[i].amount) + " " + self.items[i].inven_name + "\n"
                else:
                    ret_string = ret_string + " - " + str(self.items[i].amount) + " " + self.items[i].inven_name
            return ret_string


# Declare all the rooms
bedroom_entrance = Room("BEDROOM",
                        "You find yourself in a dimly lit BEDROOM. A crack of moonlight seeps into \
the room from your open window. A cool breeze brushes past your ear. On one side of the room you see your BED. \
On the far side you can see a closed set of CLOSET doors. Behind you is the door to the SOUTH_HALLWAY.",
                        "A normal bedroom. You've lived here your whole life!")

closet = Room("CLOSET",
              "In front of you is a set of CLOSET doors. There is an eerie rustling sound coming from the \
CLOSET. It seems like the CLOSET is sucking the light from the rest of the room and filling it with darkness. \
To your left is your BED. Behind you is the entrance to your BEDROOM.",
              "I can't tell what's in there! Its so dark I'd probably need 8 NIGHT_LIGHTs to be able to \
see in! If I want to figure out what's up with the closet I'm going to have to figure something out...")

bed = Room("BED",
           "You climb onto your BED. On one side of the room you see a set of CLOSET doors. On the other you \
can see the entrance to your BEDROOM.",
           "This is your bed! It has a white comforter and soft pillows. Your Teddy bear is usually here.")

south_hallway = Room("SOUTH_HALLWAY",
                     "You are at the south end of the upstairs hallway. Although not very long, you have access to \
multiple rooms. To your right you see the BATHROOM. Behind you is the MASTER_BEDROOM. To your left you see the \
entrance to your BEDROOM. You may also continue to the NORTH_HALLWAY.",
                     "This is the end of the upstairs hallway. Your room is here.")

north_hallway = Room("NORTH_HALLWAY",
                     "You are at the north end of the upstairs hallway. To your left is the STUDY. To your right a \
set of STAIRS heads downwards. Behind you is the SOUTH_HALLWAY.",
                     "Nothing special about the hallway, but you can go downstairs from here.")

bathroom = Room("BATHROOM",
                "You are in the upstairs BATHROOM. A claw foot bathtub lies empty in the corner of the room. You can \
see your reflection in the polished brass of the sink. Interestingly enough you can't see your reflection in the \
mirror. Behind you is the door to the SOUTH_HALLWAY.",
                "The bathroom is old but cozy. A dark floral pattern dominates the fixtures.")

master_bedroom = Room("MASTER_BEDROOM",
                      "You are in the MASTER_BEDROOM. A large four post bed takes up most of the space on the south \
wall. A small rug with dark letters reading 'Sparky' is tucked neatly into the corner. Behind you is the door to the \
SOUTH_HALLWAY.",
                      "This is my parents room. I must be careful not to break anything!")

study = Room("STUDY",
             "You are in your father's STUDY. A large wooden desk stands regally in the center of the room. \
Various pencils, pens and papers are strewn across the surface. Light from a dim desk lamp casts a mellow glow about \
the room. Behind you is the exit to the NORTH_HALLWAY.",
             "Your father doesn't usually let you come in here but I suppose since he isn't home...")

stairs = Room("STAIRS",
              "You are in the middle of the STAIRS. You can continue upwards to the NORTH_HALLWAY or downwards to the \
FOYER.",
              "A set of old wooden stairs. Certain steps creak when you step on them.")

foyer = Room("FOYER",
             "You are in the FOYER. It is a large open room with a set of STAIRS leading upwards. At the bottom of the \
STAIRS lies a dog crate currently vacant. Opposite to the stairs is a large set of double doors that lead OUTSIDE. \
To the left of the FOYER is the SITTING_ROOM. To the right is the SOUTH_LIVING_ROOM.",
             "The first room that someone sees when they enter the house. Maybe that's why my parents insist on \
keeping it so clean.")

outside = Room("OUTSIDE",
               "You burst out through the doors!",
               "It's dark out here!")

south_living_room = Room("SOUTH_LIVING_ROOM",
                         "You walk to the SOUTH_LIVING_ROOM. The room is decorated with various pieces of old \
furniture. In the corner a television flickers dimly. You can hear the distant babble of a news anchor. \
Extending forward you can see the NORTH_LIVING_ROOM. To your left is the FOYER.",
                         "A cozy spot where your parents usually lounge. The light from the television casts an \
errie glow about the room.")

north_living_room = Room("NORTH_LIVING_ROOM",
                         "You walk to the NORTH_LIVING_ROOM. This part of the room is mostly open with a \
large pool table dominating the area. The table sits atop a long black rug. Extending behind you is the \
SOUTH_LIVING_ROOM. In front of you and a bit to your left is a door leading to the MUD_ROOM.", "When my dad has \
free time he likes to spend it in here working on his game. I've never been very good though...")

sitting_room = Room("SITTING_ROOM",
                    "You are in a small SITTING_ROOM room containing two fancy armchairs on either side \
of a mahogany coffee table. The table appears to be empty. To your right is the entrance to the FOYER. On the other \
side of the room is a door leading to the KITCHEN.",
                    "No one really spends time in here. I'm not entirely sure why houses even have this room...")

kitchen = Room("KITCHEN",
               "You enter the KITCHEN. It is a mess of utensils, cooking appliances and leftover food. On one side \
of the room you see the entrance to the MUD_ROOM. On the other, a door leads to the SITTING_ROOM", "Usually mom \
always keeps some fresh JUICE in here - it's one of my favourite treats!")

mud_room = Room("MUD_ROOM",
                "You are in the MUD_ROOM at the back of the house. A set of BASEMENT_STAIRS heads downwards. You can \
see light coming from the KITCHEN on your left. To your right is the NORTH_LIVING_ROOM. From a perch on one \
side of the room, you see a pair of eyes staring down at you.", "This room is TANGO's favourite spot! \
He loves sitting on his perch and cleaning his feathers.")

basement_stairs = Room("BASEMENT_STAIRS",
                       "You are in the middle of the BASEMENT_STAIRS. You can continue down into the LANDING or head \
back up to the MUD_ROOM.",
                       "These stairs are made out of stone. They seem like they've been here forever...")

landing = Room("LANDING",
               "You have made it to the basement LANDING. You can just barely make out the faint outline of \
the BASEMENT_STAIRS leading upwards.", "You can't see far enough in front of you to really make out anything!")

b1 = Room("B1",
          "You made it to the KEY room! Better go BACKWARD or FORWARD and head to the exit after grabbing the KEY.",
          "You can't make out much of anything!")
b2 = Room("B2",
          "You are somewhere in the basement. The floor is very damp in this area.",
          "You can't make out much of anything!")
b3 = Room("B3",
          "You are somewhere in the basement.",
          "You can't make out much of anything!")
b4 = Room("B4",
          "You are somewhere in the basement.",
          "You can't make out much of anything!")
b5 = Room("B5",
          "You are somewhere in the basement.",
          "You can't make out much of anything!")
b6 = Room("B6",
          "You are somewhere in the basement.",
          "You can't make out much of anything!")
b7 = Room("B7",
          "You are somewhere in the basement. The floor is quite damp in this area.",
          "You can't make out much of anything!")
b8 = Room("B8",
          "You are somewhere in the basement.",
          "You can't make out much of anything!")
b9 = Room("B9",
          "You are somewhere in the basement.",
          "You can't make out much of anything!")

# Declare all the items
paper = Item("PAPER", "piece of PAPER", "There is a piece of PAPER on the ground.", "The paper reads: \n Adventure tip \
#1 - Make sure to always EXAMINE things! You never know what you may find! \n Adventure tip #2 - Don't forget you \
can always TAKE and DROP things! \n Adventure tip #3 - If you're ever lost try typing LOOK, that should \
help you get your bearings. \n Adventure tip #4 - To see what you're carrying type INVENTORY or I", 0.5)
teddy = Item("TEDDY", "TEDDY bear", "Your TEDDY bear is here.", "This is your Teddy bear Mr. Bruce P Bear! His grin \
stretches from ear to ear.", 3)
cat_food = Item("CAT_FOOD", "bag of CAT_FOOD", "A small bag of CAT_FOOD rests nearby.", "Some delicious Paws brand cat \
food... if only I had a bowl to put this in.", 3)
bowl = Item("BOWL", "metal BOWL", "A BOWL rests on the ground.", "A metal bowl with small mice printed along the rim, \
it's quite tasteful actually. Looks like something a cat would eat out of...", 2)
full_bowl = Item("FULL_BOWL", "FULL_BOWL of cat food", "A FULL_BOWL of cat food rests on the ground.", "A full bowl \
of cat food. I'm sure any cat would be my friend if I gave them some of this!", 5)
light = Item("NIGHT_LIGHT", "NIGHT_LIGHT", "A golden NIGHT_LIGHT shines in the area.", "If I collect enough of these \
I should be able to light up my closet.", 1)
journal = Item("JOURNAL", "JOURNAL", "A JOURNAL rests on the desk.", "The journal is open to an entry from \
March 13th 1981: \n Finally, a night off! Who knew it could be so tiring raising an 8 year old. I heard they were \
supposed to get better around this age... I'm worried about Joey... Every night he says he hears noises coming from \
his closet and no matter how many times I show him there's nothing there, he refuses to believe me. However, strange \
things do seem to happen around here quite frequently... maybe our house really is haunted... No that can't be true! \
Don't be silly Harold - you know better than that. Anyway, I've left him with the sitter tonight so Margaret and I \
can have a nice evening out together... I hope everything goes okay... ... ...", 3)
plaque = Item("PLAQUE", "PLAQUE", "A PLAQUE is nailed into the wall.", "Welcome to the McKenzie Estate! Established \
in 1912 to honour the late Dr. Henry H. McKenzie, this residence sits atop the doctor's final resting place and has \
been home to Dr. McKenzie's decendants for generations. The 3 story building has a massive basement and a main \
floor that loops around a wooden staircase leading up to the bedrooms. Some say if you listen closely, you can hear... \
the rest of the writing seems to have been polished off.", 1)
couch = Item("COUCH", "COUCH", "You can hear soft snoring coming from underneath a pile of blankets on the COUCH.", "O\
h, it's just my baby sitter Hayley... looks like she nodded off while watching TV.", 999)
batteries = Item("BATTERIES", "set of BATTERIES", "Some BATTERIES are piled in a corner nearby.", "AAA batteries! \
These look they have enough power in them to make small machines work.", 1)
pool_cue = Item("POOL_CUE", "POOL_CUE", "A POOL_CUE leans against the wall.", "A sturdy pool cue. Looks like this \
could do some damage if used properly.", 3)
cupboard = Item("CUPBOARD", "LOOKS LIKE YOU FOUND A GLITCH", "A CUPBOARD is nestled in the corner of the room.", "The \
cupboard appears to be empty.", 999)
juice = Item("JUICE", "ANOTHER GLITCH LOCATED", "A massive pitcher of JUICE sits atop the counter.", "Looks like it's \
mixed berry cocktail - my favourite!", 5)
soap = Item("SOAP", "bar of SOAP", "A bar of SOAP is here.", "A full bar of soap. You figure if you dropped it \
on your toe it would hurt quite a bit. Maybe if you dropped it on someone else's toe...", 2)
key = Item("KEY", "KEY", "There is a KEY on the ground", "This looks like the KEY to the child-lock on the \
door to the OUTSIDE. I wonder why my parents left it in the basement.", 3)
juice_box = Item("JUICE_BOX", "JUICE_BOX", "There is a JUICE_BOX on the ground.", "It looks like Cool-Aid! Drinking \
this should give me a bit more energy!", 2)

# Declare all Characters
sparky = Character("SPARKY",
                   "SPARKY the cat purrs quietly nearby.",
                   "Sparky is a short-haired black cat. He likes to spend his time upstairs and loves eating his \
favorite type of cat food 'Paws brand'. You should try TALKing to SPARKY.", 10, master_bedroom)
rodney = Character("RODNEY",
                   "RODNEY the Roomba rolls slowly across the floor.",
                   "RODNEY is an S series Roomba equipped with 3 separate vacuums and an advanced collision \
detection system. Looks like he runs on AAA batteries. RODNEY also responds to voice commands - You should try \
TALKing to him.", 4, south_living_room)
tango = Character("TANGO",
                  "TANGO stares down at your curiously.",
                  "TANGO is a medium-sized green parrot. Since he's always sitting at the top of the BASEMENT_STAIRS \
he knows a lot about what goes on in the basement (or so he says).", 6, mud_room)
spud = Character("SPUD",
                 "You can hear SPUD panting nearby.",
                 "SPUD is a black and white border collie with one eye blue and one eye brown. He loves \
playing with Joey and is fiercely loyal.", 14, foyer)

# Enemies
small_rat = Character("SMALL_RAT", "A SMALL_RAT leaps from the darkness and shows its teeth.", "It looks \
angry.", 4, b3)
large_rat = Character("LARGE_RAT", "A LARGE_RAT appears and bears its fangs.", "It looks very angry.", 9, b9)
possessed_box = Character("BOX", "A possessed BOX of clothes charges from out of nowhere.", "How does it even move? \
It doesn't have any legs.", 10, b5)
gnome = Character("GNOME", "An evil garden GNOME rushes from the shadows and brandishes its pitchfork.",
                  "Although angry, he looks quite small and weak.", 4, b7)

# Declare inventory
inventory = Inventory()

# Declare special flags
can_leave_bedroom = False  # Set to False for full play-through
sparky_light_flag = True  # S
# et to True for full play-through
final_boss = False  # Set to False for full play-through
after_final_boss = False
no_key = True  # Set to True for full play-through
has_batteries = False
found_lights = False
gotten_light_from_spud = False
talked_to_tango = False
legal = ["FORWARD", "BACKWARD", "LEFT", "RIGHT"]


def initialize_rooms():
    # bedroom_entrance
    bedroom_entrance.next_location.append(("CLOSET", closet))
    bedroom_entrance.next_location.append(("BED", bed))
    bedroom_entrance.next_location.append(("SOUTH_HALLWAY", south_hallway))

    # closet
    closet.next_location.append(("BED", bed))
    closet.next_location.append(("BEDROOM", bedroom_entrance))
    closet.items.append(paper)

    # bed
    bed.next_location.append(("CLOSET", closet))
    bed.next_location.append(("BEDROOM", bedroom_entrance))
    bed.items.append(teddy)

    # south_hallway
    south_hallway.next_location.append(("BEDROOM", bedroom_entrance))
    south_hallway.next_location.append(("NORTH_HALLWAY", north_hallway))
    south_hallway.next_location.append(("BATHROOM", bathroom))
    south_hallway.next_location.append(("MASTER_BEDROOM", master_bedroom))

    # master_bedroom
    master_bedroom.next_location.append(("SOUTH_HALLWAY", south_hallway))
    master_bedroom.items.append(light)
    master_bedroom.characters.append(sparky)

    # bathroom
    bathroom.next_location.append(("SOUTH_HALLWAY", south_hallway))
    bathroom.items.append(soap)
    bathroom.items.append(light)

    # north_hallway
    north_hallway.next_location.append(("SOUTH_HALLWAY", south_hallway))
    north_hallway.next_location.append(("STUDY", study))
    north_hallway.next_location.append(("STAIRS", stairs))
    north_hallway.items.append(cat_food)

    # study
    study.next_location.append(("NORTH_HALLWAY", north_hallway))
    study.items.append(journal)
    study.items.append(bowl)

    # stairs
    stairs.next_location.append(("NORTH_HALLWAY", north_hallway))
    stairs.next_location.append(("FOYER", foyer))

    # foyer
    foyer.next_location.append(("STAIRS", stairs))
    foyer.items.append(plaque)
    foyer.next_location.append(("OUTSIDE", outside))
    foyer.next_location.append(("SOUTH_LIVING_ROOM", south_living_room))
    foyer.next_location.append(("SITTING_ROOM", sitting_room))
    foyer.characters.append(spud)

    # sitting_room
    sitting_room.next_location.append(("FOYER", foyer))
    sitting_room.next_location.append(("KITCHEN", kitchen))
    sitting_room.items.append(cupboard)

    # south_living_room
    south_living_room.next_location.append(("FOYER", foyer))
    south_living_room.next_location.append(("NORTH_LIVING_ROOM", north_living_room))
    south_living_room.items.append(couch)
    south_living_room.characters.append(rodney)

    # north_living_room
    north_living_room.next_location.append(("SOUTH_LIVING_ROOM", south_living_room))
    north_living_room.next_location.append(("MUD_ROOM", mud_room))
    north_living_room.items.append(pool_cue)

    # kitchen
    kitchen.next_location.append(("MUD_ROOM", mud_room))
    kitchen.next_location.append(("SITTING_ROOM", sitting_room))
    kitchen.items.append(juice)

    # mud_room
    mud_room.next_location.append(("NORTH_LIVING_ROOM", north_living_room))
    mud_room.next_location.append(("KITCHEN", kitchen))
    mud_room.next_location.append(("BASEMENT_STAIRS", basement_stairs))
    mud_room.characters.append(tango)

    # basement stairs
    basement_stairs.next_location.append(("MUD_ROOM", mud_room))
    basement_stairs.next_location.append(("LANDING", landing))

    # landing
    landing.next_location.append(("BASEMENT_STAIRS", basement_stairs))
    landing.next_location.append(("FORWARD", b4))
    landing.next_location.append(("BACKWARD", b9))
    landing.next_location.append(("LEFT", b6))
    landing.next_location.append(("RIGHT", b5))

    # b1
    b1.next_location.append(("BACKWARD", b2))
    b1.next_location.append(("FORWARD", b7))
    b1.items.append(key)

    # b2
    b2.next_location.append(("FORWARD", b1))
    b2.next_location.append(("BACKWARD", b5))
    b2.next_location.append(("LEFT", b4))
    b2.next_location.append(("RIGHT", b3))

    # b3
    b3.next_location.append(("FORWARD", b8))
    b3.next_location.append(("BACKWARD", b6))
    b3.next_location.append(("LEFT", b2))
    b3.next_location.append(("RIGHT", b4))
    b3.characters.append(small_rat)

    # b4
    b4.next_location.append(("FORWARD", b9))
    b4.next_location.append(("BACKWARD", landing))
    b4.next_location.append(("LEFT", b3))
    b4.next_location.append(("RIGHT", b2))
    b4.items.append(juice_box)

    # b5
    b5.next_location.append(("FORWARD", b2))
    b5.next_location.append(("BACKWARD", b7))
    b5.next_location.append(("LEFT", landing))
    b5.next_location.append(("RIGHT", b6))
    b5.characters.append(possessed_box)

    # b6
    b6.next_location.append(("FORWARD", b3))
    b6.next_location.append(("BACKWARD", b8))
    b6.next_location.append(("LEFT", b5))
    b6.next_location.append(("RIGHT", landing))

    # b7
    b7.next_location.append(("FORWARD", b5))
    b7.next_location.append(("BACKWARD", b1))
    b7.next_location.append(("LEFT", b9))
    b7.next_location.append(("RIGHT", b8))
    b7.characters.append(gnome)

    # b8
    b8.next_location.append(("FORWARD", b6))
    b8.next_location.append(("BACKWARD", b3))
    b8.next_location.append(("LEFT", b7))
    b8.next_location.append(("RIGHT", b9))
    b8.items.append(light)

    # b9
    b9.next_location.append(("FORWARD", landing))
    b9.next_location.append(("BACKWARD", b4))
    b9.next_location.append(("LEFT", b8))
    b9.next_location.append(("RIGHT", b7))
    b9.characters.append(large_rat)


def parse(input_text):
    return input_text.upper().strip().split()


if __name__ == "__main__":
    # Initialization functions
    initialize_rooms()
    seed(15)

    # Beginning Text
    print(" 'Joey...' \n 'Joey...' \n 'Joey...' \n 'I'm coming for you Joey. You can't run from me Joey. \
For years I've been watching you and now I will consume you Joey. I've been chained here for too \
long... I'm getting stronger as the LIGHT fades! You can't escape! Joey... Joey... JOEY!'\
\n Your eyes snap open! You can feel your heart racing. Your sheets are drenched with sweat and your PJs are soaked. \
\n 'That was scary' you think to yourself. \n 'Good thing it was only a dream... I think'. \n You sit up in your bed \
and look over at your closet. You've always thought there was something unnatural about great-grandpa McKenzie's \
wardrobe. The sounds you can hear at night. Its icy black exterior. The way it seems to suck all the light out of \
the room. \n 'You know what, I've had enough - that's it!' you exclaim. \n 'No more wondering! Today will \
be the day I finally figure out what's up with that CLOSET! I better GO over there and EXAMINE it.' \
\n Pausing for a moment, you take a deep breath, steady yourself and get out of bed... \n \n")

    # Print the first room
    current_room = bedroom_entrance  # change to bedroom_entrance for full play-through
    # light.amount = 8
    # inventory.items.append(light)
    # inventory.items.append(key)
    print(bedroom_entrance)

    # Game loop controlled by boolean flag
    closed_flag = False
    while not closed_flag:

        # ------------------------------------------------ INPUT ------------------------------------------------------
        value = input("> ")
        parsed = parse(value)

        # ------------------------------------------------ UPDATE -----------------------------------------------------
        action_flag = ""
        move = True

        if len(parsed) == 0:
            action_flag = "type_something"
        if len(parsed) != 2:
            move = False

        # UPDATE CHARACTER LOCATIONS
        value = randint(0, 10)
        value2 = randint(0, 2)

        # Characters only have the chance to move 1/3 of the turns
        if value2 == 1:
            # Sparky (SH, MB, B) - only moves when you're not in his room
            if sparky.location != current_room:
                sparky.location.characters.remove(sparky)
                if value < 2:
                    sparky.location = south_hallway
                    south_hallway.characters.append(sparky)
                elif 2 <= value < 7:
                    sparky.location = master_bedroom
                    master_bedroom.characters.append(sparky)
                else:
                    sparky.location = bathroom
                    bathroom.characters.append(sparky)
            # Rodney (SLR, NLR) - only moves if you're not in his room
            if rodney.location != current_room:
                rodney.location.characters.remove(rodney)
                if value < 5:
                    rodney.location = south_living_room
                    south_living_room.characters.append(rodney)
                else:
                    rodney.location = north_living_room
                    north_living_room.characters.append(rodney)
            # Spud (F, SR, K, MR)
            if spud.location != current_room:
                spud.location.characters.remove(spud)
                if value <= 2:
                    spud.location = foyer
                    foyer.characters.append(spud)
                elif 3 <= value <= 5:
                    spud.location = sitting_room
                    sitting_room.characters.append(spud)
                elif 6 <= value <= 8:
                    spud.location = kitchen
                    kitchen.characters.append(spud)
                else:
                    spud.location = mud_room
                    mud_room.characters.append(spud)
            # small_rat (b2, b3, b4)
            if small_rat.location != current_room and small_rat.health > 0 and parsed[0] == "GO" and move and\
                    parsed[1] in legal:
                small_rat.location.characters.remove(small_rat)
                if value <= 2:
                    small_rat.location = b2
                    b2.characters.append(small_rat)
                elif 3 <= value <= 5:
                    small_rat.location = b4
                    b4.characters.append(small_rat)
                else:
                    small_rat.location = b3
                    b3.characters.append(small_rat)
            # large_rat (b8, b9)
            if large_rat.location != current_room and large_rat.health > 0 and parsed[0] == "GO" and move and\
                    parsed[1] in legal:
                large_rat.location.characters.remove(large_rat)
                if value <= 2:
                    large_rat.location = b8
                    b8.characters.append(large_rat)
                else:
                    large_rat.location = b9
                    b9.characters.append(large_rat)
            # gnome (b7, b6)
            if gnome.location != current_room and gnome.health > 0 and parsed[0] == "GO" and move and\
                    parsed[1] in legal:
                gnome.location.characters.remove(gnome)
                if value <= 5:
                    gnome.location = b7
                    b7.characters.append(gnome)
                else:
                    gnome.location = b6
                    b6.characters.append(gnome)

        if action_flag != "type_something":
            if len(parsed) > 2:
                action_flag = "2_word_error"

            elif parsed[0] == "INVENTORY" or parsed[0] == 'I':
                action_flag = "inv"

            elif parsed[0] == "EXAMINE":
                if len(parsed) == 1:
                    action_flag = "what_examine"
                elif parsed[1] == "INVENTORY":
                    action_flag = "inv"
                elif parsed[1] == current_room.name or parsed[1] == "ROOM":
                    # Special case for if you have all NIGHT_LIGHTs and you examine closet
                    if parsed[1] == "CLOSET":
                        # Check to see if you've gotten all NIGHT_LIGHTS
                        for item in inventory.items:
                            if item.name == "NIGHT_LIGHT" and item.amount >= 8:
                                final_boss = True
                        if after_final_boss:
                            print("I better get out of here.")
                            action_flag = "final_boss"
                        elif final_boss:
                            print("You carefully take out all of your collected NIGHT_LIGHTS and place them around the \
CLOSET. \n 'It's finally time' you think to yourself. Your body tenses up. A cold shiver runs through you from \
your head to your toes. You slowly approach the CLOSET doors and swing them open. The inside of the CLOSET is \
illuminated by the NIGHT_LIGHTs! You real back in terror as you see... ... ...")
                            print("Absolutely nothing.")
                            print("'That's weird' you think, 'I thought for sure something would have been in here. \
Maybe I am going cra...' *GRAAAAAAHHH*")
                            print("Suddenly, with a piercing cry, your TEDDY bear falls from your pocket and \
begins to expand. \n 'You've fallen into my trap Joey! Using the power from these NIGHT_LIGHTs I now have the \
strength to transform into my final form!' \n The TEDDY bear is now so big it almost fills the room. With a \
frightening roar, he charges. Panicking, you think to yourself, 'I need to get OUTSIDE before the monster TEDDY \
consumes me!' ")
                            inventory.items.remove(teddy)
                            after_final_boss = True
                            action_flag = "final_boss"
                        else:
                            action_flag = "current_room_examine"
                    else:
                        action_flag = "current_room_examine"
                elif len(parsed) > 1:
                    for room in current_room.next_location:
                        if parsed[1] == room[0]:
                            action_flag = room[0]
                    for item in inventory.items:
                        if parsed[1] == item.name:
                            action_flag = item.name
                    for item in current_room.items:
                        if parsed[1] == "CUPBOARD" and not found_lights:
                            print("You look around in the cupboard and find a NIGHT_LIGHT and some BATTERIES! \
What a score! You put both items into your INVENTORY.")
                            if light not in inventory.items:
                                inventory.items.append(light)
                            else:
                                for itemX in inventory.items:
                                    if itemX == light:
                                        itemX.amount = itemX.amount + 1
                            inventory.items.append(batteries)
                            found_lights = True
                            action_flag = "examine"
                        elif parsed[1] == item.name:
                            action_flag = item.name
                    for character in current_room.characters:
                        if parsed[1] == character.name:
                            action_flag = character.name
                else:
                    action_flag = "idk_examine"

            elif parsed[0] == "TALK":
                if len(parsed) == 1:
                    action_flag = "talk_to_whom"
                else:
                    for character in current_room.characters:
                        if parsed[1] == character.name:
                            # Talking to Sparky
                            if parsed[1] == "SPARKY":
                                if sparky_light_flag:
                                    print("SPARKY: *meow* Hey Joey, what are you doing up so late? Normally you're \
asleep by 9 o'clock. Do you wanna ASK me something?")
                                else:
                                    print("SPARKY: *meow* Thanks for the kibbles! *much* *munch* These are purrrrfect.")
                                action_flag = "talk"
                            # Talking to Rodney
                            elif parsed[1] == "RODNEY":
                                if not has_batteries:
                                    print("RODNEY: *wrrrrrr* *beep* ... need. more. power. ... *beep* ... can't. keep. \
going. ... *beep beep*")
                                else:
                                    print("RODNEY: Thank. You. For. Fixing. Me. Rodney. Can. Clean. Many. Things. Now.")
                                action_flag = "talk"
                            # Talking to Tango
                            elif parsed[1] == "TANGO":
                                print("TANGO: *squawk* Hi Joey! Have you heard about the basement? *squawk* \
Your parents are always talking about some KEY that's down there. Not sure what it's for though... *squawk* \
Anyway, if you do go down there it's not like up here! It's too dark to make out any rooms (not even the NIGHT_LIGHTs \
can help down there) so you'll be navigating with a reduced set of commands. Once you enter you'll only be able to \
use GO FORWARD, GO BACKWARD, GO LEFT and GO RIGHT for movement. *squawk* Hopefully you don't get lost! *squawk* Also, \
try ASKing me about the scary things that lurk in the basement. *squawk*")
                                talked_to_tango = True
                                action_flag = "talk"
                            # Talking to Spud
                            elif parsed[1] == "SPUD":
                                print("SPUD: *bark bark* Hey Joey, how's a going! What are you up to? Wanna play? \
What are you doing? Where you going? Got any snacks? *Spud seems to get distracted by his tail and starts chasing it.*")
                                action_flag = "talk"
                            # Talking to enemy
                            elif parsed[1] == "SMALL_RAT" or parsed[1] == "LARGE_RAT" or parsed[1] == "BOX" or \
                                    parsed[1] == "GNOME":
                                print("It doesn't look like it can be reasoned with!")
                                action_flag = "talk"
                    if action_flag == "":
                        if parsed[1] == "SPARKY":
                            action_flag = "sparky_not_here"
                        elif parsed[1] == "SPUD":
                            action_flag = "spud_not_here"
                        elif parsed[1] == "RODNEY":
                            action_flag = "rodney_not_here"
                        elif parsed[1] == "TANGO":
                            action_flag = "tango_not_here"
                        else:
                            action_flag = "idk_talk"

            elif parsed[0] == "ASK":
                if len(parsed) == 1:
                    action_flag = "ask_who"
                else:
                    for character in current_room.characters:
                        if parsed[1] == character.name:
                            # Asking Sparky
                            if parsed[1] == "SPARKY":
                                if sparky_light_flag:
                                    print("SPARKY: *meow* Oh, you wanna know if I have a NIGHT_LIGHT? I think I \
remember seeing one around here somewhere. *rumble* Although, I'm too hungry to right now to remember exactly \
where... maybe if I had some cat food... Do you think you could GIVE me some?")
                                else:
                                    print("SPARKY: That cat food was delicious thank you! *burp*")
                                action_flag = "talk"
                            # Asking Rodney
                            elif parsed[1] == "RODNEY":
                                if not has_batteries:
                                    print("RODNEY: *bzzzzzz* *beep* ... cant. answer. ... *beep* ... almost. dead. \
... *beep boop*")
                                else:
                                    print("RODNEY: I. Am. Doing. 100. Out. Of. 100. Now. Thank. You. For. Asking. I. \
Noticed. A. NIGHT_LIGHT. Under. The. Couch. In. The. SOUTH_LIVING_ROOM. Maybe. You. Can. Use. It. For. Something.")
                                action_flag = "talk"
                            # Asking Tango
                            elif parsed[1] == "TANGO":
                                print("TANGO: *chirp* I haven't seen them myself but apparently there are scary \
monsters in the basement you will have to ATTACK and defeat! Be careful though, if your HEALTH gets to 0... \
*nervous squawk* Well let's just say you probably don't want that to happen, ok? *squawk* I would recommend \
taking some sort of weapon down there with you but that's just me... *squawk chirp chirp*")
                                action_flag = "talk"
                            # Asking Spud
                            elif parsed[1] == "SPUD":
                                if not gotten_light_from_spud:
                                    print("SPUD: Oh! *woof* You're looking for a NIGHT_LIGHT??? Why didn't you say \
so, I have one right here! I'll put it in your INVENTORY for you! *woof woof*")
                                    if light not in inventory.items:
                                        inventory.items.append(light)
                                    else:
                                        for itemX in inventory.items:
                                            if itemX == light:
                                                itemX.amount = itemX.amount + 1
                                    gotten_light_from_spud = True
                                else:
                                    print("SPUD: *bark* That bird TANGO from the MUD_ROOM told me that long pointy \
items are especially useful at ridding the basement of evil critters. Not sure where you would find one around \
here though... *licks paws thoughtfully*")
                                action_flag = "talk"
                            # Asking enemy
                            elif parsed[1] == "SMALL_RAT" or parsed[1] == "LARGE_RAT" or parsed[1] == "BOX" or \
                                    parsed[1] == "GNOME":
                                print("It doesn't seem to respond to your question.")
                                action_flag = "talk"
                    if action_flag == "":
                        if parsed[1] == "SPARKY":
                            action_flag = "sparky_not_here"
                        elif parsed[1] == "SPUD":
                            action_flag = "spud_not_here"
                        elif parsed[1] == "RODNEY":
                            action_flag = "rodney_not_here"
                        elif parsed[1] == "TANGO":
                            action_flag = "tango_not_here"
                        else:
                            action_flag = "idk_ask"
            elif parsed[0] == "GIVE":
                if len(parsed) == 1:
                    action_flag = "give_who"
                else:
                    for character in current_room.characters:
                        if parsed[1] == character.name:
                            # Giving to to Sparky
                            if parsed[1] == "SPARKY":
                                if sparky_light_flag and full_bowl in inventory.items:
                                    print("SPARKY: OMG thank you so much! This is my favourite! Here, I dropped a \
NIGHT_LIGHT on the floor over there for you!")
                                    current_room.items.append(light)
                                    sparky_light_flag = False
                                    inventory.items.remove(full_bowl)
                                else:
                                    print("You don't have anything to give to Sparky.")
                                action_flag = "give"
                            # Giving to Rodney
                            elif parsed[1] == "RODNEY":
                                if batteries in inventory.items and not has_batteries:
                                    print("*you insert the batteries into Rodney's battery chamber*\nRODNEY: Powering. \
Up. Please. Hold. ... ... ... ...")
                                    time.sleep(3)
                                    print("1.")
                                    time.sleep(2)
                                    print("2.")
                                    time.sleep(2)
                                    print("3.")
                                    time.sleep(2)
                                    print("... ... ...")
                                    time.sleep(2)
                                    print("RODNEY: Thank. You. For. The. Energy. Good. Human. ... ... What's. That. \
You're. Looking. For. A. NIGHT_LIGHT. ... ... I. Think. I. Saw. One. In. The. FOYER. While. I. Was. \
Cleaning. You. Should. Go. Double. Check. *beep boop beep*")
                                    has_batteries = True
                                    inventory.items.remove(batteries)
                                    foyer.items.append(light)
                                    action_flag = "give"
                                else:
                                    print("You have nothing to give to Rodney!")
                                    action_flag = "give"
                            # Giving to Tango
                            elif parsed[1] == "TANGO":
                                print("Tango doesn't need anything - he seems quite content as is!")
                                action_flag = "give"
                            # Giving to Spud
                            elif parsed[1] == "SPUD":
                                print("Spud already has everything he needs!")
                                action_flag = "give"
                            elif parsed[1] == "SMALL_RAT" or parsed[1] == "LARGE_RAT" or parsed[1] == "BOX" or \
                                    parsed[1] == "GNOME":
                                print("It's too angry to accept any gifts right now!")
                                action_flag = "talk"
                    if action_flag == "":
                        if parsed[1] == "SPARKY":
                            action_flag = "sparky_not_here_give"
                        elif parsed[1] == "SPUD":
                            action_flag = "spud_not_here_give"
                        elif parsed[1] == "RODNEY":
                            action_flag = "rodney_not_here_give"
                        elif parsed[1] == "TANGO":
                            action_flag = "tango_not_here_give"
                        else:
                            action_flag = "idk_give"

            elif parsed[0] == "LOOK":
                action_flag = "move"

            elif parsed[0] == "GO":
                if len(parsed) == 1:
                    action_flag = "go_where"
                else:
                    # Check for enemies in the room
                    for character in current_room.characters:
                        if character.name == "LARGE_RAT":
                            print("The LARGE_RAT stands menacingly in your way - looks like you're going to have to \
defeat him if you want to leave!")
                            action_flag = "no_escape"
                        elif character.name == "SMALL_RAT":
                            print("The SMALL_RAT jumps in front of you preventing your escape!")
                            action_flag = "no_escape"
                        elif character.name == "BOX":
                            print("The BOX's evil stare has you in a trance - you are unable to leave!")
                            action_flag = "no_escape"
                        elif character.name == "GNOME":
                            print("The GNOME quickly scurries in front of you and blocks your path!")
                            action_flag = "no_escape"
                    # Special condition: No running from a fight!
                    if action_flag == "no_escape":
                        action_flag = "no_escape"
                    # Special condition: Only allowed out of bedroom with Teddy
                    elif current_room.name == "BEDROOM" and parsed[1] == "SOUTH_HALLWAY":
                        if teddy in inventory.items:
                            can_leave_bedroom = True
                        if can_leave_bedroom:
                            current_room = south_hallway
                            action_flag = "move"
                        else:
                            action_flag = "need_teddy"
                    # Special condition: Only allowed downstairs if given Sparky food
                    elif current_room.name == "NORTH_HALLWAY" and parsed[1] == "STAIRS" and sparky_light_flag:
                        action_flag = "need_to_feed"
                    # special condition: Extra text when going down stairs after boss
                    elif current_room.name == "NORTH_HALLWAY" and parsed[1] == "STAIRS" and after_final_boss:
                        print("~~~ I'm coming for you Joey, you better run! ~~~")
                        for location_pair in current_room.next_location:
                            if parsed[1] == location_pair[0]:
                                current_room = location_pair[1]
                                action_flag = "move"
                    # Special condition: Only allowed outside with key
                    elif current_room.name == "FOYER" and parsed[1] == "OUTSIDE" and no_key:
                        action_flag = "need_key"
                    # Special condition: Can't go outside even after key
                    elif current_room.name == "FOYER" and parsed[1] == "OUTSIDE" and not after_final_boss:
                        action_flag = "get_back_here"
                    # Special condition: Can only go basement if already talked to Tango
                    elif current_room.name == "FOYER" and parsed[1] == "OUTSIDE" and after_final_boss:
                        print("You quickly unlock the door and burst out into the night! As you run out onto the lawn \
you see the monster TEDDY come rushing out behind you. You keep running but the TEDDY is gaining on you!")
                        time.sleep(7)
                        print("You pump your arms and legs as fast as you can but its no use! The TEDDY is almost upon \
you!")
                        time.sleep(4)
                        print("With a final gasp of breath you turn and face the TEDDY...")
                        time.sleep(4)
                        print("All of a sudden you hear a loud bark and a blur of white and black comes streaking \
across the lawn, ramming into the TEDDY. 'SPUD!' you cry, as your faithful dog jumps onto the TEDDY. Quickly, SPUD \
rips the TEDDY's head off with his teeth and as he does, the bear begins to shrink back to its normal size. \
A trail of green mist seeps into the air and disappears into the night sky. All that's left is the head and lifeless \
body of a teddy bear. As you lean down to give SPUD a hug, you hear a shout from the FOYER, \n 'What's going on out \
there? SPUD, Joey get back in here!' \n You look up and see your sitter standing in the FOYER. You quickly run with \
SPUD back into the house. The entire building seems a little more friendly as you walk back up the stairs \
and head for your room. \n 'I think that's enough adventure for one night,' you think to yourself as you \
climb into bed and snuggle up closely to SPUD who has followed you up. Finally, safe at last. \n")
                        print("*** *** *** ***")
                        print("Thanks for playing!")
                        print("You died " + str(inventory.deaths) + " time(s)!")
                        if inventory.deaths == 0:
                            print("That's a perfect score! Congratulations!")
                        print("*** *** *** ***")
                        exit(0)
                    elif current_room.name == "MUD_ROOM" and parsed[1] == "BASEMENT_STAIRS" and not talked_to_tango:
                        action_flag = "better_go_talk_to_tango"
                    # You're already in that room!
                    elif parsed[1] == current_room.name:
                        action_flag = "already_here"
                    # Normal move condition
                    else:
                        for location_pair in current_room.next_location:
                            if parsed[1] == location_pair[0]:
                                current_room = location_pair[1]
                                action_flag = "move"

                    if action_flag == "":
                        action_flag = "idk_go"

            elif parsed[0] == "TAKE":
                if len(parsed) == 1:
                    action_flag = "what_take"
                else:
                    # special condition for taking cat food (need bowl)
                    if cat_food in current_room.items and parsed[1] == "CAT_FOOD":
                        if bowl in inventory.items:
                            inventory.items.append(full_bowl)
                            current_room.items.remove(cat_food)
                            inventory.items.remove(bowl)
                            print("You took the cat food and poured it into the bowl.")
                            action_flag = "take"
                        else:
                            action_flag = "need_bowl"
                    # special condition for taking key
                    elif key in current_room.items and parsed[1] == "KEY":
                        no_key = False
                        current_room.items.remove(key)
                        inventory.items.append(key)
                        print("You took the " + key.inven_name + ".")
                        action_flag = "take"
                    # special condition for taking lights
                    elif light in current_room.items and parsed[1] == "NIGHT_LIGHT":
                        if light not in inventory.items:
                            current_room.items.remove(light)
                            inventory.items.append(light)
                            print("You took the " + light.inven_name + ".")
                            action_flag = "take"
                        else:
                            for item in inventory.items:
                                if item == light:
                                    item.amount = item.amount + 1
                                    current_room.items.remove(light)
                                    print("You took the " + light.inven_name + ".")
                                    action_flag = "take"
                    # special condition for trying to take journal
                    elif journal in current_room.items and parsed[1] == "JOURNAL":
                        print("Daddy told me never to touch his journal but I suppose I could EXAMINE it...")
                        action_flag = "take"
                    # special condition for taking the couch (you can't lol)
                    elif couch in current_room.items and parsed[1] == "COUCH":
                        print("I can't take that its too heavy!")
                        action_flag = "take"
                    # special condition for taking juice_box
                    elif juice_box in current_room.items and parsed[1] == "JUICE_BOX":
                        print("You grab the juice box and suck it till it's dry. You feel quite refreshed! \
(+ 4 to HEALTH)")
                        inventory.health = inventory.health + 4
                        current_room.items.remove(juice_box)
                        action_flag = "take"
                    # special condition for trying to take plaque
                    elif plaque in current_room.items and parsed[1] == "PLAQUE":
                        print("You can't take this it's nailed to the wall! I could EXAMINE it though...")
                        action_flag = "take"
                    # special condition for trying to take cupboard
                    elif cupboard in current_room.items and parsed[1] == "CUPBOARD":
                        print("You try to move the cupboard but it won't budge! I may be able to EXAMINE what's inside \
though.")
                        action_flag = "take"
                    # Special condition for taking juice
                    elif juice in current_room.items and parsed[1] == "JUICE":
                        print("You carefully pour a bit of juice out into a cup and drink it in one gulp. \
You instantly feel refreshed and ready to go!")
                        action_flag = "take"
                        if inventory.health < 10:
                            inventory.health = 10
                    # Normal take condition
                    else:
                        for item in current_room.items:
                            if parsed[1] == item.name:
                                current_room.items.remove(item)
                                inventory.items.append(item)
                                print("You took the " + item.inven_name + ".")
                                action_flag = "take"
                    if action_flag == "":
                        action_flag = "idk_take"

            elif parsed[0] == "DROP":
                if len(parsed) == 1:
                    action_flag = "what_drop"
                else:
                    # special condition for trying to drop teddy
                    if parsed[1] == "TEDDY" and teddy in inventory.items:
                        print("You can't drop Mr. Bear! It'll be too scary without him!")
                        action_flag = "drop"
                    # special condition for trying to drop key
                    elif parsed[1] == "KEY" and key in inventory.items:
                        print("I probably shouldn't drop this - wouldn't want to lose it.")
                        action_flag = "drop"
                    # special condition for trying to drop night_light
                    elif parsed[1] == "NIGHT_LIGHT":
                        for item in inventory.items:
                            if item == light:
                                if item.amount == 1:
                                    inventory.items.remove(item)
                                    current_room.items.append(item)
                                    print("You dropped the " + item.inven_name + ".")
                                    action_flag = "drop"
                                else:
                                    item.amount = item.amount - 1
                                    current_room.items.append(item)
                                    print("You dropped the " + item.inven_name + ".")
                                    action_flag = "drop"
                    else:
                        for item in inventory.items:
                            if parsed[1] == item.name:
                                inventory.items.remove(item)
                                current_room.items.append(item)
                                print("You dropped the " + item.inven_name + ".")
                                action_flag = "drop"
                    if action_flag == "":
                        action_flag = "idk_drop"

            elif parsed[0] == "ATTACK":
                if len(parsed) == 1:
                    action_flag = "what_attack"
                else:
                    for enemy in current_room.characters:
                        if enemy.name == parsed[1] and (enemy.name == "LARGE_RAT" or enemy.name == "SMALL_RAT" or
                                                        enemy.name == "BOX" or enemy.name == "GNOME"):
                            # Take a battle turn
                            joey_hit = randint(0, 7)
                            enemy_hit = randint(0, 2)
                            if joey_hit < 7:
                                if pool_cue in inventory.items:
                                    print("You use your POOL_CUE to stab the " + enemy.name + " for 3 damage!")
                                    enemy.health = enemy.health - 3
                                elif soap in inventory.items:
                                    print("You whack the " + enemy.name + " with your bar of SOAP for 2 damage!")
                                    enemy.health = enemy.health - 2
                                else:
                                    print("You hit the " + enemy.name + " with your bare hands. It does 1 damage.")
                                    enemy.health = enemy.health - 1
                            else:
                                print("Your attacked missed!")
                            if enemy.health <= 0:
                                print("You defeated the " + enemy.name + "!")
                                current_room.characters.remove(enemy)
                                if enemy.name == "BOX":
                                    print("Looks like the BOX dropped something when it died!")
                                    current_room.items.append(light)
                                print("***")
                                print(current_room)
                                for item in current_room.items:
                                    print(item)
                            else:
                                time.sleep(1)
                                if enemy_hit < 2:
                                    if enemy.name == "BOX" or enemy.name == "LARGE_RAT":
                                        print("The " + enemy.name + " retaliates and hits you for 2 damage!")
                                        inventory.health = inventory.health - 2
                                    else:
                                        print("The " + enemy.name + " strikes back and hits you for 1 damage!")
                                        inventory.health = inventory.health - 1
                                else:
                                    print("The " + enemy.name + " tried to attack you but missed!")
                                if inventory.health <= 0:
                                    if enemy.name == "BOX":
                                        enemy.health = 8
                                    elif enemy.name == "LARGE_RAT":
                                        enemy.health = 7
                                    else:
                                        enemy.health = 4
                                    print("Oh no! Your health has reached 0! You lose consciousness!")
                                    time.sleep(4)
                                    print("...")
                                    time.sleep(2)
                                    print("...")
                                    time.sleep(2)
                                    print("You feel your body slowly start to float, you're not sure where you are...")
                                    time.sleep(4)
                                    print("You hear a voice calling... *squawk* Joey we need you!... You slowly \
open your eyes...")
                                    time.sleep(4)
                                    inventory.health = 2
                                    inventory.deaths = inventory.deaths + 1
                                    current_room = mud_room
                                    print("\n")
                                    print(current_room)
                                    print("TANGO: *squawk* Joey! You should drink something to restore your health!")
                            action_flag = "attack"
                        elif enemy.name == parsed[1] and (enemy.name == "SPUD" or enemy.name == "RODNEY" or
                                                          enemy.name == "TANGO" or enemy.name == "SPARKY"):
                            print("I can't attack " + enemy.name + "! He's my friend!")
                            action_flag = "attack"
                    if action_flag == "":
                        action_flag = "idk_attack"

            elif parsed[0] == "HELP":
                action_flag = "help"

            elif parsed[0] == "HEALTH":
                action_flag = "health"

        # ------------------------------------------------- RENDER ----------------------------------------------------
        if action_flag == "2_word_error":
            print("I'm sorry I don't understand! (commands must only be 1 or 2 words long)")
        elif action_flag == "type_something":
            print("(Try typing something!)")
        elif action_flag == "move":
            print(current_room)
            for item in current_room.items:
                print(item)
            for character in current_room.characters:
                print(character)
        # NEED NEED NEED NEED
        elif action_flag == "need_teddy":
            print("It's too scary to go out into the dark hallway alone... I need my TEDDY bear!")
        elif action_flag == "need_bowl":
            print("You need something to put the CAT_FOOD in!")
        elif action_flag == "need_to_feed":
            print("As you try to walk down the stairs, you can hear SPARKY the cat let out a high pitched meow. \
Maybe you should see what he wants before heading downstairs...")
        elif action_flag == "need_key":
            print("Looks like the childproof lock is on, if I want to go outside I'm going to need the KEY.")
        elif action_flag == "get_back_here":
            print("You hear a voice yell from the SOUTH_LIVING_ROOM, 'Hey who's there!?!' \n I \
guess I better stay inside, don't want to scare my sitter...")
        elif action_flag == "better_go_talk_to_tango":
            print("TANGO: *squawk* Before you go down there Joey I have something to tell you! *squawk* Come TALK to \
me!")
        # INVENTORY INVENTORY INVENTORY INVENTORY
        elif action_flag == "inv":
            print(inventory)
        # EXAMINE EXAMINE EXAMINE EXAMINE
        elif action_flag == "what_examine":
            print("What do you want me to examine?")
        elif action_flag == "current_room_examine":
            print(current_room.examine)
        elif action_flag == "idk_examine":
            print("I'm not sure what you want me to examine!")
        elif action_flag == "examine":
            pass
        # TAKE TAKE TAKE TAKE
        elif action_flag == "what_take":
            print("What do you want me to take?")
        elif action_flag == "idk_take":
            print("I can't take that!")
        elif action_flag == "take":
            pass
        # DROP DROP DROP DROP
        elif action_flag == "what_drop":
            print("What do you want me to drop?")
        elif action_flag == "idk_drop":
            print("I'm not sure what you want me to drop!")
        elif action_flag == "drop":
            pass
        # GO GO GO GO
        elif action_flag == "go_where":
            print("Where do you want to go?")
            for room in current_room.next_location:
                print(room[0])
        elif action_flag == "idk_go":
            print("I'm not sure where that is!")
            print("Where do you want to go?")
            for room in current_room.next_location:
                print(room[0])
        elif action_flag == "already_here":
            print("You're already here! (Type LOOK to get details)")
        elif action_flag == "no_escape":
            pass
        # TALK TALK TALK TALK
        elif action_flag == "talk":
            pass
        elif action_flag == "talk_to_whom":
            print("Who do you want to talk to?")
        elif action_flag == "sparky_not_here":
            print("Sparky can't hear you from here (he's usually upstairs somewhere).")
        elif action_flag == "spud_not_here":
            print("Spud isn't in this room right now.")
        elif action_flag == "rodney_not_here":
            print("Rodney can't hear you right now. He must be cleaning elsewhere.")
        elif action_flag == "tango_not_here":
            print("Tango isn't in this room! (he's usually on his perch in the kitchen).")
        elif action_flag == "idk_talk":
            print("I'm not sure who you want me to talk to!")
        # ASK ASK ASK ASK
        elif action_flag == "ask_who":
            print("Who would you like to ask?")
        elif action_flag == "idk_ask":
            print("I'm not sure who you want me to ask!")
        # GIVE GIVE GIVE GIVE
        elif action_flag == "give":
            pass
        elif action_flag == "give_who":
            print("Who do you want me to give something to?")
        elif action_flag == "sparky_not_here_give":
            print("You can't give Sparky something if he's not here!")
        elif action_flag == "spud_not_here_give":
            print("You can't give Spud something if he's not here!")
        elif action_flag == "rodney_not_here_give":
            print("You can't give Rodney something if he's not here!")
        elif action_flag == "tango_not_here_give":
            print("You can't give Tango something if he's not here!")
        elif action_flag == "idk_give":
            print("I'm not sure who you want me to give something to!")
        # ATTACK ATTACK ATTACK ATTACK
        elif action_flag == "what_attack":
            print("What do you want me to attack?")
        elif action_flag == "idk_attack":
            print("I'm not sure what you want me to attack!")
        elif action_flag == "attack":
            pass
        # HELP HELP HELP HELP
        elif action_flag == "help":
            if not talked_to_tango:
                print("List of commands: \n GO <room> \n TAKE <item> \n DROP <item> \n LOOK \n EXAMINE <anything> \n \
INVENTORY or I \n TALK <someone> \n ASK <someone> \n GIVE <someone> \n HELP")
            else:
                print("List of commands: \n GO <room> \n TAKE <item> \n DROP <item> \n LOOK \n EXAMINE <anything> \n \
INVENTORY or I \n TALK <someone> \n ASK <someone> \n GIVE <someone> \n ATTACK <someone> \n HEALTH \n HELP")
        # HEALTH HEALTH HEALTH HEALTH
        elif action_flag == "health":
            if inventory.health > 3:
                print("Your current health is: " + str(inventory.health))
            else:
                print("Your current health is: " + str(inventory.health))
                print("(you should drink some JUICE to recover)")
        # FINAL BOSS FINAL BOSS FINAL BOSS
        elif action_flag == "final_boss":
            pass
        for item in inventory.items:
            if action_flag == item.name:
                print(item.examine)
        for item in current_room.items:
            if action_flag == item.name:
                print(item.examine)
        for character in current_room.characters:
            if action_flag == character.name:
                print(character.examine)
        for room in current_room.next_location:
            if action_flag == room[0]:
                print("I should probably GO there before I examine it.")
        if action_flag == "":
            print("I'm sorry I couldn't quite understand that! Type HELP for a list of commands!")
