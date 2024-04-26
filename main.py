"""
Author:         Aiden Mills
Date:           04/25/2024
Assignment:     Project 2
Course:         CPSC1051
Lab Section:    001

https://github.com/aidenjmills

Create a role play game 
"""

#Class used to call on the text for every situation
class Text:
    #initializes text function
    def __init__(self, room_name, turn = 0):
        self.room_name = room_name
        self.type = ''
        self.turn = turn
        self.intros = {'Beginning Room': 'You are in a cramped, musty room surrounded by spiders and other bugs crawling along the walls. In front of you is an extremely old and worn down door.', 
                        'Main Hall': 'You are in a massive, open hall with a rundown chandelier hanging from the ceiling. Cobwebs cover everything, and in each corner of the room is a door.', 
                        'Cliff Room': 'You open the door to find the entire room is a massive pit. You accidentally kick a pebble down the hole, but you never hear it hit the bottom', 
                        'Girl Room': 'You open the door to a very dimly lit room. The only light source is a flickering lightbulb hanging from the middle of the ceiling. Below the lightbulb sits a little girl in a bow and a dress facing the other direction. She appears to be crying.', 
                        'Armor Room': ['You open the door to find the room is almost completely black. You can not see anything. After your eyes adjust a bit, you are able to make out a dark figure standing in the back left corner. It is facing you…', 
                        'The room is illuminated. You discover the figure in the corner is just an old suit of armor carrying what looks like a medieval mace. The entire room is filled with old, antique furniture and valuables. ', 
                        'You walk deeper and deeper into the room, astounded by the artifacts and relics. Something falls behind you, and you turn just in time to see the suit of armor sprinting full speed in your direction. It uses its mace and takes a swing at your head…', 
                        "You hear the 'Woosh' from the mace flying right over your head. The mace crashes into an old dresser, and the suit of armor completely falls apart into the separate pieces of metal. The mace lays on the ground in front of you. It may be useful later.", 
                        'The room is exactly as you left it. The suit of armor is still destroyed on the floor.', 
                        'You narrowly escape the raging suit of armor and slam the door behind you. '], 
                        'Mirror Room': ['You enter a dark room with a trail of lit candles lying on the ground. They form a path that leads to an old, dirty, body-length mirror.',
                        'You follow the path up to the mirror. After looking in it for a bit, you decide there is nothing of use in this room. That is exactly when your reflection smiles at you.', 
                        'Before your reflection can reach out of the mirror to grab you, you smash the mirror to a million pieces with the medieval mace. This reveals a doorway with a staircase leading somewhere up.'], 
                        'Riddle Room': ["After climbing the stairs, you enter a small corridor with a door at the end. Above the door is written,\n“When things go wrong, what can you always count on?”\nIt appears to be a riddle. You should give it an answer.", 
                        'Nothing happens. That must not be right.', 'Again nothing. You hear something moving up the staircase behind you.']}
        self.deaths = {'Beginning Room': 'Suddenly, the walls all around you start to close in. Before you can even react, you are being squished alive.', 
                        'Cliff Room': 'Now, why would you go and do that?', 'Girl Room': 'You approach the girl and try to place your hand on her shoulder. However, your hand goes right through her. Suddenly, the girl turns her head 180 degrees to face you, and her smile goes from ear to ear…', 
                        'Armor Room': ['You creep into the room, trying your best to watch your step in the dark. You look up to see if you can still see the figure, but it is gone…', 'Home Run!'], 
                        'Mirror Room': ['You follow the path up to the mirror. After looking in it for a bit, you decide there is nothing of use in this room. That is exactly when your reflection smiles at you. Suddenly your reflection’s hand reaches out of the mirror and grabs you by the neck…', 
                        'You drop the mace and try to run away. However, you are not fast enough, and a hand grabs you on the shoulder and jerks you back.'], 
                        'Riddle Room': '“Too long,” someone whispers behind you as you are dragged backward into the shadowy staircase below.'}

    #class for rooms with one intro
    def intro_text(self):
        return self.intros[self.room_name]
    
    #class for rooms with one death
    def death_text(self):
        return self.deaths[self.room_name]

    #class for rooms with more than one death
    def special_death_text(self):
        return self.deaths[self.room_name][self.turn - 1]

    #class for rooms with more than one intro
    def special_intro_text(self):
        return self.intros[self.room_name][self.turn - 1]

    #Determines which text function to return
    def __str__(self):
        if self.type == 'intro' and self.turn != 0:
            return self.special_intro_text()
        elif self.type == 'intro':
            return self.intro_text()
        elif self.type == 'death' and self.turn != 0:
            return self.special_death_text()
        elif self.type == 'death':
            return self.death_text()

