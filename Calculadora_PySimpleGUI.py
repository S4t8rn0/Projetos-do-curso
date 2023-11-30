import PySimpleGUI as sg

layout= [
    [sg.Text('Calculadora')],
    [sg.Text('Digite um número'), sg.InputText()],
    [sg.Text('Digite outro número'), sg.InputText()],
    [sg.Button('Somar'), sg.Button('Subtrair')]
]
window = sg.Window('Calculadora', layout)

while True:
    event, values= window.read()

    if event == sg.WIN_CLOSED:
        sg.popup_yes_no('Tem certeza que deseja fechar?')
        if event in ('Sim'):
            print('Ok')
            break
        if event in('não'):
            sg.WIN_CLOSED
    
    if event in ('Somar'):
        result= int(values[0]) + int(values[1])
        sg.popup(f'O valor da soma foi {result}.')

    if event in('Subtrair'):
        result= int(values[0]) - int(values[1])
        sg.popup(f'O valor da subtração foi {result}.')

window.close()