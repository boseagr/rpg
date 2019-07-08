class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.status = 'alive'

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.name + ' is ' + self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
        
    def hug(self):
        print(self.name + " doesn't want to hug you")

    def set_status(self, status):
        self.status = status
        
    def get_status(self):
        return self.status


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        
    def set_weakness(self, weakness):
        self.weakness = weakness
        
    def get_weakness(self):
        return self.weakness
        
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print('you fend ' + self.name + ' off with the ' + combat_item)
            self.set_status('deceased')
            return True
        else:
            print(self.name + ' crush you, you puny adventurer')
            return False
            

class Friend(Character):
    def __init__(self, char_name, char_description):
         super().__init__(char_name, char_description)
         self.likeness = None
         self.item = None
         
    def set_item(self, item):
        self.item = item
        
    def get_item(self):
        return self.item
        
    def set_likeness(self, item):
        self.likeness = item
        
    def get_likeness(self):
        return self.likeness        
         
    def hug(self):
        print(self.name + ' hug you back')
        
    def sent_gift(self, gift):
        if gift == self.likeness:
            print(self.name + ' really like your gift and give you something')
            return True
        else:
            print('[' + self.name + ' says] : Thanks, but you will need it more')
            print(self.name + ' give the item back to you')
            return False