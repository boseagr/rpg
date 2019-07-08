import learnrpg
from time import sleep

my_item = None

kitchen = learnrpg.Room('Kitchen')
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = learnrpg.Room('Dining Hall')
dining_hall.set_description('A room with large square table. There are candles at the center of table. One dirty plate also on it')
dining_hall.set_first_visit(True)
dining_hall.set_first_visit_text('You jolt with surprise, there is something there, something so smelly, although not that smelly, but it smelly, you see dave, your butcher, become something else')

ballroom = learnrpg.Room('Ballroom')
ballroom.set_description('Quite large but dark, spider make their homes here')

kitchen.link_room(dining_hall, 'south')
dining_hall.link_room(kitchen, 'north')
dining_hall.link_room(ballroom, 'west')
ballroom.link_room(dining_hall, 'east')

dave = learnrpg.Enemy('Dave', 'A brainless Zombie')
dave.set_conversation('Bzzz..... harrr.....')
dave.set_weakness('cheese')
dining_hall.set_character(dave)

jane = learnrpg.Friend('Jane', 'the cook at your mansion, cute looking girl but can get mad for small mistake')
jane.set_conversation('Hello Master, looks like i am missing something, but i forget what is it..')
jane.set_likeness('sword')
kitchen.set_character(jane)

cheese = learnrpg.Item('cheese')
cheese.set_description('a dairy product, still new and fresh.')
jane.set_item(cheese)

knife = learnrpg.Item('sword')
knife.set_description('Quite big sword (or knife), long and sharp to chop meat')
ballroom.set_item(knife)

all_command = ['help', "north", "south", "east", "west", 'talk', 'fight', 'give', 'take', 'hand', 'exit', 'hug']
current_room = kitchen
game_running = True

print('type "help" for all possible command')
print('------------------------------------')
print('\n')
print('Story')
print('-----')
print('You wake up in the night. You feel so hungry that you immediately go to kitchen, however you only saw your cook there. You hear some noise nearby. What is it?')

while game_running:
    print('\n')
    current_room.get_details()
    
    first_visit = current_room.get_first_visit()
    if first_visit:
        print('\n')    
        print(current_room.get_first_visit_text())
        current_room.set_first_visit(False)
        sleep(0.8)
        
    possible_command = ''   
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        print('\n')
        inhabitant.describe()
        possible_command += '[talk] [fight] [hug] [give]'
        
    item = current_room.get_item()
    if item is not None:
        print('\n')
        item.describe()
        possible_command += ' [take]'
    
    for direction in current_room.linked_rooms:
        possible_command += ' [' + direction + ']'
    
    if my_item is not None:
        possible_command += ' [hand]'
        
    print('[possible command: ' + possible_command + ']')
    command = input('> ')
    
    if command == 'help':
        print('all commands :')
        print('-'*15)
        print('"north", "south", "east", "west" : to go to the respected direction')
        print('"talk" : talk to any character in room')
        print('"fight"  : fight the character in room')
        print('"give"  : give something to the character in room')
        print('"hug"  : hug character in room')
        print('"take"  : take item in room')
        print('"hand"  : get detail of the item you hold')
        print('"exit"  : exit game')
    elif command in ['north', 'south', 'east', 'west']:
        sleep(0.2)
        current_room = current_room.move(command)
    elif command == 'exit':
       game_running = False
    elif command == 'hand':
       sleep(0.2)
       if my_item is not None:
           my_item.describe_at_hand()
       else:
          print("You didn't hold anything")        
    elif command == 'take':
        sleep(0.2)
        if item is not None and my_item == None:
            print('You take : "' + item.get_name() + '", then you hold it tight')
            my_item = item
            current_room.set_item(None)
        elif my_item is not None:
            print('You currently hold "' + my_item.get_name() + '", you cant hold any item anymore')
        else:
           print('Nothing to take here')
    elif command in ['talk', 'hug', 'fight', 'give']:
        sleep(0.2)
        if inhabitant is None:
            print('ga ada siapa-siapa di sini')
        elif command == 'talk':
            inhabitant.talk()
            sleep(0.2)
        elif command == 'hug':
            inhabitant.hug()
            sleep(0.2)
        elif command == 'give':
            if my_item is None:
                print('You have no item to give to ' + inhabitant.name)
            elif isinstance(inhabitant, Enemy):        
                print(inhabitant.name + ' is hate you, ' + inhabitant.name + " don't want anything from you")
            else:
                print('You give ' + my_item.get_name() + ' to ' + inhabitant.name)
                likey = inhabitant.sent_gift(my_item.get_name())
                sleep(1)
                if likey:
                    print(inhabitant.name + ' give you ' + inhabitant.get_item().get_name() + ' in return')
                    my_item = inhabitant.get_item()
                    sleep(1)
        elif command == 'fight':
            sleep(0.2)
            if isinstance(inhabitant, Friend):
                inhabitant.fight('love')
            elif my_item is None:
                print('You have no item to fight ' + inhabitant.name)
                sleep(1)
                print('You step back from ' +inhabitant.name)
                sleep(1)            
            else:
                print('You want to fight ' + inhabitant.name + ' with ' + my_item.get_name() + '? [type "y" to continue fight or type anything to cancel and step back]')
                tool = input('> ')
                if tool == 'y':
                    print('You fight ' + inhabitant.name + ' with ' + my_item.get_name() + ' bravely.')
                    sleep(1)
                    game_running = inhabitant.fight(my_item.get_name())
                    sleep(1)
                else:
                    sleep(1)
                    print('You step back from ' +inhabitant.name)
                    sleep(1)
                if inhabitant.get_status() == 'deceased':
                    print(inhabitant.name + ' is gone now')
                    current_room.set_character(None)
    else:
        sleep(0.2)
        print('I dont understand what you mean. [Hint : type "help" to list all available command]')
       
    if dining_hall.get_character() == None:
        sleep(1)
        print('You have finished the game, thanks for playing')
        sleep(1)
        game_running = False
