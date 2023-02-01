# ZX81_USB_KBD
This CircuitPython code for the Raspberry Pi Pico 2040 allows a [Sinclair ZX81](https://en.wikipedia.org/wiki/Sinclair_ZX81) keyboard matrix to be used as the basis for a USB keyboard that can be used in Linux or MS Windows.

**A new keyboard matrix and a 3d print of the ZX81 case was used, so no ZX81 were harmed in the production of this project**

## Connecting the keyboard membrane
The ZX81 keyboard membrane connects through one 5 way and one 8 way Connfly Ds1020 connector. These can typically be cheaply sourced on ebay.

The 13 lines from the membrane (5 columns, 8 rows) are routed to the first 13 GPIO lines on a Raspberry Pico. This can be simply achieved by mounting the Ds1020 on Veroboard, with PCB headers then taking the output to the Pico. I am sure those with more hardware skills than me could easily fabricate a dedicated PCB, including mounting the Pico 2040.

No diodes are used in the circuit. The keyboard functions well without them.

## Installation
The project uses CircuitPython, and the Adafruit Matrix Keypad library. Instructions for installation can be found [here](https://learn.adafruit.com/matrix-keypad/python-circuitpython).

The code must run automatically on power up. In addition the usual auto-mount of the CIRCUITPY drive should be disabled.

`boot.py` is used to prevent automount. Using `code.py` as the filename for the code file ensures that the code will run on power on (see [here](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial)).

Both `boot.py` and `code.py` should be copied to the root directory of the CIRCUITPY drive.

## Known issues
The keyboard has been tested with several ZX81 emulators. On most emulators the keyboard functions correctly. On two emulators [EightyOne](https://github.com/charlierobson/EightyOne) and Spud81 shift period is parsed as > rather than comma. This means that the keyboard cannot currently be used to create a comma for those emulators.

A later version of this code may address this by checking the shift status and explicitly sending a comma when shift and period is pressed.

# Why?
The ZX81 keyboard is not the greatest for fast typing. Also it only posesses a sub-set of the keys needed to drive a modern OS. The reasons for doing this were:
1) It can be fun to control a ZX81 emulator with an authentic keyboard.
2) It makes a change for me to code for a real time application in Python, rather than C

It is also amusing that a $3 dollar part, running at 125MHz, with 264kB of RAM and 2MB of Flash, is being used to control the keyboard of the ZX81, when originally the ZX81 processor ran at 3.25MHz, and the base ZX81 was initially sold with 1kB of RAM!
