import PySimpleGUI as sg

# Define the main menu layout
def create_main_menu():
    return [[sg.Text('Main Menu', font=('Helvetica', 16))],
            [sg.Button('Start Game')],
            [sg.Button('Exit')]]


# Define the layout for the chessboard
def create_chess_game():
    board_layout = []
    for row in range(8):
        row_layout = []
        for col in range(8):
            color = 'firebrick4' if (row + col) % 2 == 0 else 'wheat'
            piece = 'images/wB.png'
            button = sg.Button(size=(4, 3), image_filename=piece, button_color=('tomato', color), key=(row, col))
            row_layout.append(button)
        board_layout.append(row_layout)
    return [[sg.Menu([['File', ['Return to Menu', 'Exit']]])]] + board_layout


# Function to create a window
def create_window(layout):
    return sg.Window('Chess Game', layout)

# Start with the main menu
layout = create_main_menu()
window = create_window(layout)

# Event loop
while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Start Game':
        window.close()
        layout = create_chess_game()
        window = create_window(layout)
    elif event == 'Return to Menu':
        window.close()
        layout = create_main_menu()
        window = create_window(layout)

window.close()
