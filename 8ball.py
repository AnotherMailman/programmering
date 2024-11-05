import random

ja=["Ja","Japp","värkar så"]
otydligt=["Okej","testa igen","Fesök igen","Kanske"]
nej=["Nej","Nope","nix"]

r = random.randint(1,3)

if r == 1:
    print(random.choice(ja))
elif r == 2:
    print(random.choice(otydligt))
else:
    print(random.choice(nej))

