import functions
import FreeSimpleGUI as sg



label = sg.Text("Add a ToDo")
add_input = sg.Input()
add_button = sg.Button("Add")

window = sg.Window("My Todo App",layout=[[label],[add_input,add_button]])
window.read()
window.close()