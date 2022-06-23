from inventory import Inventory
from forage import Forage
from craft import Craft
from player import Player

class FakeMinecraft():
    """Overall class for the game, contains all functions and behaviors."""
    
    def __init__(self):
        """Initialize attributes and behavior for the game."""
        self.inventory = Inventory()
        self.player = Player()
        self.forage = Forage(self)
        self.craft = Craft(self)
        
        # Set the game as running by default.
        self.running = True
        # Start game.
        self._run_game()
        
    def _run_game(self):
        """Begin the main while loop for the game."""
        while self.running:
            print("\n\n-=========== Main Menu ==========-")
            choice = input("|| 1) Open inventory. \n|| 2) Forage. \n|| 3) Craft. \n|| 4) Exit. \n\n>>> ").lower()
            
            if choice in ['1', 'inventory', 'open inventory', 'inv', 'i']:
                self.inventory.call()
            elif choice in ['2', 'forage', 'f']:
                self.forage.forage()
            elif choice in ['3', 'craft', 'crafting', 'crafting menu', 'cm']:
                self._crafting_menu()
            elif choice in ['4', 'exit', 'e']: 
                print("You have exited the game.")
                self.running = False
        
    def _crafting_menu(self):
        """Prompt the user for an item to craft, and add item to inventory."""
        print("\n-========== Crafting Menu ==========-")
        choice = input("|| 1) See craftable items. \n|| 2) Craft. \n|| 3) Exit crafting "
            "menu. \n\n>>> ").lower()

        if choice in ['1', 'see craftable items']:
            self.craft.show_craftable_items()
            self._crafting_recipe()
        elif choice in ['2', 'craft', 'c']:
           self._craft_item()
        elif choice in ['3', 'exit crafting', 'e', 'exit']:
            pass

    def _crafting_recipe(self):
        """
        Prompt the user to view the crafting recipe of any craftable item,
        or exit the crafting menu.
        """
        choice = input("\n\n|| 1) View recipe details \n|| 2) Exit \n\n>>> ").lower()

        if choice in ['1', 'view recipe details', 'view details', 'details', 
                      'recipe', 'r']:
            item = input("\n-- What item would you like to see the details of? "
                "-- \n\n>>> ").lower()
            self.craft.show_recipe(item)
            self._crafting_menu()
        elif choice in ['2', 'exit', 'e']:
            self._crafting_menu()

    def _craft_item(self):
        """Prompt the user to select an item to craft."""
        item = input("\n-== What would you like to craft? ==- \n>>> ")
        amount = int(input("\n-== How many times would you like to craft this "
            "item? ==- \n>>> "))

        if not self.craft.is_craftable(item):
            print("\n-== This item cannot be crafted. ==-")
        elif not self.craft.has_material(item, amount):
            print("\n-== You do not the the resources to craft this item. ==-")
        else:
            self.craft.craft(item, amount)
            print(f"\n-== You crafted {item} {str(amount)} time(s). ==-")