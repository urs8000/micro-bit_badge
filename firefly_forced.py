# A micro:bit Firefly.
# By Nicholas H.Tollervey. Released to the public domain.
# enhanced by urs marti (2016)
# - if no button pressed, it sends after a random delay
# - button A sends a flash , button B (should) clear message
#
# to do:  also textual messages should be received and displayed
# 
import radio
import random
from microbit import *

# Create the "flash" animation frames. Can you work out how it's done?
flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

# The radio won't work unless it's switched on.
radio.on()

must_send = random.randint(10000, 60000)   # forced flash at random delay
cnt_must_send = 0

# Event loop.
while True:
    cnt_must_send = cnt_must_send + 1
    if must_send == cnt_must_send:
        radio.send('flash')
        cnt_must_send = 0
    # Button A sends a "flash" message.
    if button_a.was_pressed():         # or button_b.was_pressed():
        radio.send('flash')  # a-ha
        cnt_must_send = 0
        display.set_pixel(2, 2, 9)
        sleep(100)
        display.set_pixel(2, 2, 0)
    # Read any incoming messages.
    incoming = radio.receive()
    if incoming == 'flash':
        # If there's an incoming "flash" message display
        # the firefly flash animation after a random short
        # pause.
        sleep(random.randint(50, 350))
        display.show(flash, delay=100, wait=False)
        cnt_must_send = 0
        # Randomly re-broadcast the flash message after a
        # slight delay.
        if random.randint(0, 9) == 0:
            sleep(500)
            radio.send('flash')  # a-ha