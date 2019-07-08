class Room():

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        self.first_visit = False
        self.first_visit_text = None
        
    def set_description(self, room_description):
        self.description = room_description
        
    def get_description(self):
        return self.description
        
    def set_name(self, room_name):
        self.name = room_name
        
    def get_name(self):
        return self.name
        
    def set_character(self, character):
        self.character = character
        
    def get_character(self):
        return self.character
        
    def set_item(self, item):
        self.item = item
        
    def get_item(self):
        return self.item        
        
    def set_first_visit(self, first_visit):
        self.first_visit = first_visit
        
    def get_first_visit(self):
        return self.first_visit     

    def set_first_visit_text(self, first_visit_text):
        self.first_visit_text = first_visit_text
        
    def get_first_visit_text(self):
        return self.first_visit_text     
                
    def describe(self): 
        print(self.description)
        
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        
    def get_details(self):
        """Print the room details"""
        print('The ' + self.get_name())
        print('-'*15)
        print(self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print('The ' + room.get_name() + ' is ' + direction)

            
    def move(self, direction):
        """Used to make Character move to different rrom"""
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print('Ga ada jalannya')
            return self