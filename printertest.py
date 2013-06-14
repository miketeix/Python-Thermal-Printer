#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)



# Print the 75x75 pixel logo in adalogo.py
import gfx.wayfinding as wayfinding
printer.printBitmap(wayfinding.width, wayfinding.height, wayfinding.data)


printer.sleep()      # Tell printer to sleep
printer.wake()       # Call wake() before printing again, even if reset
printer.setDefault() # Restore printer to defaults
