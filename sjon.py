import random

sea = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King',
'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King'
]
player1 = []
player2 = []
player3 = []
player4 = []

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

remain = 52

def take_card(from_player, to_player, card):
    if from_player == to_player:
        return
    



while remain >= 0:
    print("player2 turn")
    pick2 = random.choice(player2)
    ask = random.randrange(1, 4)
    take_card(2, ask, pick2)

    print("player3 turn")
    pick3 = random.choice(player3)
    ask = random.randrange(1, 4)
    take_card(3, ask, pick3)



    print("player4 turn")
    pick4 = random.choice(player4)


    print("Your turn")
    print("Pick a player")
    ask = input().lower()

    match ask:
        case "player2":
            print("a")
        case "player3":
            print("b")
        case "player4":
            print("c")
        case _:
            print("d")