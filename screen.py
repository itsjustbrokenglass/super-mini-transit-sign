# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
from transit import get_formatted_arrival_times
import board
import busio
from digitalio import DigitalInOut, Direction, Pull
from PIL import Image, ImageDraw
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# Create the SSD1306 OLED class.
disp = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c)


# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT
button_A.pull = Pull.UP

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT
button_B.pull = Pull.UP

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT
button_L.pull = Pull.UP

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT
button_R.pull = Pull.UP

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT
button_U.pull = Pull.UP

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT
button_D.pull = Pull.UP

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT
button_C.pull = Pull.UP


# Clear display.
disp.fill(0)
disp.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=0)
current_stop_code = 0


def draw_arrival_times(stop_code):
        if stop_code == 13428:
            stop_name = "7 Haight: Outbound"
        elif stop_code == 15201:
            stop_name = "N Judah: Outbound"
        draw.rectangle((0, 0, width, height), outline=0, fill=0)
        draw.multiline_text((5, 5), stop_name, fill=1)  

        times = get_formatted_arrival_times(stop_code)
        x = 20
        for time in times:
            draw.multiline_text((x, 30), str(time), fill=1)  
            x+=20

while True:
    if not button_L.value:
        current_stop_code = 13428

        draw_arrival_times(13428)
    if not button_R.value:
        current_stop_code = 15201

        draw_arrival_times(15201)
    if not button_A.value: 
        draw_arrival_times(current_stop_code)
    else:
        disp.image(image)

    disp.show()


