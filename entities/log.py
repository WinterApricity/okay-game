import sys
sys.path.append('/Users/fiona_l13/Desktop/cheeseburger_minecraft2/components')

from item import Item 

class Log():
    """Overall class to manage behaviors and attributes of log."""
    
    def __init__(self):
        self.item = Item(
            "a part of the trunk or a large branch of a tree that has fallen "
            "or been cut off"
            )
   
   
   
# Test.
if __name__ == '__main__':     
    log = Log()
    print(log.item.description)