#Class for the starting rooom
class BegRoom:
    #initializes the room class
    def __init__(self, turn_count = 0, death_count = 0, object = False):
        self.turn_count = turn_count
        self.death_count = death_count
        self.text = Text('Beginning Room')
        self.object = object
    
    #Runs the move function when the Class is called
    def __call__(self):
        return self.move()
    
    #Runs the main program for the room
    def move(self):
        print()
        self.text.type = 'intro'
        print(self.text)
        print('What would you like to do?')
        print('A. Leave the room through the door')
        print('B. Stay inside and look around')
        choice = input().lower().strip()
        check = True
        while check:
            if choice == 'a':
                self.turn_count += 1
                main_hall = MainHall(self.turn_count, self.death_count, self.object)
                main_hall()
                check = False
            elif choice == 'b':
                print()
                self.turn_count += 1
                self.text.type = 'death'
                print(self.text)
                self.death_count += 1
                print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                self.move()
                check = False
            else:
                print('Please select a valid option')
                choice = input().lower().strip()

#Class for the Main Hall room
class MainHall:
    #initializes the room class
    def __init__(self, turn_count, death_count, object):
        self.turn_count = turn_count
        self.death_count = death_count
        self.text = Text('Main Hall')
        self.object = object

    #Runs the move function whenever the class is called
    def __call__(self):
        return self.move()

    #runs the main program for the room
    def move(self):
        print()
        self.text.type = 'intro'
        print(self.text)
        print('What would you like to do?')
        print('A. Enter Door #1')
        print('B. Enter Door #2')
        print('C. Enter Door #3')
        print('D. Enter Door #4')
        choice = input().lower().strip()
        check = True
        while check:
            if choice == 'a':
                self.turn_count += 1
                cliff_room = CliffRoom(self.turn_count, self.death_count, self.object)
                cliff_room()
                check = False
            elif choice == 'b':
                self.turn_count += 1
                armor_room = ArmorRoom(self.turn_count, self.death_count, self.object)
                armor_room()
                check = False
            elif choice == 'c':
                self.turn_count += 1
                girl_room = GirlRoom(self.turn_count, self.death_count, self.object)
                girl_room()
                check = False
            elif choice == 'd':
                self.turn_count += 1
                mirror_room = MirrorRoom(self.turn_count, self.death_count, self.object)
                mirror_room()
                check = False
            else:
                print('Please select a valid option')
                choice = input().lower().strip()  

#Class for the room with the cliff
class CliffRoom:
    #initializes the room class
    def __init__(self, turn_count, death_count, object):
        self.turn_count = turn_count
        self.death_count = death_count
        self.text = Text('Cliff Room')
        self.object = object

    #Runs the move function when the class is called
    def __call__(self):
        return self.move()

    #Runs the program for the room
    def move(self):
        print()
        self.text.type = 'intro'
        print(self.text)
        print('What would you like to do?')
        print('A. Continue Forward')
        print('B. Turn back around')
        choice = input().lower().strip()
        check = True
        while check:
            if choice == 'a':
                print()
                self.turn_count += 1
                self.text.type = 'death'
                print(self.text)
                self.death_count += 1
                print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                beg_room = BegRoom(self.turn_count, self.death_count)
                beg_room()
                check = False
            elif choice == 'b':
                self.turn_count += 1
                main_hall = MainHall(self.turn_count, self.death_count, self.object)
                main_hall()
                check = False
            else:
                print('Please select a valid option')
                choice = input().lower().strip() 

#Class for the room with the little girl
class GirlRoom:
    #initializes the girl room class
    def __init__(self, turn_count, death_count, object):
        self.turn_count = turn_count
        self.death_count = death_count
        self.text = Text('Girl Room')
        self.object = object

    #runs the move function when the class is called
    def __call__(self):
        return self.move()

    #Runs the main program for the room 
    def move(self):
        print()
        self.text.type = 'intro'
        print(self.text)
        print('What would you like to do?')
        print('A. Approach the girl and offer help')
        print('B. Turn back around')
        choice = input().lower().strip()
        check = True
        while check:
            if choice == 'a':
                print()
                self.turn_count += 1
                self.text.type = 'death'
                print(self.text)
                self.death_count += 1
                print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                beg_room = BegRoom(self.turn_count, self.death_count)
                beg_room()
                check = False
            elif choice == 'b':
                self.turn_count += 1
                main_hall = MainHall(self.turn_count, self.death_count, self.object)
                main_hall()
                check = False
            else:
                Print('Please select a valid option')
                choice = input().lower().strip() 

