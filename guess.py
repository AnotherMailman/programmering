import random

svar = random.randrange(1,101)

print(svar)

Ratt = 0
while Ratt <= 1:
    print("Gissa ett number mellan 1 och 100")
    val = input()

    try:
        val = int(val)
    except:
        print("Inte ett number")
        continue

    if val == svar:
        print("Rätt!")
        Ratt += 1
        break
    elif val < svar:
        print("Talet är högre")
    elif val > svar:
        print("Talet är lägre")
    else: print("Inte ett number")