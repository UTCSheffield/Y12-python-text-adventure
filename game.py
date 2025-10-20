"""
A simple text adventure designed as a learning experience for new programmers.
"""
__author__ = 'Phillip Johnson'
__author__ = 'Mr Eggleton'
# __author__ = ''

import world
from player import Player


def play():
    world.load_tiles()  # Load the tiles into the world from map.txt
    player = Player()

    # The Start tile on the map sets the player location variables
    room = world.get_tile(player.location_x, player.location_y)
    print(room.intro_text())  # Print the Start room text

    # Loop while the player is alive but hasn't won
    while player.is_alive() and not player.victory:
        room = world.get_tile(player.location_x, player.location_y)
        room.modify_player(player)

        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:  # Print all the actions here
                print(action)

            action_input = input('Action: ')  # get the input
            for action in available_actions:  # loop around the actions
                if action_input == action.hotkey:  # Did they press this key?
                    player.do_action(action, **action.kwargs)  # do the action
                    break


if __name__ == "__main__":  # If we have started this python file run this code
    play()
