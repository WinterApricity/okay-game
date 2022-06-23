from item_categories import *

# Items.
iron = Item("Iron", "a lustrous, ductile, malleable, silver-gray metal")
log = Item("Log", "a part of the trunk or a large branch of a tree that has "
           "fallen or been cut off")
stick = Item("Stick", "a thin piece of wood that has fallen or been cut from a "
             "tree, can be crafted from wood planks")
stone = Item("Stone", "rock, it's a piece of rock")
wood_plank = Item("Wood plank", "a long, flat, rectangular piece of wood, can "
                  "be crafted from logs")

# Food.
watermelon = Food("Watermelon", "a large oblong or roundish fruit with a "
                        "hard green or white rind often striped or variegated, a "
                        "sweet watery pink, yellowish, or red pulp, and usually "
                        "many seeds", 4)


# Dictionary mapping of item name to item objects.
items = {
    'iron': iron,
    'log': log,
    'stick': stick,
    'stone': stone,
    'wood plank': wood_plank,
    'watermelon': watermelon,
}