#Class for the room with the armor suit
class ArmorRoom:
    #initializes the armor room class
    def __init__(self, turn_count, death_count, object):
        self.turn_count = turn_count
        self.death_count = death_count
        self.text = Text('Armor Room')
        self.object = object

    #Determines which function to run when the class is called
    def __call__(self):
        if not self.object:
            return self.move1()
        else:
            return self.move2()

    #Function that runs the program for the room when the user has the mace
    def move2(self):
        print()
        self.text.type = 'intro'
        self.text.turn = 5
        print(self.text)
        main_hall = MainHall(self.turn_count, self.death_count, self.object)
        main_hall()

    #Function that runs the program for the room when the user does not have the mace
    def move1(self):
        print()
        self.text.type = 'intro'
        self.text.turn = 1
        print(self.text)
        print('What would you like to do?')
        print('A. Continue forward in the dark')
        print('B. Try the light switch')
        print('C. Turn back around')
        choice = input().lower().strip()
        check = True
        while check:
            if choice == 'a':
                self.turn_count += 1
                self.text.type = 'death'
                self.text.turn = 1
                print(self.text)
                self.death_count += 1
                print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                beg_room = BegRoom(self.turn_count, self.death_count,)
                beg_room()
                check = False
            elif choice == 'b':
                print()
                self.turn_count += 1
                self.text.type = 'intro'
                self.text.turn = 2
                print(self.text)
                print('What would you like to do?')
                print('A. Enter the room and look around')
                print('B. Turn back around')
                choice = input().lower().strip()
                check = True
                while check:
                    if choice == 'a':
                        print()
                        self.turn_count += 1
                        self.text.type = 'intro'
                        self.text.turn = 3
                        print(self.text)
                        print('What would you like to do?')
                        print('A. Duck')
                        print('B. Jump')
                        print('C. Try an run')
                        choice = input().lower().strip()
                        check = True
                        while check:
                            if choice == 'a':
                                print()
                                self.turn_count += 1
                                self.text.type = 'intro'
                                self.text.turn = 4
                                print(self.text)
                                print('What would you like to do?')
                                print('A. Grab the mace and exit the room')
                                print('B. Exit the room')
                                choice = input().lower().strip()
                                check = True
                                while check:
                                    if choice == 'a':
                                        self.object = True
                                        self.turn_count += 1
                                        main_hall = MainHall(self.turn_count, self.death_count, self.object)
                                        main_hall()
                                        check = False
                                    elif choice == 'b':
                                        self.turn_count += 1
                                        main_hall = MainHall(self.turn_count, self.death_count, self.object)
                                        main_hall()
                                        check = False
                                    else:
                                        print('Please select a valid option')
                                        choice = input().lower().strip()
                            elif choice == 'b':
                                self.turn_count += 1
                                self.text.type = 'death'
                                self.text.turn = 2
                                print(self.text)
                                self.death_count += 1
                                print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                                beg_room = BegRoom(self.turn_count, self.death_count,)
                                beg_room()
                                check = False
                            elif choice == 'c':
                                print()
                                self.text.type = 'intro'
                                self.text.turn = 6
                                print(self.text)
                                self.turn_count += 1
                                main_hall = MainHall(self.turn_count, self.death_count, self.object)
                                main_hall()
                                check = False
                            else:
                                print('Please select a valid option')
                                choice = input().lower().strip() 
                    elif choice == 'b':
                        self.turn_count += 1
                        main_hall = MainHall(self.turn_count, self.death_count, self.object)
                        main_hall()
                        check = False
                    else:
                        print('Please select a valid option')
                        choice = input().lower().strip() 
            elif choice == 'c':
                self.turn_count += 1
                main_hall = MainHall(self.turn_count, self.death_count, self.object)
                main_hall()
                check = False
            else:
                print('Please select a valid option')
                choice = input().lower().strip() 

