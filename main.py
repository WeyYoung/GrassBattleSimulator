from map import create_map, populate_map, display_map, auto_monster_and_health, place_entity
from player import Player
from wildmon import WildMon
from battle import rock_paper_scissors

def main():
    # 🌟 Game intro and Pokémon partner selection
    print("🌟 Welcome to the world of Pokémon! 🌟")
    print("Choose your Pokémon partner:")
    print("1. Pikachu ⚡")
    print("2. Charmander 🔥")
    print("3. Bulbasaur 🍃")
    print("4. Squirtle 💧")

    poke_choice = input("Enter the number of your choice: ").strip()
    if poke_choice == '1':
        player_name = "Pikachu"
    elif poke_choice == '2':
        player_name = "Charmander"
    elif poke_choice == '3':
        player_name = "Bulbasaur"
    elif poke_choice == '4':
        player_name = "Squirtle"
    else:
        player_name = "Eevee"

    print(f"\n✨ {player_name}, let's begin our Pokémon adventure together! ✨\n")

    # Prompt for map size
    while True:
        try:
            size = int(input("Enter map size (e.g. 5 for 5x5 map): "))
            if size < 3 or size > 15:
                print("Please enter a number between 3 and 15.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Create and populate map
    grid = create_map(size)
    monster_count, health_count = auto_monster_and_health(size)
    print(f"🗺️ Generating map with {monster_count} monsters and {health_count} potions...\n")
    populate_map(grid, monster_count, health_count, place_boss=True, player_start=(0, 0))

    # Initialize player
    player = Player(player_name)

    # Main game loop
    while player.is_alive():
        print("\n📍 Current Map:")
        display_map(grid, player.position)
        print(f"\n🧍 {player.name} - Level: {player.level} | HP: {player.hp}")

        move = input("Move (W/A/S/D or type 'quit' to exit): ").strip().upper()
        if move == 'QUIT':
            print("👋 You left the adventure. See you next time, trainer!")
            break

        if move not in ['W', 'A', 'S', 'D']:
            print("Invalid input. Please use W, A, S, or D.")
            continue

        # Player movement
        player.move(move, size)
        x, y = player.position
        current_tile = grid[x][y]

        # Tile interaction logic
        if current_tile == 'M':
            if player.level >= 5:
                print("\n(⚠️) You're already super strong! Let's not bully little wild Pokémon 🐣")
                print("👉 Head north to face Mewtwo and become the Pokémon Champion! 💥")
            else:
                print("\n⚔️ A wild Pokémon appears! Prepare for battle! ⚔️")
                rock_paper_scissors(player)
                place_entity(grid, 'M', player.position)  # Respawn a new monster
            grid[x][y] = ' '

        elif current_tile == 'H':
            print("\n🍷 You found a potion lying in the grass!")
            player.heal(20)
            place_entity(grid, 'H', player.position)  # Respawn a new potion
            grid[x][y] = ' '

        elif current_tile == 'B':
            print("\n💥 You encountered the Legendary Pokémon: Mewtwo! 💥")
            if player.can_fight_boss():
                confirm = input("You are strong enough to challenge Mewtwo! Fight? (Y/N): ").strip().upper()
                if confirm == 'Y':
                    print("\n🌟 You defeated Mewtwo and became a true Pokémon Master! 🌟")
                    break
                else:
                    print("You ran away safely... 🏃💨")
            else:
                confirm = input("You're too weak to defeat Mewtwo now. Fight anyway? (Y/N): ").strip().upper()
                if confirm == 'Y':
                    player.take_damage(50)
                    print("Mewtwo was too powerful! You were blown away! (╥﹏╥)")
                    print("You need to grow stronger before facing Mewtwo again! 💪")
                else:
                    print("Wise choice... Get stronger and come back later!")
            place_entity(grid, 'B', player.position)  # Respawn Mewtwo
            grid[x][y] = ' '

        else:
            print("\n🌾 Nothing here... just some tall grass swaying in the breeze.")

    # Game over condition
    if not player.is_alive():
        print(f"\n💀 {player.name} has fainted... Game Over. (｡•́︿•̀｡)")
    else:
        print(f"\n🎊 {player.name} wins the game and becomes Champion of the Pokémon World! 🎊")

if __name__ == '__main__':
    main()