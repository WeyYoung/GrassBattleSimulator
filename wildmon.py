class WildMon:
    def __init__(self, mon_type):
        """
        Initialize a wild monster.
        :param mon_type: 'M' for regular wild monster, 'B' for Boss.
        """
        self.type = mon_type

    def is_boss(self):
        """
        Check if this monster is the Boss.
        """
        return self.type == 'B'

    def get_name(self):
        """
        Return display name of the monster.
        """
        return "Mewtwo 👑" if self.is_boss() else "Wild Pokémon 🐾"

    def get_intro(self):
        """
        Return battle introduction text for the monster.
        """
        if self.is_boss():
            return "💥 A mighty legendary Pokémon appears... It's Mewtwo! Prepare for the ultimate battle! 💥"
        else:
            return "⚔️ A wild Pokémon blocks your path! Get ready to fight! 🐾"