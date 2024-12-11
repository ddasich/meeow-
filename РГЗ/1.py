import PySimpleGUI as sg

sg.theme("DarkBrown")

l = [
    [sg.Text("Введите слово:", font="20px"),
     sg.InputText(font="20px", size=(25, None), key="input_word")],
    [sg.Button("Искать", button_color="orange", font="20px", size=(15, 1)),
     sg.Button("", button_color="DarkBrown", font="20px", key="show_image", size=(1, 1))],
    [sg.Text("Результат:", font="20px"),
     sg.Multiline(key="output", font="20px", size=(80, 5), disabled=True)]
]

window = sg.Window("Словарь", l)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Искать":
        word = values["input_word"].strip()
        window["output"].update("")
        found = False

        if not word:
            sg.popup_error("Тут ничо нет")
        else:
            with open(r'/Users/m1/Desktop/file.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    if line.lower().startswith(word.lower()):
                        definition = line[len(word):].strip()
                        window["output"].update(f"{definition}")
                        found = True
                        break

            if not found:
                sg.popup_error(f"Слово '{word}' не найдено.")

    if event == "show_image":
        image_path = '/Users/m1/Desktop/mem-2.png'
        image_l = [[sg.Image(filename=image_path)],
                        [sg.Button("Закрыть")]]

        image_window = sg.Window("А вот так вот:0", image_l)

        while True:
            img_event, img_values = image_window.read()
            if img_event == sg.WIN_CLOSED or img_event == "Закрыть":
                break

        image_window.close()

window.close()