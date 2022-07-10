import sys
sys.path.append('/Users/fiona_l13/Desktop/cheeseburger_minecraft2/components')

from item import Item 
from hunger import Hunger

class Watermelon():
    """Overall class to manage behaviors and attributes of watermelon."""
    
    def __init__(self):
        self.item = Item(
            "a large oblong or roundish fruit with a hard green or white rind "
            "often striped or variegated, a sweet watery pink, yellowish, or "
            "red pulp, and usually many seeds"
            )
        self.hunger = Hunger(4)
   
   
   
# Test.
if __name__ == '__main__':     
    watermelon = Watermelon()
    print(watermelon.item.description)
    print(watermelon.hunger.hunger)