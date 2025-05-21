import random

# Character representations on the map
MONSTER_CHAR = 'M'   # Monster
HEALTH_CHAR = 'H'    # Health potion
PLAYER_CHAR = 'P'    # Player
BOSS_CHAR = 'B'      # Boss (e.g. Mewtwo)

def create_map(n):
    """
    Create an n x n 2D grid filled with empty spaces.
    """
    return [[' ' for _ in range(n)] for _ in range(n)]

def auto_monster_and_health(size):
    """
    Automatically determine how many monsters and potions to place,
    based on the map size.
    """
    if size <= 5:
        return random.randint(4, 6), random.randint(2, 3)
    elif size <= 8:
        return random.randint(6, 10), random.randint(3, 5)
    else:
        return random.randint(10, 15), random.randint(5, 7)

def populate_map(grid, monster_count, health_count, place_boss=True, player_start=(0, 0)):
    """
    Randomly place monsters, potions, and optionally the Boss on the map.
    Avoid placing anything at the player's starting position.
    """
    size = len(grid)
    available_positions = [(i, j) for i in range(size) for j in range(size) if (i, j) != player_start]

    # Place Boss
    if place_boss and available_positions:
        x, y = random.choice(available_positions)
        grid[x][y] = BOSS_CHAR
        available_positions.remove((x, y))

    # Place monsters
    for _ in range(monster_count):
        if available_positions:
            x, y = random.choice(available_positions)
            grid[x][y] = MONSTER_CHAR
            available_positions.remove((x, y))

    # Place potions
    for _ in range(health_count):
        if available_positions:
            x, y = random.choice(available_positions)
            grid[x][y] = HEALTH_CHAR
            available_positions.remove((x, y))

def display_map(grid, player_pos):
    """
    Display the map in a grid format, marking the player's current position.
    """
    size = len(grid)
    for i in range(size):
        row_display = ''
        for j in range(size):
            if (i, j) == player_pos:
                row_display += '| ' + PLAYER_CHAR + ' '
            else:
                row_display += '| ' + grid[i][j] + ' '
        row_display += '|'
        print(row_display)

def place_entity(grid, entity_char, player_pos):
    """
    Randomly place a new entity ('M', 'H', 'B') on a free space, 
    avoiding the player's current location.
    """
    size = len(grid)
    empty_positions = [(i, j) for i in range(size) for j in range(size)
                       if grid[i][j] == ' ' and (i, j) != player_pos]
    if empty_positions:
        x, y = random.choice(empty_positions)
        grid[x][y] = entity_char
        entity_name = {'M': 'wild Pokémon 🐾', 'H': 'potion 🧪', 'B': 'Mewtwo 👑'}
        print(f"✨ A new {entity_name.get(entity_char, 'entity')} has appeared somewhere on the map!")

# Test the map
if __name__ == '__main__':
    from map import create_map, populate_map, display_map

    size = 3
    grid = create_map(size)
    populate_map(grid, monster_count=5, health_count=3, place_boss=True)
    player_pos = (0, 0)
    display_map(grid, player_pos)