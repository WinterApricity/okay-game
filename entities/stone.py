import sys
sys.path.append('/Users/fiona_l13/Desktop/cheeseburger_minecraft2/components')

from item import Item 

class Stone():
    """Overall class to manage behaviors and attributes of stone."""
    
    def __init__(self):
        self.item = Item("rock, it's a piece of rock")
   
   
   
# Test.
if __name__ == '__main__':     
    stone = Stone()
    print(stone.item.description)