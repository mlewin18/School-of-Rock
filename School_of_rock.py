"""
Shep Lewin
++++++++++
December 11, 2018
+++++++++++++++++
"""

from printing import *
from ascii import *
from instructions import *
from time import *
import random

terminal = '>>> '
start_time = perf_counter()
death_count = 0
call_count = 0
chapter_count = 0
mvmnt_count = 0
found_items = []

test = False
chapNum = 0.0
callNum = 0
y = 0.0
events = []
listedItemNumbers = []
actions = []
yes = ['Yes', 'Y', 'Yep', 'Sure']
no = ['No', 'N', 'Nope', 'Nah']
chptrlist = [0, 0.1]
POlst = [
    'Archer, Jennifer - 8469        Bhik-Ghanie, Rebecca - 2193 ',
    'Bardo, Lucy - 6686             Bevan, John - 1346          ',
    'Barsky, Marina - 6753          Bervy-Walters, Samuel - 2290',
    'Baum, David - 2535             Bergman, Michael - 7943     ',
    'Baumann, Michael - 4161        Beaumont-Biggs, Karen - 3936',
]
voiceOnThePhone = [
    """
    Hey, buddy, I bet your leg's hurting pretty bad right about now isn't it?
    Sorry you ended up on that roof, the parties responsible for your survival are being punished as we speak.
    In the mean time, would you mind dying?
    It would save me a lot of effort.
    """,
    """
    So you're still alive.
    Not so great a following orders are we?
    Seriously though, just succumb to to sweet release of death already!
    """,
    """ 
    Look, friend.
    I'm gonna level with you.
    You being alive is really fanning the flame under my ass and at this point my butthole is starting to singe.
    Stop being and pain and die.
    """,
    """
    Alright, at this point I'm starting to think that you just aren't getting the message.
    Assuming that you may be a few braincells short of a lobe I'm going to walk you through this whole death thing.
    It's pretty simple, just find the closest sharp object an swallow it.
    """
]


def phone_call(setup):
    global callNum, call_count
    call_count += 1
    if "Picked up cellphone" in events and 'First phone call' not in events:  # First phone call with cell
        phn = 'the cellphone you picked up starts buzzing.'
        events.append('First phone call')
    elif "Picked up cellphone" in events and 'First phone call' in events:  # Other calls with cell
        phn = 'the cellphone starts buzzing again.'
    else:
        phn = 'a mounted phone near you begins to ring.'  # All calls without cell
    start = setup + phn
    Break = '-'*20
    Type(start)
    Type('You answer it.')
    print()
    Type(Break)
    for i in (voiceOnThePhone[callNum].splitlines()):
        Type(i)
    Type(Break)
    Type("~CLICK~", speed=0, footer=1)
    Type("The line goes dead.")
    callNum += 1


def intro():
    School_of_Rock = Ascii('School of Rock')
    School = Ascii('School        ')
    of = Ascii('       of      ')
    Rock = Ascii('           Rock')
    down(20)
    Type('Welcome to...', speed=3)
    wait(3)
    down(60)
    wait(0.7)
    print(School.compile())
    down(20)
    wait(1)
    down(60)
    print(of.compile())
    down(20)
    wait(1)
    down(60)
    print(Rock.compile())
    down(20)
    wait(1)
    down(60)
    wait(1.5)
    School_of_Rock.flatten()

# /////////////////////////////////////////[ENDINGS]////////////////////////////////////////////


def death():
    global chapNum, death_count
    death_count += 1
    wait(2.5)
    title('DEATH')
    Type("You died of stupid.", footer=1)
    Type("|Q|uit", 0)
    Type("|R|estart chapter", 0)
    print()
    choice = input(">>> ")
    choice = choice.capitalize()
    if choice in 'Quit':
        quit()
    elif choice in "Restart":
        Type("Alright...", 3)
        Type("Just don't do it again!")
        wait(2)
        if chapNum < 1:
            chapNum = 0.1
        else:
            chapNum -= 1
        new_chapter()
    else:
        Type('...', 3)
        Type("That wasn't an option.")
        death()


