import keypad
import board
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from supervisor import ticks_ms

def check_press(previous):
    new_tick = ticks_ms()
    if new_tick < previous:
        # Allow for wrap around at 2^29
        new_tick += 536870912
    return (new_tick - previous) < 1000 # 1000ms = 1 second

time.sleep(1)
# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# 8 Rows 5 Columns. Note rows are not in order
km = keypad.KeyMatrix(
    row_pins=(board.GP5, board.GP6, board.GP7, board.GP9, board.GP10, board.GP8, board.GP11, board.GP12),
    column_pins=(board.GP0, board.GP1, board.GP2, board.GP3, board.GP4),
)

key_ZX81 = {0 : Keycode.FIVE,
            1 : Keycode.FOUR,
            2 : Keycode.THREE,
            3 : Keycode.TWO,
            4 : Keycode.ONE,

            5 : Keycode.T,
            6 : Keycode.R,
            7 : Keycode.E,
            8 : Keycode.W,
            9 : Keycode.Q,

            10 : Keycode.SIX,
            11 : Keycode.SEVEN,
            12 : Keycode.EIGHT,
            13 : Keycode.NINE,
            14 : Keycode.ZERO,

            15 : Keycode.Y,
            16 : Keycode.U,
            17 : Keycode.I,
            18 : Keycode.O,
            19 : Keycode.P,

            20 : Keycode.V,
            21 : Keycode.C,
            22 : Keycode.X,
            23 : Keycode.Z,
            24 : Keycode.LEFT_SHIFT,

            25 : Keycode.G,
            26 : Keycode.F,
            27 : Keycode.D,
            28 : Keycode.S,
            29 : Keycode.A,

            30 : Keycode.H,
            31 : Keycode.J,
            32 : Keycode.K,
            33 : Keycode.L,
            34 : Keycode.ENTER,

            35 : Keycode.B,
            36 : Keycode.N,
            37 : Keycode.M,
            38 : Keycode.PERIOD,
            39 : Keycode.SPACE,
           }
# Create an event we will reuse
event = keypad.Event()

#print ("Starting...")
shift = False           # True if shift pressed
comma = False           # True if comma sent instead of shift period

'''
 To generate a non Sinclair key from a Sinclair keyboard:
 1. Shift is pressed without another key
 2. Shift is released, without another key being pressed
 3. Within 1 second shift is pressed again
 4. Shift is released, without another key being pressed
 5. Within 1 second a numeric key is pressed without shift being pressed
'''
double_count = 0        # Counts shift press-release pairs that are in time
double_tick = 0         # millisecond tick of the last time that the shift key was released
double_converted = 0    # The converted key code sent as a result of a double press
double_original = 0     # The original key press that triggered the double press

while True:
    if km.events.get_into(event):
        # Convert the event to a specific key
        key_code = key_ZX81.get(event.key_number, 0)

        if key_code != 0:
            if event.pressed:
                # Check for double shifts to generate function keys
                if key_code == Keycode.LEFT_SHIFT:
                    shift = True
                    if double_count:
                        # check that the second shift was in time
                        if not check_press(double_tick):
                            double_count = 0
                    double_count += 1
                    kbd.press(Keycode.LEFT_SHIFT)
                else:
                    # Need to translate shift period to comma
                    if key_code == Keycode.PERIOD and shift:
                        comma = True
                        # Release shift and send comma
                        kbd.release(Keycode.LEFT_SHIFT)
                        kbd.press(Keycode.COMMA)
                    else:
                        if double_count > 1:
                            # Has another key been pressed in time?
                            if check_press(double_tick):
                                # Convert function keys 1 - 9 to F1 - F9. 0 maps to Escape
                                if key_code >= Keycode.ONE and key_code <= Keycode.ZERO:
                                    if key_code == Keycode.ZERO:
                                        double_converted = Keycode.ESCAPE
                                    else:
                                        double_converted = Keycode.F1 + (key_code - Keycode.ONE)
                                    double_original = key_code
                                    key_code = double_converted
                        # Ensure that the key press is always sent on
                        kbd.press(key_code)

                    # Another key has been pressed, so double shift ends
                    double_count = 0
            else:   # Key release
                if key_code == Keycode.LEFT_SHIFT:
                    if double_count:
                        double_tick = ticks_ms()
                    shift = False
                    kbd.release(Keycode.LEFT_SHIFT)
                if key_code == Keycode.PERIOD and comma:
                    comma = False
                    kbd.release(Keycode.COMMA)
                    #Restore the shift state if needed
                    if shift:
                        kbd.press(Keycode.LEFT_SHIFT)
                else:
                    if key_code == double_original:
                        kbd.release(double_converted)
                        double_original = 0
                    else:
                        kbd.release(key_code)
