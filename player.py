import random
import items
import world

__author__ = 'Phillip Johnson'
__author__ = 'Mr Eggleton'
# __author__ = ''


class Player():
    def __init__(self):
        self.inventory = [items.Gold(15), items.Rock()]  # What the player has
        self.hp = 100  # Health Points
        self.location_x, self.location_y = world.starting_position  # From map
        self.victory = False  # Has the Player Won yet?

    def is_alive(self):
        return self.hp > 0  # Has the player got more than 0 health points?

    def do_action(self, action, **kwargs):  # kwargs = Keyword Arguments
        # This is Python magic, Functions and Methods are also variables
        action_method = getattr(self, action.method.__name__)  # Get the method
        if action_method:
            action_method(**kwargs)  # Do the method with the arguments given

    def print_inventory(self):
        for item in self.inventory:  # Loop around everything the player has
            print(item, '\n')  # Print the __str__() for the inventory item

    def move(self, dx, dy):  # Move to  the next tile / room
        self.location_x += dx  # Add horizontal movement
        self.location_y += dy  # Add vertical movement
        # Print the intro text for this new room
        print(world.get_tile(self.location_x, self.location_y).intro_text())

    def move_north(self):  # Move North
        self.move(dx=0, dy=-1)  # One less in the y axis (0 is the top)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def flee(self, tile):
        """Moves the player randomly to an adjacent tile"""
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