def end():
    global chapNum
    print()
    title('Congratulations!')
    wait(.5)
    Type("Your journey ends here, pilot!")
    Type("You've limped your way to a temporary end of the game.", footer=1)
    Type("|R|estart chapter", 0)
    Type("|S|it and wait /!\\ Snacks not provided /!\\ ", 0)
    Type("|Q|uit", 0)
    print()
    choice = input(">>> ")
    choice = choice.capitalize()
    if choice in 'QuitSit':
        quit()
    elif choice in "Restart":
        if chapNum < 1:
            chapNum = 0.1
        else:
            chapNum -= 1
        wait(2)
        new_chapter()
    else:
        Type('...', 3)
        Type("That wasn't an option.")
        end()


def alford():
    #  STATUS
    state_list = []
    if 'Food' not in events:
        state_list.append('Hungry')
    if 'Water' not in events:
        state_list.append('Thirsty')
    if 'Crutch' not in found_items:
        state_list.append('Injured')
    status = str(' and '.join(state_list))
    #  MEMORY
    memories = ['nothing at all.']
    if 'Meet the bird' in events:
        memories.append('your time with the mutant bird.')
    if 0.3 in chptrlist:
        memories.append('falling off a roof.')
    if 'survived explosion' in events:
        memories.append('almost being blown up.')
    memory = 'You collapse face first on the pavement and slowly expire while thinking fondly of ' + random.choice(memories)
    #  STORY
    Type('You pass the gatehouse and step out onto the main road.', footer=1)
    if len(state_list) > 0:
        status = '[ You are ' + status + ' ]'
        Type(status, footer=1)
        wait(1)
    Type('|W|alk to town', 0)
    Type('|S|tay on campus', 0, footer=1)
    choice = input(terminal)
    if choice in 'Walk to town':
        if len(state_list) == 0:
            win_screen()
        else:
            Type('You make it about fifty feet.')
            if 'Injured' in state_list:
                Type('You\'re then reminded that one of your legs is little more than a meat sack full of bone fragments.')
            elif 'Thirsty' in state_list:
                Type('You\'re then reminded that you\'re so dehydrated your tongue feels like Hardtack.')
            elif 'Hungry' in state_list:
                Type('You\'re then reminded that you\'re so hungry even breathing tastes good.')
            Type(memory)
            death()
    elif choice in 'Return to campus':
        Act()


def win_screen():
    wait(3)
    title('You Win!')
    Type('Congratulations on escaping campus.')
    wehere = 'We here at Treadstone hope this simulation has left you feeling fulfilled and happy with your use of the last ' + str(round(perf_counter() - start_time, 5)) + ' seconds.'
    Type(wehere)
    Type('Enjoy the rest of of your life.')
    wait(5)
    credits()


def credits():
    writers = ['Max Bernstein', 'Sam Statter', 'Benji Kapit']
    supporters = ['Mia Palmiero', 'Derrick Hansen']
    artists = ['Glenn Chappell', 'Bruce Jakeway', 'Paul Burton', 'jsm', 'http://patorjk.com']
    title('CREDITS')
    Type('WRITING', 0, footer=1, lag=0.8)
    for i in writers:
        Type(i, 0, lag=0.8)
    for i in range(2):
        Type('\n', lag=0.8)

    Type('MORAL SUPPORT', 0, footer=1, lag=0.8)
    for i in supporters:
        Type(i, 0, lag=0.8)
    for i in range(2):
        Type('\n', lag=0.8)

    Type('ASCII images', 0, footer=1, lag=0.8)
    for i in artists:
        Type(i, 0, lag=0.8)

    for i in range(50):
        Type('\n', lag=0.8)

# /////////////////////////////////////////[CHOICES]////////////////////////////////////////////


def falling_off_a_roof():
    print()
    Type("|R|ight leg", 0)
    Type("|L|eft leg", 0)
    print()
    choice = input(terminal)
    choice = choice.capitalize()
    if choice in 'Left leg':
        Type("That's two for two and a drop out of the gene pool.")
        Type("You bake like an equally immobile potato in the hot sun.")
        Type("Darwin reigns eternal.")
        death()
    elif choice in 'Right leg':
        Type("Ever break a glow stick twice?")
        Type("Same principle but this time the juice isn't glowing.")
        chptrlist.append(2.1)
        new_chapter()
    else:
        Type("Invalid leg, choose a different one.")
        falling_off_a_roof()


