class Item():
    """Overall class to manage all items of the game."""
    
    def __init__(self, name, description): 
        """Initialize attributes of items."""
        self.name = name
        self.description = description
        # Set the item amount in the user's inventory to 0.
        self.amount = 0
        
class Food(Item):
    """Subclass of Item, contains all food items of the game."""
    
    def __init__(self, name, description, hunger):
        """Initialize attributes of food."""
        # Inherit from parent class.
        super().__init__(name, description)
        
        # Initailize own attributes.
        self.hunger = hunger
        
    def eat(self):
        """Consume the food and increasee player hunger."""
   
# Test.
if __name__ == '__main__':
    watermelon = Food("Watermelon", "a large oblong or roundish fruit with a "
                        "hard green or white rind often striped or variegated, a "
                        "sweet watery pink, yellowish, or red pulp, and usually "
                        "many seeds", 4)

    print(watermelon.name)
    print(watermelon.description)
    print(watermelon.hunger)