class Inventory():
    """Overall class to manage the user inventory."""

    def __init__(self, game):
        """Initialize attributes of the inventory."""
        # Initialize the items from the game
        self.items = game.items
        
    def call(self):
        """Print out user inventory."""
        print("\n-========== Inventory ===========-")
        
        # Loop through each item to determine if inventory is empty.
        inventory_empty = True
        for item in self.items.keys():
            if self.items[item].amount != 0:
                # Set inventory_empty to False.
                inventory_empty = False
                # Exit the loop.
                break
        
        # Print the inventory.    
        if inventory_empty:
            print("\n   ---------- empty ----------   ")
        else:
            for item in self.items.keys():
                if self.items[item].amount != 0:
                    # Print the item and the amount.
                    print(f"-|- \n-|- {item} ({self.items[item].amount})")
            print("-|-")
        
    def add(self, item, amount):
        """Increment the amount attribute of the item."""
        self.items[item].amount += amount

    def remove(self, item, amount):
        """Decrease the amount attribute of the item."""
        self.items[item].amount -= amount