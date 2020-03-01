# Numworks hardware
The screen is 320 x 220 pixels

*MCU STM32F730V8T6
This is the brain and heart of our calculator. This chip combines an ARMv7-M Cortex-M7 core clocked at 216 MHz and 256K of Static RAM.

*Flash memory AT25SF641
This is the persistant memory of our calculator. This chip stores 64 Mbit of data, and serves it over a 104 MHz Quad-SPI bus

*Display controller ST7789V
The LCD panel integrates an LCD controller that receives bitmap data from the MCU and drives the pixel matrix accordingly. This LCD controller has an integrated SRAM framebuffer and is driven using a 16-bit wide bus.

*Logic power supply RT9078
This part regulates the voltage from the Lithium-Polymer battery. It's a low-dropout regulator that takes any voltage between 3.0V and 5.5V and outputs a constant 2.8V. Its efficiency depends on the voltage gap and is fixed by the fact that the input current is equal to the output current.

*RGB LED LTST-S310F2KT
This surface-mounted component includes three LEDs (red, green and blue) in a small package. These LEDs are able to glow an arbitrary through the casing of the device.

## Numworks Python Turtle manual
[From the manual](https://www.numworks.com/fr/ressources/manuel/python/#le-module-turtle)

forward (x)
Advance by x pixels.

backward (x)
Move back x pixels.

right (a)
Rotates from a degrees to the right.

left (a)
Rotates from a degrees to the left.

goto (x, y)
Go to the coordinate point (x, y).

setheading (a)
Sets an orientation from a degrees.

circle (r)
Draw a circle with radius r pixels.

speed (x)
Defines the speed of the plot (x is between 0 and 10).

position()
Returns the current position (x, y) of the turtle.

heading ()
Returns the current orientation of the turtle.

pendown ()
Lower the pencil.

PenUp ()
Lift the pencil.

pensize (x)
Size of the plot in pixels.

isDown ()
Returns True if the pencil is lowered.

reset ()
Reset the drawing.

showturtle ()
Displays the turtle.

hideturtle ()
Hide the turtle.

color ('c') or color (r, g, b)
Changes the color of the path.

blue
Color blue.

red
Red color.

green
Green color.

yellow
Yellow color.

brown
Brown color.

black
Black color.

white
White color.

pink
Pink color.

orange
Orange color.

purple
Violet color.

gray
Grey color.
