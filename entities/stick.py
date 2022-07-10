import sys
sys.path.append('/Users/fiona_l13/Desktop/cheeseburger_minecraft2/components')

from item import Item 

class Stick():
    """Overall class to manage behaviors and attributes of stick."""
    
    def __init__(self):
        self.item = Item(
            "a thin piece of wood that has fallen or been cut from a tree, can "
            "be crafted from wood planks"
            )
   
   
   
# Test.
if __name__ == '__main__':     
    stick = Stick()
    print(stick.item.description)