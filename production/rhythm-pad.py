import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.col_pins = [board.A3, board.D4, board.D5, board.D6]
keyboard.row_pins = [board.D7, board.D8, board.D9]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
        [
        KC.N7, KC.N8, KC.N9, KC.NO,
        KC.N4, KC.N5, KC.N6, KC.N0,
        KC.N1, KC.N2, KC.N3, KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()
