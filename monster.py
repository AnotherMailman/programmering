class Monster:
    def __init__(self, name : str, health : str, attack_power : str):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target : str):
        print(f"{self} attackerade {target}")


class Dragon(Monster):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

class Vampire(Monster):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

class Zombie(Monster):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)