def drinking_acid():
    Type('[Taste]', 0)
    Type("Hmmm, you're parched.")
    Type("Hey, that beaker over there has some funny colored water in it!", footer=1)
    Type("|D|rink from it")
    Type("|L|eave it")
    choice = input(terminal).capitalize()
    if choice == "Drink from it":
        Type("The cool liquid burns going down.")
        Type("literally.")
        Type("Hey since when could you breathe through that hole in your neck?", 1)
        death()
    elif choice == "Leave it":
        Type("Yeah, DUH right?")
    else:
        Type("Just drink the acid or don't. Stop making this complicated.")
        drinking_acid()


def leave_with_the_bird():
    Type('|L|eave with the bird', 0)
    Type('|S|tay on campus', 0)
    print()
    choice = input(terminal).capitalize()
    if choice in 'Leave with the bird':
        win_screen()
    elif choice in 'Stay on campus':
        new_chapter()
    else:
        error('Invalid Choice')
        leave_with_the_bird()


def picking_the_lock():
    Type('|y/n|', 0)
    print()
    choice = input(terminal).capitalize()
    if choice in yes:
        del items[5]
        chptrlist.append(1.5)
    elif choice in no:
        chptrlist.append(1.5)
        Act()
    else:
        error('Invalid choice')
        picking_the_lock()


def eating_the_food():
    Type("Your stomach is rumbling like a mac truck and there's food all around (putrid though it might be).")
    Type('Grab some grub?')
    Type("|E|at", 0)
    Type("|D|on't eat", 0)
    print()
    choice = input(terminal)
    if choice in 'Eat':
        Type('As soon as you swallow the unidentifiable food you realize your mistake.')
        Type("But it's too late.")
        Type('You erupt from both ends!')
        death()
    if choice in "Don't eat":
        Type('Probably the right move.')


def drinking_the_water():
    Type('|D|rink from the hose.', 0)
    Type('|L|eave it', 0)
    print()
    choice = input(terminal).capitalize()
    if choice in 'Drink from the hose':
        Type('The cool water is refreshing and you feel energized.')
        events.append('Water')
        print()
    elif choice not in 'Drink from the hose' and choice not in 'Leave it':
        error('Invalid choice')
        drinking_the_water()


def opening_the_box(boxID):
    Type('Enter a code or type \'exit\'')
    code = input(terminal).capitalize()
    for i in code:
        if i and i not in '01234567891011213' or code == '' and code != 'Exit':
            error('invalid code')
    if int(code) == 6753:
        del items[(int(boxID)-1)]
        Type('Something clicks and the box springs open to reveal...')
        wait(1)
        Type('A gourmet bag of croutons?')
        found_item('Gourmet croutons')
    else:
        Type('Nothing happens')


def reading_the_list():
    Type('Examine the list?')
    Type('[y/n]', 0)
    print()
    choice = input(terminal).capitalize()
    if choice in yes:
        for i in POlst:
            Type(i, 0)


def eating_the_bars():
    Type('Eat the bars?')
    Type("|E|at", 0)
    Type("|D|on't eat", 0)
    print()
    choice = input(terminal).capitalize()
    if choice in 'Eat':
        Type('You tear the wrappers off the bars and shove them down your throat without chewing.')
        Type('A small portion of the hole inside of you is filled.')
        Type('Maybe the counseling offices upstairs can finish the job.')
        events.append('Food')
    if choice in "Don't eat":
        Type('Right.')
        Type('Probably expired or something.')


#  /////////////////////////////////////////[INVENTORY]////////////////////////////////////////////


