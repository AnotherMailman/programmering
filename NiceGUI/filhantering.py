from nicegui import ui

target = "Alex"

def targetalex():
  target = "alex"
def targetemma():
  target = "emma"
def targetjonas():
  target = "jonas"
konversation = []
i = 0

document = "C:\Programmering\NiceGUI\konversation"

with ui.column().classes("self-center"):
  ui.button("Alex", on_click=lambda: targetalex())
  ui.button("Emma", on_click=lambda: targetemma())
  ui.button("Jonas", on_click=lambda: targetjonas())

f = open(document, "r", encoding="utf-8")
new_f = open("ny " + document, "w", encoding="utf-8")

for line in f: 
  name = line.split(":")[0]

  if name != target:
    new_f.write(line)

f.close()
new_f.close()

ui.run(native=True)