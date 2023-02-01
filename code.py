import keypad
import board
import usb_hid
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

time.sleep(1)
# Set up a keyboard device.
kbd = Keyboard(usb_hid.devices)

# 8 Rows 5 Columns
km = keypad.KeyMatrix(
    row_pins=(board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12),
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
while True:
    if km.events.get_into(event):
        # Convert the event to a specific key
        key_code = key_ZX81.get(event.key_number, 0)
        
        if key_code != 0:
            if event.pressed:
                kbd.press(key_code)
            else:
                kbd.release(key_code)