items = [
    # {'Name': '','Description':''},`
    {'Name': 'Chewed gum', 'Description': 'Your pocket overfloweth with used gum.\nStimulate your senses!',
     'img':
    '''
 ______ 
|   _  |
|_-|_|_|
|      |
| CHEW |
|______|

    '''
     },
    {'Name': 'Wallet', 'Description': 'A wallet containing a student ID and two dollars.',
     'img':
     '''
 ________ 
|       ||
|  BMF  ||
|_______||

     '''
     },
    {'Name': 'Calculator watch',
     'Description': '''You wield the power to complete basic mathematical operations!
6 + 9 = 7''',
     'img':
'''
 |_| 
|[5]|
|:::|
 |'|
'''
     },
    {'Name': 'Small tin can', 'Description': 'The label reads "Fancy Feast."\nIt\'s half empty.',
     'img':
"""
+-----+
|Fancy|
|Feast|
+-----+
"""
     },
    {'Name': 'Severed pinky toe', 'Description': 'You want a toe?\nI can get you a toe.\nBelieve me.\nThere are ways, Dude.',
     'img':
"""
  _  
||_||
| _ |
|   |
^^^^^
"""
     },
    {'Name': 'Bobby pin',
     'Description': 'You lick it.\nIt tastes like home.',
     'img':
"""
<==x=
"""
     },
]


newItem = [
    {'Name': 'Cellphone',
     'Description':
"""
Holding it makes you feel powerful.
You're filled with the urge to waste hours of your life absorbing forgettable media.
""",
     "img":
"""
 __i 
|---|
|[_]|
|:::|
|:::|
'---'
"""
},
    {'Name': 'Lock box',
     'Description': 'opening_the_box()',
     "img":
"""
  _______________ 
+--------------+ |
| [0][0][0][0] | |
+--------------+' 
"""
     },
    {'Name': 'Sword',
     'Description':
        """
You can see your reflection in it.
You consider using it to pick that thing out of your teeth.
        """,
     'img':
"""
      /|__________________
O|===|* >________________/
      \|                  
"""
     },
     {'Name': 'Crutch',
      'Description':
         """
Hobbling around on it makes you feel like a pirate.
Avast, ye landlubbers! Haul in the poop deck and hoist the tiller!
         """,
      'img':
"""
 _                                          
| \________  ____________                   
 \   ______||___  ______ \_________ _ ____  
  | |___________||______| ________//_//___:]
 / ________||____________/                  
|_/                                         
"""
      },
     {'Name': 'Gourmet croutons',
      'Description':
         """
The unholy bread cubes mock you.
They are both stale and lacking of substance.
         """,
      'img':
"""
    +--+    .             
.   |  |        ::       .
    +--+   +-+            
    .      | |      +--+  
::         +-+    . |  |  
                    +--+  
"""
      },
]


def found_item(item):
    for i in newItem:
        if i['Name'] == item:
            question = "Pick up the " + i['Name'] + '?'
            print()
            Type(question)
            Type('|y/n|', 0, footer=1)
            yn = input(terminal)
            yn = yn.capitalize()
            if yn in yes:
                items.append(i)
                Type("[Item added to inventory]")
                print()
                events.append('Picked up ' + item)
            elif yn not in yes and yn not in no:
                error('Invalid Choice')
    found_items.append(item)


# /////////////////////////////////////////[CHAPTERS]////////////////////////////////////////////


def change_chapter():
    global chapNum, chapter_count
    if round(chptrlist[-1]) != round(chptrlist[-2]):
        chapTemp = round(chapNum)
        chapTemp += 1.1
        chapNum = chapTemp
        chapter_count += 1
    else:
        chapNum += .1
        chapter_count += .1


