import PySimpleGUI as sg 

sg.theme('BluePurple')

layout = [[sg.Text('your typed chars appears here:'), sg.Text(size=(15,1), key='-Output-')],[sg.Input(key='-IN-')], [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Patter 2B', layout)

while True: 
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break 
    if event == 'show': 
        window['-Output'].update(values['-IN-'])
        
window.close()