class Craft():
    """Overall class for all recipes and related crafting behavior for the game."""

    def __init__(self, game):
        """Initialize all recipes."""
        # Initialize user.
        self.player = game.player
        self.inventory = game.inventory

        # Dictionary of all craftable items.
        self.recipes = {
            'wood plank': {
                'exp': 1,
                'amount': 4,
                'recipe': {'log': 1}
            }, 

            'stick': {
                'exp': 1,
                'amount': 4,
                'recipe': {'wood plank': 2},
            }
        }

        # Create a list of craftable items based on user exp level.
        self.craftable_items = self._get_craftable_items()

    def _get_craftable_items(self):
        """Return a list of all craftable items based on user exp level."""
        items = []
        for item in self.recipes.keys():
            if self.recipes[item]['exp'] <= self.player.exp_level:
                items.append(item)

        return items

    def show_craftable_items(self):
        """Show craftable items."""
        print("\n-========== Craftable Items ==========-")
        print("| ", end='')
        index = 0
        for item in self.craftable_items:
            print(f"{item}", end=' | ')

            # Limit the number of items in the inventory to 3 per row.
            index += 1
            if index % 3 == 0:
                print("\n----------------------------------")
                print('| ', end='')

    def show_recipe(self, item):
        """Show the recipe of the item that the user requested."""
        # Run if item cannot be crafted.
        if item not in self.recipes.keys():
            print("\n-== This item is unavailable. ==-")
        else:
            # Print recipe details.
            print(f"\n-===== Recipe Details of {item.title()} =====-")
            # Print level requirement for recipe.
            print(f"|| \n|| Level Requirement = {str(self.recipes[item]['exp'])}")

            # Print item recipe.
            print(f"|| \n|| -== Item Recipe ==-")
            for material in self.recipes[item]['recipe'].keys():
                print(f"|| -|- \n|| -|- {material} ({self.recipes[item]['recipe'][material]})")
            print("|| -|-")
            
            # Print recipe output.
            print(f"|| \n|| -== Output ==- \n|| -|- \n|| -|- {item} ({str(self.recipes[item]['amount'])})")
            print("|| -|-")

    def is_craftable(self, item):
        """Return True if the item is currenty craftable."""
        if item in self.craftable_items:
            return True
        else:
            return False

    def has_material(self, item, amount):
        """
        Return True if the player has the materials for the item that they want 
        to craft.
        """
        for material in self.recipes[item]['recipe'].keys():
            if self.recipes[item]['recipe'][material] * amount > self.inventory.items[material].amount:
                return False

        return True
    
    def craft(self, item, amount):
        """
        Remove the materials used from user inventory.
        Add the crafted item to user inventory.
        """
        # Remove material.
        for material in self.recipes[item]['recipe'].keys():
            material_amount = self.recipes[item]['recipe'][material] * amount
            self.inventory.remove(material, material_amount)

        # Add crafted item.
        recipe_yield = self.recipes[item]['amount'] * amount
        self.inventory.add(item, recipe_yield)

# Example: 
#   Dict = { 
#       DiamondPickaxe: {Exp: 1, Amount: 1, Recipe: {Wood: 3, Diamond: 3}},
#       IronSword: {Exp: 1, Amount: 1, Recipe: {Wood: 3, Iron:3}}
#   }
