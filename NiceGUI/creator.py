from nicegui import ui

import random

first = [
    "James ", "Michael ", "Robert ", "john ", "David ", "William ", "Richard ", "Joseph ", "Thomas ", "Christopher ", "Charles ", "Daniel ", "Matthew ", "Peter ", "Jane "
]

last = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Griffith", "Gonzales", "Wilson", "Doe"
]

gender = ["female", "female", "male", "female", "forgor"]

race = ["human", "dwarf", "elf"]

job = ["blacksmith", "town drunk", "class clown", "jester", "Hermit", "Brewer", "incarerated", "undertaker", "executionarer", "warrior", "mercenary", "entertainer", "diplomat"]

trait = ["teetotaler", "narcoleptic", ]

life_expec = 1

for i in range(1):
    random.shuffle(first)
    random.shuffle(last)
    random.shuffle(gender)
    random.shuffle(job)
    random.shuffle(trait)

char_name = (first[0] + last[0])
char_gender = (gender[0])
char_race = (race[0])
if char_race == "dwarf":
    life_expec = 3.5
elif char_race == "elf":
    life_expec = 7.5
else:
    pass
char_age = round(random.random()*100*life_expec, 1)
char_job = (job[0])
char_trait1 = (trait[0])
char_trait2 = (trait[-1])

with ui.column().classes("self-center"):
    ui.label("You cant change or randomize!")
    ui.label("Name: " + char_name)
    ui.label("Gender: " + char_gender)
    ui.label("Race: " + char_race)
    ui.label("Age: " + str(char_age))
    ui.label("Occupation: " + char_job)
    ui.label("Trait: " + char_trait1)
    ui.label("Triat: " + char_trait2)

ui.run(native=True)