#Class for the room with the mirror
class MirrorRoom:
    #Initializes the mirror room class
    def __init__(self, turn_count, death_count, object):
        self.turn_count = turn_count
        self.death_count = death_count
        self.text = Text('Mirror Room')
        self.object = object

    #determines which function to run when the class is called
    def __call__(self):
        if not self.object:
            return self.move1()
        else:
            return self.move2()

    #Function that runs the program for the room when the user does not have the mace
    def move1(self):
        print()
        self.text.type = 'intro'
        self.text.turn = 1
        print(self.text)
        print('What would you like to do?')
        print('A. Approach the mirror and get a closer look')
        print('B. Turn back around')
        choice = input().lower().strip()
        check = True
        while check:
            if choice == 'a':
                print()
                self.turn_count += 1
                self.text.turn = 1
                self.text.type = 'death'
                print(self.text)
                self.death_count += 1
                print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                beg_room = BegRoom(self.turn_count, self.death_count)
                beg_room()
                check = False
            elif choice == 'b':
                self.turn_count += 1
                main_hall = MainHall(self.turn_count, self.death_count, self.object)
                main_hall()
                check = False
            else:
                Print('Please select a valid option')
                choice = input().lower().strip()
    
    #Function that runs the program for the room when the user has the mace
    def move2(self):
        print()
        self.text.type = 'intro'
        self.text.turn = 1
        print(self.text)
        print('What would you like to do?')
        print('A. Approach the mirror and get a closer look')
        print('B. Turn back around')
        choice = input().lower().strip()
        check = True
        while check:
            if choice == 'a':
                print()
                self.turn_count += 1
                self.text.type = 'intro'
                self.text.turn = 2
                print(self.text)
                print('What would you like to do?')
                print('A. Use the mace and try to smash the mirror')
                print('B. Try and run away')
                choice = input().lower().strip()
                check = True
                while check:
                    if choice == 'a':
                        print()
                        self.turn_count += 1
                        self.text.type = 'intro'
                        self.text.turn = 3
                        print(self.text)
                        print('What would you like to do?')
                        print('A. Walk up the staircase')
                        print('B. Leave the room')
                        choice = input().lower().strip()
                        check = True
                        while check:
                            if choice == 'a':
                                self.turn_count += 1
                                riddle_room = RiddleRoom(self.turn_count, self.death_count)
                                riddle_room()
                                check = False
                            elif choice == 'b':
                                print()
                                self.turn_count += 1
                                self.text.type = 'death'
                                self.text.turn = 2
                                print(self.text)
                                self.death_count += 1
                                print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                                beg_room = BegRoom(self.turn_count, self.death_count)
                                beg_room()
                                check = False
                            else:
                                print('Please select a valid option')
                                choice = input().lower().strip()
                    elif choice == 'b':
                        print()
                        self.turn_count += 1
                        self.text.type = 'death'
                        self.text.turn = 1
                        print(self.text)
                        self.death_count += 1
                        print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                        beg_room = BegRoom(self.turn_count, self.death_count)
                        beg_room()
                        check = False
                    else:
                        print('Please select a valid option')
                        choice = input().lower().strip()  
            elif choice == 'b':
                self.turn_count += 1
                main_hall = MainHall(self.turn_count, self.death_count, self.object)
                main_hall()
                check = False
            else:
                print('Please select a valid option')
                choice = input().lower().strip()

#Class for the room with the riddle
class RiddleRoom:
    #initializes room class
    def __init__(self, turn_count, death_count):
        self.turn_count = turn_count
        self.death_count = death_count
        self.text = Text('Riddle Room')

    #returns move function when class is called
    def __call__(self):
        return self.move()

    #Function that runs the program for the room
    def move(self):
        print()
        self.text.type = 'intro'
        self.text.turn = 1
        print(self.text)
        answer = input().lower().strip()
        check = True
        global counts
        while check:
            if answer == 'fingers':
                self.turn_count += 1
                counts = [self.turn_count, self.death_count]
                check = False
            else:
                print()
                self.text.type = 'intro'
                self.turn_count += 1
                self.text.turn = 2
                print(self.text)
                answer = input().lower().strip()
                if answer == 'fingers':
                    self.turn_count += 1
                    counts = [self.turn_count, self.death_count]
                    check = False
                else:
                    print()
                    self.turn_count += 1
                    self.text.turn = 3
                    print(self.text)
                    answer = input().lower().strip()
                    if answer == 'fingers':
                        self.turn_count += 1
                        counts = [self.turn_count, self.death_count]
                        check = False
                    else:
                        print()
                        self.turn_count += 1
                        self.death_count += 1
                        self.text.type = 'death'
                        print(self.text)
                        print(f'\nYou Died\n\nAttempt #{self.death_count + 1}')
                        beg_room = BegRoom(self.turn_count, self.death_count)
                        beg_room()

#Main function          
def main():
    print('The Haunted Mansion Escape Room')
    print('        by: Aiden Mills')
    print()
    print('Do your best to try and escape')
    beg_room = BegRoom()
    beg_room()
    print('The door in front of you opens and you can finally see the light of day...')
    print()
    print('Congradulations! You have escaped the haunted house.')
    #Puts the results on the text file
    results = open('Results.txt', 'w')
    results.write(f'Game Results\n')
    results.write(f'   - Total turns taken: {counts[0]}\n')
    results.write(f'   - Total deaths: {counts[1]}')
    results.close()
    print()
    print("Check your results on the 'Results.txt' file")

if __name__ == "__main__":
    main()