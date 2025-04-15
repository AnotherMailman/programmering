from nicegui import ui

def addition():
    result_label.text = num_1.value + num_2.value

def subtraction():
    result_label.text = num_1.value - num_2.value

def multiplication():
    result_label.text = num_1.value * num_2.value

def division():
    result_label.text = num_1.value / num_2.value

with ui.column().classes("self-center"):
    ui.label("Calculator").classes("text-2xl")
    num_1 = ui.number(label="Nummer 1")
    num_2 = ui.number(label="Nummer 2")
    with ui.row():
        ui.button('+', on_click=lambda: addition())
        ui.button('-', on_click=lambda: subtraction())
        ui.button('*', on_click=lambda: multiplication())
        ui.button('/', on_click=lambda: division())

    result_label = ui.label("")

ui.run(native=True)