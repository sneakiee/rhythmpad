import board
import neopixel
import time

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.col_pins = [board.A3, board.D4, board.D5, board.D6]
keyboard.row_pins = [board.D7, board.D8, board.D9]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

LED_TOP_PIN = board.A0
LED_BOTTOM_PIN = board.D10
TOP_LEDS = 3
BOTTOM_LEDS = 3

strip_top = neopixel.NeoPixel(LED_TOP_PIN, TOP_LEDS, brightness=1.0, auto_write=False, pixel_order=(1, 0, 2))
strip_bottom = neopixel.NeoPixel(LED_BOTTOM_PIN, BOTTOM_LEDS, brightness=1.0, auto_write=False, pixel_order=(1, 0, 2))

FIXED_COLOR = (255, 255, 255)
FADE_TIME = 0.5

led_map = {
    0: ([0], []),
    1: ([1], []),
    2: ([2], []),
    3: ([0], [0]),
    4: ([1], [1]),
    5: ([2], [2]),
    6: ([2], [2]),
    7: ([], [0]),
    8: ([], [1]),
    9: ([], [2]),
}

active_keys = {}

def update_leds():
    now = time.monotonic()

    # Clear LEDs
    for i in range(TOP_LEDS):
        strip_top[i] = (0, 0, 0)
    for i in range(BOTTOM_LEDS):
        strip_bottom[i] = (0, 0, 0)

    keys_to_remove = []
    for key_index, press_time in active_keys.items():
        elapsed = now - press_time
        if elapsed >= FADE_TIME:
            keys_to_remove.append(key_index)
            continue

        brightness = 1 - (elapsed / FADE_TIME)
        color = tuple(int(c * brightness) for c in FIXED_COLOR)

        top_idxs, bottom_idxs = led_map.get(key_index, ([], []))
        for i in top_idxs:
            strip_top[i] = color
        for i in bottom_idxs:
            strip_bottom[i] = color

    for key in keys_to_remove:
        del active_keys[key]

    strip_top.show()
    strip_bottom.show()

keyboard.keymap = [
        [
        KC.N7, KC.N8, KC.N9, KC.NO,
        KC.N4, KC.N5, KC.N6, KC.N0,
        KC.N1, KC.N2, KC.N3, KC.NO,
    ]
]

def after_matrix_scan(kbd):
    pressed = kbd.matrix_update.pressed
    if pressed:
        for idx, is_pressed in enumerate(pressed):
            if is_pressed and idx not in active_keys:
                active_keys[idx] = time.monotonic()

    update_leds()

keyboard.after_matrix_scan = after_matrix_scan

if __name__ == '__main__':
    keyboard.go()
