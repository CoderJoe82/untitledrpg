class Entity():
    def __init__(self):
        self.name = "Entity"
        self.hp = 100
        self.max_hp = 100
        self.stats = {
            "strength" : 10,
            "dexterity" : 10,
            "intellect" : 10,
            "wisdom" : 10,
            "constitution" : 10,
            "charisma" : 10,
            "faith" : 10
        }

    def take_damage(self, amount):
        damage_taken = amount
        self.hp -= damage_taken

    def is_alive(self):
        if self.hp <= 0:
            return False
        return True