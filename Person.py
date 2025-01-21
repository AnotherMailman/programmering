number = []

person = input()

number = list(person)

if "-" in number:
    number.remove("-")
if "+" in number:
    number.remove("+")

total = 0

for i in range(len(number) - 1):
    if i % 2 == 0:
        x = int(number[i])*2
        if(x > 9):
            total += int(str(x)[0])
            total += int(str(x)[1])
        else: 
            total += x
    else:
        total += int(number[i])


control = (10 - (total % 10)) % 10

if str(control) == number[-1]:
    print("Kontrol numbret är korrekt")
else:
    print("Kontrol numbret är inkorrekt")

print(number[-1])