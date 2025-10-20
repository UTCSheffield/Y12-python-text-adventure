__author__ = 'Phillip Johnson'
__author__ = 'Mr Eggleton'
# __author__ = ''

_world = {}
starting_position = (0, 0)


def get_tile(x, y):
    """Returns the tile at the given coordinates or None if there is no tile.

    :param x: the x-coordinate in the worldspace
    :param y: the y-coordinate in the worldspace
    :return: the tile at the given coordinates or None if there is no tile
    """
    return _world.get((x, y))


def load_tiles():
    """Parses a file that describes the world space into the _world object"""
    with open('resources/map.txt', 'r') as f:
        rows = f.readlines()

    x_max = len(rows[0].split('\t'))  # Splitting up the map with Tabs
    for y in range(len(rows)):
        cols = rows[y].split('\t')  # Splitting up the map with Tabs
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '')  # stripping off newlines

            if tile_name == 'Start':  # record the Start position
                global starting_position
                starting_position = (x, y)

            if tile_name == '':
                _world[(x, y)] = None  # If no room mark the map space blank
            else:
                # Create a Tile object for the Class in the map at (x, y)
                _world[(x, y)] = getattr(__import__('tiles'), tile_name)(x, y)
