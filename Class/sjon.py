import random

sea = ['ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king',
'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king',
'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king',
'ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king'
]

player1 = []
player2 = []
player3 = []
player4 = []
players = [player1, player2, player2, player4
]

print("Shuffling deck")

random.shuffle(sea)

print("Cards being dealt")

for i in range(7):
    player1.append(sea[0])
    sea.pop(0)
for i in range(7):
    player2.append(sea[0])
    sea.pop(0)
for i in range(7):
    player3.append(sea[0])
    sea.pop(0)
for i in range(7):
    player4.append(sea[0])
    sea.pop(0)

remain = len(sea)

def take_card(from_player, to_player, card):
    print(from_player, "asked", to_player, "if they had any", card)
    if from_player == to_player:
        return (from_player, " hurt itself in its confusion")
        
    elif card == to_player:
        amount = 0
        while card in to_player:
            from_player.append(card)
            to_player.pop(card)
            amount += 1
            print(from_player, " took ", amount, card, " from ", to_player)
    
    elif card in sea:
        from_player.append(sea[0])
        sea.pop(0)
        print("Go fish ", from_player, " found a ", from_player[-1])
    
    else: print(from_player, "hurt itself in its own confusion")


while len(player1) != 0 and len(player2) != 0 and len(player3) != 0 and len(player4) != 0:
    print("player2 turn")
    ask = random.choice(players)
    pick = random.choice(player2)
    take_card(player2, ask, pick)

    print("player3 turn")
    ask = random.choice(players)
    pick = random.choice(player3)
    take_card(player3, ask, pick)

    print("player4 turn")
    ask = random.choice(players)
    pick = random.choice(player4)
    take_card(player4, ask, pick)

    print("player1 hand ", player1)
    print("player2 hand ", player2)
    print("player3 hand ", player3)
    print("player4 hand ", player4)

    print("Your turn")
    print("Pick a player")
    ask = input().lower()
    pick = input().lower()
    take_card(player2, ask, pick)