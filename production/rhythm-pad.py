import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS_COL = [board.A3, board.D4, board.D5, board.D0]
PINS_ROW = [board.D1, board.D2, board.D3]
keyboard.diode_orientation = DiodeOrientation.DIODE_COL2ROW

keyboard.keymap = [
        [
        KC.NP7, KC.NP8, KC.NP9,
        KC.NP4, KC.NP5, KC.NP6, KC.NP0,
        KC.NP1, KC.NP2, KC.NP3,
    ]
]

if __name__ == '__main__':
    keyboard.go()