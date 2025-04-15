def addition(x,y):
    return x+y
def subtraktion(x,y):
    return x-y
def multiplikation(x,y):
    return x*y
def division(x,y):
    return x/y

print("Välkommen tll miniräknaren")
print("Mata in 1 tal")
tal1=int(input())
print("Mata in ett annat tal")
tal2=int(input())
print("1 för addition, 2 för subtraktion, 3 för multiplikation, 4 för division")
Arithmetic=int(input())
if Arithmetic==1:
    print(addition(tal1, tal2))
elif Arithmetic==2:
    print(subtraktion(tal1, tal2))
elif Arithmetic==3:
    print(multiplikation(tal1, tal2))
elif Arithmetic==4:
    print(division(tal1, tal2))
else: print("ogiltig val")