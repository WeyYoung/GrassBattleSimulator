import random

def rock_paper_scissors(player):
    """
    A simple rock-paper-scissors mini-game for battling wild Pokémon.
    - Win: Player levels up.
    - Lose: Player takes 20 HP damage.
    - Tie: Replay until there's a result.
    """
    choices = ['rock', 'paper', 'scissors']
    rules = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    while True:
        player_choice = input("Choose rock, paper, or scissors: ").strip().lower()

        # Input validation
        if player_choice not in choices:
            print("❌ Invalid input. Please type 'rock', 'paper', or 'scissors'.")
            continue

        monster_choice = random.choice(choices)
        print(f"👾 The wild Pokémon chose: {monster_choice}")

        if player_choice == monster_choice:
            print("🤝 It's a tie! Try again!\n")
            continue
        elif rules[player_choice] == monster_choice:
            print("🎉 You won the battle! Your Pokémon is growing stronger! 💪\n")
            player.gain_level()
            return True
        else:
            print("💥 You lost the battle! Stay strong, trainer!\n")
            player.take_damage(20)
            return False


if __name__ == '__main__':
    from player import Player

    player = Player("TestPlayer")
    rock_paper_scissors(player)