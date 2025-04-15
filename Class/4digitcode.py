import random

code = [0, 0, 0, 0,]

testing = [0, 0, 0, 0,]

Tu = True

for x in range(3):
    code [x] = random.randrange(1,9)
print(code)
while Tu == True:
    print("gissa 4 number koden")
    guess = (input)
    test = list(guess)
    print(test)
    if test == code:
        print("You guessed the code right!")
        tu = False
        break
    for y in range(3):
        if test[y] == code[y]:
            print (y + " is a green!")
        elif test[y] in code:
            print(y + "is a yellow...")
        else:
            print(y + "is a red..")