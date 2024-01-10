#Code will go here
import PySimpleGUI as sg

def layouts(num):
    if num == 1:
        return [
        [sg.Text("Select a text file:")],
        [sg.Input(key='file_path'), sg.FileBrowse()],
        [sg.Button('Load'), sg.Button('Exit')],
        [sg.Text("Items in the file:")],
        [sg.Listbox(values=[], size=(30, 5), key='listbox')]
    ]
def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
        return [line.strip() for line in content]
    except FileNotFoundError:
        sg.popup_error(f"File not found: {file_path}")
        return []

window = sg.Window('Text File Reader', layouts(1))
while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'Load':
            file_path = values['file_path']
            items = read_text_file(file_path)
            window['listbox'].update(values=items)

window.close()