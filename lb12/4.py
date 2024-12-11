from random import randint
import PySimpleGUI as sg


def to_signed_binary(number, bits=8):
    if number >= 0:
        real = bin(number)[2:].zfill(bits)
        rev = real
        dlc = real
    else:
        real = bin((1 << bits) + number)[2:].zfill(bits)
        rev = ''.join('1' if bit == '0' else '0' for bit in real)
        dlc = bin(int(rev, 2) + 1)[2:].zfill(bits)

    return real, rev, dlc


sg.theme("Orange")

layout = [
    [sg.Text("Введите число:", font="20"),
     sg.InputText(font="20", size=(10, None), key="number1")],
    [sg.Button("Узнать значения", button_color="green", font="20", size=(20, 1))],
    [sg.Text("Прямой код:", font="20"),
     sg.InputText(key="real1", font="20", size=(25, 1), disabled=True),
     sg.Text("Обратный код:", font="20"),
     sg.InputText(key="rev1", font="20", size=(25, 1), disabled=True),
     sg.Text("Дополнительный код:", font="20"),
     sg.InputText(key="dlc1", font="20", size=(25, 1), disabled=True)]
]

window = sg.Window("Значения двоичного кода", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Узнать значения":
        try:
            number = int(values["number1"])
            if -128 <= number <= 127:
                real, rev, dlc = to_signed_binary(number)
                window["real1"].update(real)
                window["rev1"].update(rev)
                window["dlc1"].update(dlc)
            else:
                sg.popup_error("Введите число в диапазоне -128 до 127")
        except ValueError:
            sg.popup_error("Введите корректное целое число")

window.close()