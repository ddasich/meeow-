import PySimpleGUI as sg
import random

c_image = [[sg.Image(r"/Users/m1/Downloads/Архив/bio.png")]]
c_input = [[sg.Text("Введите количество бактерий:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="micro")],
           [sg.Text("Количество секунд:", font="Arial 20"), sg.Input(font="Arial 20", size=(5, 0), key="count")],
           [sg.Text("Результат:", font="Arial 20"), sg.Input(font="Arial 20", readonly=True, size=(5, 0), key="res")],
           [sg.Button("Рассчитать", font="Arial 20")]]

layout = [
    [sg.Column(c_image), sg.VSeperator(), sg.Column(c_input, justification='right')]
]

window = sg.Window("Калькулятор бактерий", layout)

while 1:

    event, value = window.read()

    if event == sg.WIN_CLOSED:
        break

    micro = value["micro"]
    count = value["count"]
    res = 0

    if micro.isdigit() and count.isdigit():
        micro = int(micro)
        count = int(count)
    else:
        window["res"].update(res)
        continue
    res = micro

    for _ in range(count):
        b = random.randint(0, 4)
        res = res * micro + b

    if event == "Рассчитать":
        window["res"].update(res)


window.close()

