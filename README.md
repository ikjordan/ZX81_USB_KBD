# ZX81_USB_KBD
This CircuitPython code for the Raspberry Pi Pico 2040 allows a [Sinclair ZX81](https://en.wikipedia.org/wiki/Sinclair_ZX81) keyboard matrix to be used as the basis for a USB keyboard that can be used in Linux or MS Windows.

**A new keyboard matrix and a 3d print of the ZX81 case was used, so no ZX81 were harmed in the production of this project**

<a href="zx81.jpg"><img src="zx81.jpg" height="300"/></a>
# Resources
The following resources are needed to complete this project
### ZX81 Case
A 3d printed replica ZX81 case, using [this](https://www.thingiverse.com/thing:4525078) design
### ZX81 Keyboard membrane
Replacement ZX81 keyboard membranes are readily available from sites such as ebay or [Sell My Retro](https://www.sellmyretro.com/category/retro-computers/sinclair/sinclair-zx81/components)
### ZX81 Keyboard connectors
The ZX81 keyboard membrane connects through one 5 way and one 8 way connector. These can be purchased from Sell My Retro or ebay
### Raspberry Pi Pico
To minimise soldering a Pi Pico H with male headers attached can be used

### Screws, Rubber feet, USB cable
Five 2.5x12 or 2.5x14 screws are needed to join the bottom and top halves of the case. To finish the effect ZX81 feet pads to cover the screws can be found on ebay or Sell My Retro

A micro to USB A cable makes the connection between the Pico and the Windows or Linux host. The Pico is powered by the host computer
## Connecting the keyboard membrane
The 13 lines from the membrane (5 columns, 8 rows) are routed to the first 13 GPIO lines on a Raspberry Pico via the keyboard connectors. The 5 columns connect to GP0 through to GP4, The rows connect to GP5 to GP12. This can be simply achieved by mounting the keyboard connectors on Veroboard. PCB headers are then attached to the Veroboard and Dupont female connectors used to join the header pins to the Pico GPIO pins. I am sure those with more hardware skills than me could easily fabricate a dedicated PCB, including mounting the Pico 2040

No diodes are used in the circuit. The keyboard functions well without them
## Software Installation
The project uses CircuitPython, and the Adafruit Matrix Keypad library. Instructions for installation can be found [here](https://learn.adafruit.com/matrix-keypad/python-circuitpython).

The code must run automatically on power up. In addition the usual auto-mount of the CIRCUITPY drive should be disabled.

`boot.py` is used to prevent automount. Using `code.py` as the filename for the code file ensures that the code will run on power on (see [here](https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial))

Both `boot.py` and `code.py` should be copied to the root directory of the CIRCUITPY drive

## Notes
Several ZX81 emulators have been tested. Most decode shift period as a comma. However at least two emulators do not, with shift period generating greater than

To support all emulators the shift state is tracked and a comma key state is explicitly sent in place of shift period

# Why?
The ZX81 keyboard is not the greatest for fast typing. Also it only possesses a sub-set of the keys needed to drive a modern OS. The reasons for creating this project were:
1) It can be fun to control a ZX81 emulator with an authentic keyboard
2) It makes a change for me to code for a real time application in Python, rather than C

It is also amusing that a $3 dollar part, running at 125MHz, with 264kB of RAM and 2MB of Flash, is being used to control the keyboard of the ZX81, when originally the ZX81 processor ran at 3.25MHz, and the base ZX81 was initially sold with 1kB of RAM!
