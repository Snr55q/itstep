
class Chatacter:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def attack(self):
        return self.health

class Hero(Chatacter):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        return self.weapon

class Enemy(Chatacter):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    def damage(self):
        return self.damage

hero = Hero("Moder", 100, 100)
enemy = Enemy("Hellhacker", 150, 333)

print(hero.attack())
print(enemy.attack())