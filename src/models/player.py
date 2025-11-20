class Player():
    def __init__(self):
        self.name = "Hero"
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intellect = 10
        self.wisdom = 10
        self.charisma = 10
        self.faith = 10
        self.hp = self.constitution * 10
        self.max_hp = self.constitution * 10
        self.mana = self.intellect * 10
        self.max_mana = self.intellect * 10