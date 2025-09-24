# This program demonstrates how to use Python and gpiozero to blink Morse code with an LED on a Raspberry Pi. It encodes the word PACE in Morse code and outputs it through LED flashes.

#!/usr/bin/python

import gpiozero
import time

led = gpiozero.PWMLED(17)

morsecode = ".--. .- -.-. ."


for c in morsecode:
        if c == ".":
                led.on()
                time.sleep(.3)
                led.off()
        elif c == "-":
                led.on()
                time.sleep(1)
                led.off()
        elif c == " ":
                time.sleep(2)
        time.sleep(.1)
pace in morse code:
Blink "PACE" as morris code on your Pi

2 second delay between letters  -off

.3 sec delay for a DOT - on

1  sec delay for a DASH    -on
 
,1 sec delay between dots/dashes    -off
