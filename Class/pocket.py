class Pokemon:
    def __init__(self, element : str, name : str, health : float, attack : float, defence : float):
        self.element = element
        self.name = name
        self.health = health
        self.attack = attack
        self.defence = defence

def typing(object : Pokemon, subject : Pokemon):
    match object:
        case "grass":
            return 1
        case "water":
            return 1
        case "fire":
            return 1
        case "eletric":
            return 1
        

pokemon_1 = Pokemon("electric", "Pikachú", 100.0, 10.0, 0.0)

pokemon_2 = Pokemon("grass", "Boo", 100.0, 1.0, 4.0)

def strike(attacker : Pokemon, target : Pokemon):
    print(f"{attacker} attackerade {target}")
    return 50 * (attacker.attack / target.defence) * typing(attacker.element, target.element)


print(strike(pokemon_1, pokemon_2))