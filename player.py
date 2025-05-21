class Player:
    def __init__(self, name):
        """
        Initialize player attributes.
        """
        self.name = name
        self.level = 1           # Start at level 1
        self.max_hp = 100        # Max HP
        self.hp = self.max_hp    # Current HP
        self.position = (0, 0)   # Starting position on the map

    def move(self, direction, map_size):
        """
        Move the player in the given direction (W/A/S/D).
        Prevent going out of bounds.
        """
        row, col = self.position
        if direction == 'W' and row > 0:
            self.position = (row - 1, col)
        elif direction == 'S' and row < map_size - 1:
            self.position = (row + 1, col)
        elif direction == 'A' and col > 0:
            self.position = (row, col - 1)
        elif direction == 'D' and col < map_size - 1:
            self.position = (row, col + 1)

    def gain_level(self):
        """
        Increase player's level by 1, max level is 5.
        """
        if self.level < 5:
            self.level += 1
            print(f"🌟 {self.name} leveled up to Lv.{self.level}! You're getting stronger! 💪✨")

    def take_damage(self, amount):
        """
        Reduce HP when taking damage.
        """
        self.hp -= amount
        print(f"💥 Ouch! {self.name} took {amount} damage! Current HP: {self.hp} 💔")

    def heal(self, amount):
        """
        Restore HP (but not above max HP).
        """
        self.hp = min(self.hp + amount, self.max_hp)
        print(f"💖 {self.name} found a potion and recovered +{amount} HP! Now at {self.hp} HP! ✨")

    def is_alive(self):
        """
        Check if the player is still alive (HP > 0).
        """
        return self.hp > 0

    def can_fight_boss(self):
        """
        Check if the player is strong enough to fight the boss (Lv. 5).
        """
        return self.level >= 5