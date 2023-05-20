import PySimpleGUI as sg

layout = [
    [sg.Text('Qual é o seu nome')],
    [sg.Input(key='input_name')],
    [sg.Text(size=(40, 1), key='output_name')],
    [sg.Button('OK'), sg.Button('Quit')],
]

window = sg.Window('Qual é o seu nome', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    window['output_name'].update("Hello" + values['input_name'])

window.close()
