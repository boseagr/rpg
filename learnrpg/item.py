class Item:
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        
    def set_name(self, item_name):
        self.name = item_name
        
    def get_name(self):
        return self.name
        
    def set_description(self, description):
        self.description = description
        
    def get_description(self):
        return self.description

    def describe(self):
        print('There is "'+ self.name + '" inside the room!' )
        print( self.name + ' is ' + self.description )
        
    def describe_at_hand(self):
        """Print the item if it taken by character"""
        print(self.name + ' - ' + self.description )        