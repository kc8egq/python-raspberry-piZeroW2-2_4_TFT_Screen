import digitalio
import board
import time

# Turn on the Backlight
backlight = digitalio.DigitalInOut(board.D23)
backlight.switch_to_output()
backlight.value = True
time.sleep(30)

backlight.value = False

