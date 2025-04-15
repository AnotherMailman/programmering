import datetime

print("Ange start året")
startardatum = int(input())
print("Ange start månaden")
startmanaddatum = int(input())
print("Ange start dagen")
startdagdatum = int(input())
print("Ange slut året")
slutardatum = int(input())
print("Age slut månaden")
slutmanaddatum = int(input())
print("Ange slut dagen")
slutdagdatum = int(input())
print("Ange mätarens nivå i starten")
matarnivastart = int(input())
print("Ange mätarens niva i slutet")
matarnivaslut = int(input())
print("Ange priset på kilowatt per timmen i öre")
oreperkwh = int(input())
print("Ange priset för el i huset per dag i öre")
oreperdag = int(input())

startdatum = datetime.datetime(startardatum, startmanaddatum, startdagdatum)
slutdatum = datetime.datetime(slutardatum, slutmanaddatum, slutdagdatum)

total = ((((slutdatum - startdatum).days * oreperdag) + ((matarnivaslut - matarnivastart) * oreperkwh)) * 1.25) / 100

print("Det kommer kosta " + str(total) + " kronor")