def new_chapter():
    change_chapter()
    chapline = 'CHAPTER ' + str(round(chapNum, 1))
    title(chapline)
    if chptrlist[-1] == 0.1:
        Type("The wind wakes you.")
        wait(0.5)
        Type("The glaring sun sears your eyes as you blink the sleep out of them.")
        wait(0.5)
        Type("Where are you?")
        wait(2)
        Type("As a matter of fact...", 3)
        wait(0.7)
        Type("Who are you?")
        Act()
        new_chapter()
    elif chptrlist[-1] == 0.2:
        Type("As you climb to your feet a sharp pain shoots through your right leg.")
        Type("It feels fractured.")
        Type("You consider sitting, but the metal you were lying on seems less appealing than just hopping around.")
        Type("You wrack your sun-baked raisin of a brain for your next step.")
        Act()
        new_chapter()
    elif chptrlist[-1] == 0.3:
        Type("You hop over to the low side of the roof and begin to lower yourself off but you slip!")
        Type("Land on your...")
        falling_off_a_roof()
        new_chapter()
    elif chptrlist[-1] == 1.1:  # In fisher
        Type("You find yourself in a cool dark building.")
        Type("Lab equipment lies in disarray.")
        Type("A mysterious ticking noise emanates from a stove top halfway down the hall.")
        Act()
        new_chapter()
    elif chptrlist[-1] == 1.2:  # unlocked
        Type("Stepping into the doorway you take a look around the room.")
        Type("It looks like a cleared out office with only a desk and a chair.")
        if "Cellphone" not in found_items or "Lock box" not in found_items:
            Type("Sitting on the desk are two objects, a cellphone and a small lock-box.")
            found_item('Cellphone')
            found_item('Lock box')
        Act()
        new_chapter()
    elif chptrlist[-1] == 1.3:  # unlocked explosion
        Type("Stepping into the doorway you take a look around the room.")
        Type("It looks like a cleared out office with only a desk and a chair.")
        Type("Sitting in the desk are two objects, a cellphone and a small lock-box.")
        Type("You consider picking them up but your train of thought is interrupted...")
        Type("By the gas introducing itself to the electric igniter on the stove.")
        Type("Maybe your atomized braincells will miss each other.")
        Type("Probably not.")
        death()
    elif chptrlist[-1] == 1.4:  # locked
        Type("You limp over to the door only to find it's locked.")
        Type("If only you had something to pick it with...")
        Type("Break your bobby pin to pick the lock?")
        picking_the_lock()
    elif chptrlist[-1] == 1.5:  # inside locked
        events.append('unlocked locked')
        Type("After an embarrassing amount of time you manage to unlock the door.")
        Type("It swings open and you notice several things at once.")
        Type("1) the smell of gas is REALLY strong in here.")
        Type("2) there's a SWORD lying on a desk.")
        Type("3) Verbal Kint WAS Keyser Söze!")
        found_item('Sword')
        Type("The gas is starting to make you dizzy so you step into the hallway.")
        Type("Something about that ticking noise is really starting to get to you...")
        Act()
        new_chapter()
    elif chptrlist[-1] == 1.6:  # exit door
        Type("Under the exit sign is a pair of glass doors leading out of the building.")
        Type("You recognize the doors as locking automatically from the inside,")
        Type("If you leave you wont be able to get back in!")
        Act(True)
        if chptrlist[-1] == 1.1 and 'unlocked locked' in events:
            Type("Feeling indecisive you turn back to face the assorted doors-")
            Type("and get a fireball to the face!")
            Type("The gas from the open lab and the igniter on the stove top were in cahoots!")
            death()
        new_chapter()
    elif chptrlist[-1] == 2.1:  # outside fisher
        if 'unlocked locked' in events:
            events.append('survived explosion')
            Type("Just as the door swings closed behind you a fireball erupts inside the building!")
            Type("The force of the resulting shock wave nearly knocks you off your feet.")
            Type("Tinnitus plays your eardrums like a preschooler on the cymbals.")
            Type("You brush the dust off you like a badass and thank Darwin that you weren't in that building a second longer.")
            Type("Squinting in the bright sunlight you survey your surroundings.")
        elif 0.3 in chptrlist:
            Type("You grit your teeth and survey your surroundings.")
        else:
            Type("Stepping through the doors you squint in the bright sunlight and survey your surroundings.")
        Type("Ahead of you is a beautiful golf course with various-")
        Type("That can't be right.")
        Type("What kind of golf course would have buildings on it?")
        Type("Oh, wait.")
        Type("This is Bard College at Simon's Rock!")
        Type("While the specifics of your situation are still hazy the three visible buildings and their functions slowly slide into your memory...")
        Type('Your deep-seated impulse to run from your problems takes hold and, paired with the feeling that something has gone terribly wrong, you know what you have to do:')
        title('ESCAPE CAMPUS')
        Act()
        new_chapter()
    elif chptrlist[-1] == 3.1:  # Dining hall (hose water, mutant bird?)
        phone_call('As you approach the dining hall ')
        Type("Looking at the Dining Hall you feel a sense of disappointment.")
        Type("You attribute it to the overwhelming stench of rotting food.")
        Act()
        new_chapter()
    elif chptrlist[-1] == 3.2:  # Entering alarmed door
        if 'Meet the bird' in events:
            Type("The massive bird greets you with it's tiny beady eyes.")
        else:
            Type('As you pull the door open a fire alarm sounds!')
            Type('You stumble backwards in surprise and clumsily fall on your ass.')
            Type('As you struggle back to your feet a massive shadow falls over you.')
            Type('Looking up you find yourself faced by a very hungry looking twenty foot tall mutant bird!')
            Type('Scared out of your limited wits you evaluate your possible courses of action.')
            events.append('Meet the bird')
        Act(True)
        new_chapter()
    elif chptrlist[-1] == 3.21:  # Fight the bird
        if 'Picked up Sword' in events:
            Type('Raising your sword, you face your fine feathered foe.')
            Type('The bird pauses for a moment and with a kind of "Eh" look, flaps off into the distance.')
            events.append('Scare the bird')
            new_chapter()
        else:
            Type('Raising your fists, you face your fine feathered foe.')
            Type('"HAVE AT THEE!!" You yell, before remembering you have no weapon but your sun burnt hands.')
            Type('For a moment you regret not picking up a stick or something.')
            death()
    elif chptrlist[-1] == 3.22:  # Run for the door
        Type('Forgetting for a moment that your leg is severely injured you break for the door.')
        Type('You immediately unbalance and face plant, embarrassing yourself to no end.')
        Type("The bird doesn't mind, it eats you anyway.")
        death()
    elif chptrlist[-1] == 3.23:  # Talk to the bird
        Type('"Hey man, what can I do for ya?"')
        Type("You say, assuming the bird's gender identity for, like, no reason.")
        if 'Picked up Gourmet croutons' in events:
            Type('"I MOVE FOR NO MAN..."')
            Type('"WITHOUT CROUTONS."')
            Type('it responds.')
            Type("\"Well, I've got news for you!\"")
            Type('You say, drawing the croutons from your back pocket.')
            Type('The bird accepts your humble offering and in return offers to fly you off campus.')
            leave_with_the_bird()
        else:
            Type('"I MOVE FOR NO MAN."')
            Type('It replies in a rich base.')
            Type('Intimidated and a little dejected you turn your back on the dining hall.')
            chptrlist.append(3.5)
            Act(move_only=True)
            new_chapter()
    elif chptrlist[-1] == 3.3:  # Inside dining hall
        Type('Opening the door you step inside the Dining hall.')
        Act()
        new_chapter()
    elif chptrlist[-1] == 3.4:
        Type("While looking around the dining hall you find a car key and a set of crutches.")
        found_item('Car key')
        found_item('Crutches')
        eating_the_food()  # choose next chapter
    elif chptrlist[-1] == 3.5:  # Leaving dining hall
        Type('Stepping away from the dining hall you gaze across the fields of green at the remaining buildings.')
        Act(move_only=True)
        new_chapter()
    elif chptrlist[-1] == 3.6:  # Searching outside of dining hall
        Type('As you walk the perimeter of the building you see a hose and spigot.')
        drinking_the_water()
        Type('Around the back of the building you find a boarded up door and nothing else of interest.')
        Act()
        new_chapter()
    elif chptrlist[-1] == 4.1:  # Dolliver dorm  (bike parts)
        phone_call('As you approach the dorm ')
        end()
    elif chptrlist[-1] == 5.1:  # Student union  (crutch, food)
        phone_call('As you approach the student union ')
        if 'exhausted' not in events:
            events.append('exhausted')
            Type('As you approach the front door of the Student Union a wave of exhaustion washes over you.')
            Type('Dehydration, hunger, and your injury are taking their toll.')
            Type('You\'re not sure how much longer you can stay on your feet.')
        Act()
        new_chapter()
    elif chptrlist[-1] == 5.2:  # Inside SU
        Type('Stepping inside the building you take stock of your options.')
        Act()
        new_chapter()
    elif chptrlist[-1] == 5.3:  # Security desk
        Type('The security door is locked.')
        Type('On it is a list of teachers\' names and their respective P.O. box numbers.')
        reading_the_list()
        Act()
        new_chapter()
    elif chptrlist[-1] == 5.4:  # Vending machines
        if 'visited vending' in events:
            if 'Food' in events:
                Type('The vending machines are completely empty')
            else:
                Type('The two granola bars still sit in the broken machine.')
                eating_the_bars()
            if 'Picked up Crutch' not in events:
                found_item('Crutch')
        else:
            Type('All three of the vending machines are completely ransacked.')
            Type('You\'re about to give up hope when a plastic glimmer catches your eye.')
            Type('Two granola bars are sitting at the back of one of the machines!')
            eating_the_bars()
            Type('Lying next to one of the machines is a single crutch.')
            found_item('Crutch')
            events.append('visited vending')
        Act()
        new_chapter()
    elif chptrlist[-1] == 5.5:  # Leaving SU
        Type('Stepping out of the Student Union you evaluate your options.')
        Act(move_only=True)
        new_chapter()
    elif chptrlist[-1] == 6.1:  # Road to town
        alford()
    else:
        Type("Invalid chapter", 0)
    print()
    #  'Look', 'Feel', 'hear', 'Taste', 'Smell', 'Move'

