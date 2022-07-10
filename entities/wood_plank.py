import sys
sys.path.append('/Users/fiona_l13/Desktop/cheeseburger_minecraft2/components')

from item import Item 

class WoodPlank():
    """Overall class to manage behaviors and attributes of wood plank."""
    
    def __init__(self):
        self.item = Item(
            "a long, flat, rectangular piece of wood, can be crafted from logs"
            )
   
   
   
# Test.
if __name__ == '__main__':     
    wood_plank = WoodPlank()
    print(wood_plank.item.description)