class Inventory():
    """Overall class to manage the user inventory."""

    def __init__(self):
        """Initialize attributes of the inventory."""
        # Initialize empty inventory.
        self.inventory = {}
        
    def call(self):
        """Print out user inventory."""
        print("\n-========== Inventory ===========-")

        # Respond if there is nothing in inventory.
        if not(self.inventory):
            print("\n   ---------- empty -----------   ")
        # Print out inventory.
        else:           
            for item in self.inventory.keys():
                print(f"-|- \n-|- {item} ({self.inventory[item]})")
                print("-|-")
                
    def add(self, item, amount):
        """Increment item number in user inventory."""
        # If the item does not exist in inventory, add it to inventory.
        if item not in self.inventory:
            self.inventory[item] = 0

        # Increase item by item amount.
        self.inventory[item] += amount

    def remove(self, item, amount):
        """Remove the item from inventory if item amount is 0."""
        # Decrease the item by item amout.
        self.inventory[item] -= amount
        
        # If the item does not exist in iventory, remove it from inventory.
        if self.inventory[item] == 0:
            del self.inventory[item]