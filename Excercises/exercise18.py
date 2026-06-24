import FreeSimpleGUI as sg

label1 = sg.Text("Enter feet:")
label2 = sg.Text("Enter inches:")

input_feet = sg.Input(key = "feet")
input_inches = sg.Input(key = "inches")

convert_button = sg.Button("Convert")
label3 = sg.Text()

window = sg.Window("Convertor", layout = [[label1, input_feet],
                                          [label2, input_inches],
                                          [convert_button, label3]])
while True:
    event, values = window.read()
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])
    meters = (feet * 0.3048) + (inches * 0.0254)
    label3.update(meters)
    if event == sg.WIN_CLOSED:
        break
