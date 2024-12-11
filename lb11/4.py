import os
from random import randint
import PySimpleGUI as sg

sg.theme("OrangeBrown")

layout = [
    [sg.Image(r"/Users/m1/Downloads/cat.png")],  # Исправленный путь
    [sg.Text("Границы чисел:", font="20px"),
     sg.InputText(font="20px", size=(15, None), key="min_val"),
     sg.Text(":", font="20px"),
     sg.InputText(font="20px", size=(15, None), key="max_val")],
    [sg.Button("Давай, делай!!!", button_color="orange", font="20px", size=(15, 1))],
    [sg.Input(key="res", font="20px", size=(30, 1), readonly=True)]
]

window = sg.Window("Meow", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Давай, делай!!!":
        try:
            min_val = int(values["min_val"])
            max_val = int(values["max_val"])

            if min_val > max_val:
                sg.popup_error("Ну ты чо, начало не может быть меньше конца:0")
                continue

            random_number = randint(min_val, max_val)
            window["res"].update(random_number)
        except ValueError:
            sg.popup_error("Пожалуйста, можно адекватнее границы:0")

window.close()