# /////////////////////////////////////////[CHAPTER FUNCTIONS]////////////////////////////////////////////

# While debugging act(), sense(), and move() I had trouble getting the functions to pass a "chptr" var all the way back
# to new_chapter() so instead of troubleshooting for another few hours I created a persistent list to which I could
# append the most recent chapter change directly from move(). This also made the front end chapter # easier to compute
# as the current and most recent chapter can both be called directly from chptrlist[].


class Act:  # Hah. get it?
    def __init__(self, move_only=False):
        self.center = center_finder()
        self.actions = []
        self.movements = []
        self.senses = []
        self.chptr = chptrlist[-1]
        self.moveOpts = []
        self.chstr = str(self.chptr)
        for i in open('movements.txt', 'r'):
            self.movements.append(i)
        for i in open('senses.txt', 'r'):
            self.senses.append(i)
        if move_only:
            self.list_move()
            self.choose_move()
        else:
            self.refine()
            self.list_actions()
            self.choose_action()
        new_chapter()

    def refine(self):
        for i in ['Look', 'Feel', 'Hear', 'Taste', 'Smell', 'Move', 'Inventory']:
            for k in self.senses:
                if str(chptrlist[-1])+i in k and i not in self.actions:  # accounts for duplicates
                    self.actions.append(i)
                    break
        self.actions.append('Move')
        self.actions.append('Inventory')

    def list_actions(self):
        print('\n')
        wait(1)
        bars = 0
        printlist = [' ']
        for i in self.actions:  # Prints out the list with correct spacing and brackets
            string = ['|']
            for j in i:
                string.append(j)
            string.insert(2, '|')
            item = (''.join(string) + "  ")
            printlist.append(item)
        for i in printlist:
            bars += len(i)

        Type('-' * bars, 0)
        print()
        print(' '*int(self.center-(bars//2)), end='')
        for i in printlist:
            print(i, end='')
            wait(0.3)
            sys.stdout.flush()
        Type('-' * bars, 0)
        print()

    def choose_action(self):
        self.item = False
        action = input(terminal).capitalize()
        for i in self.actions:
            if action in i:
                self.item = i
        if not self.item:
            error('Invalid action')
            self.choose_action()
        bug_hunt(self.item)
        bug_hunt(self.actions)
        if self.item in self.actions and self.item not in 'MoveInventory':
            bug_hunt('Item in actions')
            self.list_sense()
        elif self.item == "Inventory":
            bug_hunt('act.if2')
            self.list_inventory()
            self.choose_inventory()
        elif self.item == "Move":
            self.list_move()
            self.choose_move()

    def list_sense(self):
        index = self.chstr + self.item
        bug_hunt(index)
        if index == '1.1Taste':
            drinking_acid()
        else:
            bug_hunt('run else')
            header = '[' + self.item + ']'
            Type(header, 0)
            wait(1)
            for string in self.senses:
                bug_hunt('in for loop')
                if index in string:
                    Type(string[10:-1])
                bug_hunt('Printed strings')
            bug_hunt('finished for loop')
        self.actions.remove(self.item)  # The user can no longer use this sense till the end of the chapter
        print()
        self.list_actions()
        self.choose_action()

    def list_inventory(self):
        print()
        Type("(Select an item number for more details)", footer=2, )
        num = 1
        Type('[0]  Exit inventory', 0, -9, footer=1)
        wait(.3)
        for i in items:
            k = str(num)
            itemID = "[" + k + "]  " + i['Name']
            Type(itemID, 0, -9, lag=0.005)
            wait(0.3)
            sys.stdout.flush()
            listedItemNumbers.append(str(num))
            num += 1

    def choose_inventory(self):
        print()
        print()
        itemID = input("Inventory> ")
        for i in itemID:
            if i and i not in '01234567891011213' or itemID == '':
                error('invalid id')
                self.choose_inventory()
        if itemID in listedItemNumbers:
            bug_hunt('check.if1')
            print()
            item = items[int(itemID) - 1]
            wait(1)
            img = (item['img']).split('\n')
            for i in img:
                Type(i, 0, lag=0)
            name = ('[' + item['Name'] + ']')
            wait(.5)
            Type(name, 0)
            if item['Name'] == 'Lock box':
                opening_the_box(itemID)
            else:
                descrpt = (item['Description']).split('\n')
                for i in range(len(descrpt)):
                    Type(descrpt[i])
            self.choose_inventory()
        elif itemID == '0':
            self.list_actions()
            self.choose_action()
        else:
            error("Item not listed")
            print()
            self.choose_inventory()

    def list_move(self):
        print()
        for i in self.movements:  # prints movement options
            sys.stdout.flush()
            if self.chstr in i[0:3]:
                wait(.5)
                self.moveOpts.append(i[7:-1])
                prnt = '|' + i[7] + '|' + i[8:-8]
                Type(prnt, 0)
        print()

    def choose_move(self):
        global mvmnt_count
        mvmnt_count += 1
        final = False
        choice = input(terminal).capitalize()
        for i in self.moveOpts:
            if choice in i[0:-8]:
                events.append(self.chstr + choice)
                final = float(i[-4:])
                chptrlist.append(final)
        if not final:
            error('Invalid movement')
            self.choose_move()


def title(chptrstring):
    string = Ascii(chptrstring)
    wait(1.5)
    down(60)
    print(string.compile())
    down(20)
    wait(2)


def cheat():
    global test
    test = True
    global speed
    k = input(' Cheat> ').capitalize()
    if 'Start' in k:
        k = float(k[6:])
        chptrlist.append(k)
        new_chapter()
    elif "Death" in k:
        death()
    elif 'Get' in k:
        item = k[4:]
        item = item.capitalize()
        found_item(item)
        cheat()
    elif k == '':
        chptrlist.append(0.2)
        new_chapter()
    elif 'Speed' in k:
        test = False
        k = k[5:]
        print('text speed set to', k, '\n')
        speed = float(k)
        cheat()
    elif k == 'Act':
        Act()
    elif k == 'Skip':
        new_chapter()
    elif k == 'Ending':
        alford()
    elif k == 'Win':
        win_screen()
    elif 'Fix' in k:
        item = k[4:]
        item = item.capitalize()
        events.append(item)
        cheat()
    else:
        error('Invalid Cheat')
        cheat()


def error(text):
    txt = text.capitalize()
    errtxt = '/!\\ ['+txt+'] /!\\'
    print()
    Type(errtxt, 1)
    print()


def bug_hunt(function_name):
    # function_name = str(function_name)
    # print('[[['+function_name+']]]')
    pass


def main():
    global speed
    print('Type \"setup\" to center, \"Help\" for a tutorial, \"Credits\" for credits, or \"Start\" to begin the game.')
    v = input(terminal)
    v = v.capitalize()
    if v == 'Start' or v == '':
        intro()
        new_chapter()
    elif v == 'Test':
        speed = 0.00
        cheat()
    elif v == 'Help':
        instructions()
        main()
    elif v == 'Credits':
        credits()
        main()
    elif v == 'Setup':
        Center(50)
        intro()
        new_chapter()
    else:
        main()


if __name__ == '__main__':
    main()
