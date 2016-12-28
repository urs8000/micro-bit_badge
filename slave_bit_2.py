from microbit import *
import radio


# start here
radio.on()
radio.config(channel=43, queue=10, length=128, power=4, data_rate=radio.RATE_2MBIT)


while True:
    msg = radio.receive_bytes()
    if not msg:
        display.set_pixel(2, 2, 5)
    else:
        msg_len = 0
        msg_len = len(msg)
        display.scroll(msg, delay=150, loop=False)
        display.scroll("---")
        sleep(50)
        display.scroll(str(msg_len), delay=150, loop=False)
