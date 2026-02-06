import PySimpleGUI as sg 

layout = [[sg.Button('Klik saya')]]

Window = sg.Window('contoh program mysimplegui', layout)

while True:
    event, values = Window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'klik saya':
        print('tombol diklik')
        
Window.close()