import random

score = 0
opscore = 0

alternativ=["sten", "sax", "påse"]



while score < 3 and opscore < 3:
    print("Sten, sax, påse")
    roshambo= input().lower()
    roshambeu = random.choice(alternativ)
    if roshambo == roshambeu:
        print("Oavgjort", roshambo, "mot", roshambeu)
    elif roshambo == "sten" and roshambeu == "sax":
        print("Vinst", roshambo, "mot", roshambeu )
        score = score + 1
    elif roshambo == "sten" and roshambeu == "påse":
        print("Förlust", roshambo, "mot", roshambeu)
        opscore = opscore + 1
    elif roshambo == "sax" and roshambeu == "påse":
        print("vinst", roshambo, "mot", roshambeu)
        score = score + 1
    elif roshambo == "sax" and roshambeu == "sten":
        print("Förlust", roshambo, "mot", roshambeu)
        opscore = opscore + 1
    elif roshambo =="påse" and roshambeu == "sten":
        print("vinst", roshambo, "mot", roshambeu)
        score = score + 1
    elif roshambo =="påse" and roshambeu =="sax":
        print("Förlust", roshambo, "mot", roshambeu)
        opscore = opscore + 1
    else:
        print("Inte möjligt")
    
    print(score, "/", opscore)

if score == 3:
    print("Vinnare")
elif opscore == 3:
    print ("Nolla")