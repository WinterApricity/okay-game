from random import choice
from wsgiref.handlers import read_environ

class Forage():
    """Overall class for all behaviors of the foraging system."""
    
    def __init__(self, game):
        """Initialize properties needed for foraging."""
        # Initialize player.
        self.player = game.player
        self.inventory = game.inventory
    
        # Create a dictionary with 
        #   all item names as the key and required exp as the value.
        self.items = self._get_all_forageables()

        # Create a list of foreagable items based on user exp level.
        self.forageable_items = self._get_forageable_items()

    def _get_all_forageables(self):
        """Retrieve all forageable items from txt file."""
        # Open the txt file.
        with open('forageable_items.txt', 'r') as file:
            # Append each line of the file to a list.
            content = file.readlines()
            # Initialize an empty dictionary.
            items = {}
            # Loop through every line.
            for line in content:
                # Spilt up each line into items and required exp.
                item, exp = line.split(',')
                # Add item, exp to dictionary.
                items[item.strip()] = int(exp.strip())

        return items

    def _get_forageable_items(self):
        """Return a list of all forageable items based on user exp level."""
        items = []
        for item in self.items.keys():
            if self.items[item] <= self.player.exp_level:
                items.append(item)
        
        return items

    def forage(self):
        """
        Return a random item that the user can forage,
            and add it to player inventory.
        """
        # Get random item.
        random_item = choice(self.forageable_items)
        print(f"\n-== You have found 1 {random_item}. ==-")
        
        # Increment item amount in inventory.
        self.inventory.add(random_item, 1)

        return random_item