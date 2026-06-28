import FreeSimpleGUI as sg
from convert import convert
sg.theme('Black')
label1 = sg.Text("Enter feet:")
label2 = sg.Text("Enter inches:")

input_feet = sg.Input(key = "feet")
input_inches = sg.Input(key = "inches")

convert_button = sg.Button("Convert")
label3 = sg.Text()
exit_button = sg.Button("Exit")
window = sg.Window("Convertor", layout = [[label1, input_feet],
                                          [label2, input_inches],
                                          [convert_button,exit_button, label3]])
while True:
    try:
        event, values = window.read()
        print(event, values)
        feet = float(values["feet"])
        inches = float(values["inches"])
        meters = convert(feet, inches)
        label3.update(meters)
    except ValueError:
        sg.popup_error("Please enter a number")

    if event == "sg.WIN_CLOSED" or event == "Exit":
        break
