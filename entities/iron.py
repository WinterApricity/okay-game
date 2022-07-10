import sys
sys.path.append('/Users/fiona_l13/Desktop/cheeseburger_minecraft2/components')

from item import Item 

class Iron():
    """Overall class to manage behaviors and attributes of iron."""
    
    def __init__(self):
        self.item = Item("a lustrous, ductile, malleable, silver-gray metal")
   
   
   
# Test.
if __name__ == '__main__':     
    iron = Iron()
    print(iron.item.description)