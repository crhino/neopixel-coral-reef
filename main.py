import board
import neopixel
from adafruit_led_animation.color import CYAN, BLUE, PURPLE, GREEN, YELLOW
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup
DARK_BLUE = (3,5,99)
DARK_GREEN = (25,89,25)
BLUE_GREEN = (44,130,110)
LIGHT_GREEN = (114,245,2)
MED_BLUE = (5,165,250)
YELLOW_ORANGE = (250,224,27)
GREEN_YELLOW = (213,250,65)
TEAL = (45,128,140)
DARK_PURPLE = (128,5,247)

# construct color cycles given start and end colors

def color_cycle_array(start, end, steps):
    colors = list(map(lambda step: interpolate_color_between(
        start, end, step/steps), [i for i in range(steps)]))
    colors.extend(colors[::-1])
    return colors


def interpolate_color_between(color1, color2, ratio):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    r = int(r1 + (r2 - r1) * ratio)
    g = int(g1 + (g2 - g1) * ratio)
    b = int(b1 + (b2 - b1) * ratio)
    return (r, g, b)


pixel_pin = board.D18
pixel_num = 50

pixels = neopixel.NeoPixel(
    pixel_pin, pixel_num, brightness=1, auto_write=False,
    pixel_order=neopixel.RGB)

# LED # for each objects on Pillar, end number is non-inclusive
rock = PixelSubset(pixels, 27, 28)
shelf = PixelSubset(pixels, 20, 23)
antler = PixelSubset(pixels, 17, 20)
small_brain = PixelSubset(pixels, 7, 8)
big_brain = PixelSubset(pixels, 9, 11)
barnacle = PixelSubset(pixels, 12, 14)
branch1 = PixelSubset(pixels, 14, 15)
branch2 = PixelSubset(pixels, 24, 25)
moray = PixelSubset(pixels, 26, 27)
pipe_barnacle1 = PixelSubset(pixels, 29, 30)
pointy_lips1 = PixelSubset(pixels, 31, 32)
pipe_barnacle2 = PixelSubset(pixels, 34, 35)
pointy_lips2 = PixelSubset(pixels, 36, 37)
pointy_lips3 = PixelSubset(pixels, 38, 39)
crab_on_coral = PixelSubset(pixels, 41, 42)

# Color cycles

steps = 50
cyan_to_blue = color_cycle_array(CYAN, BLUE, steps)
blue_to_purple = color_cycle_array(BLUE, PURPLE, steps)
green_to_light_green = color_cycle_array(GREEN, LIGHT_GREEN, steps)
blue_green_to_dark_green = color_cycle_array(BLUE_GREEN, DARK_GREEN, steps)
light_green_to_med_blue = color_cycle_array(LIGHT_GREEN, MED_BLUE, steps)
dark_purple_to_green = color_cycle_array(DARK_PURPLE, GREEN, steps)
yellow_orange_to_green_yellow = color_cycle_array(YELLOW_ORANGE, GREEN_YELLOW, steps)

# Setup animations
# TODO: add delay to the cycle
speed = 0.2
crab_animation = ColorCycle(crab_on_coral, speed, dark_purple_to_green)
lips1_animation = ColorCycle(pointy_lips1, speed, blue_to_purple)
lips2_animation = ColorCycle(pointy_lips2, speed, blue_to_purple)
lips3_animation = ColorCycle(pointy_lips3, speed, blue_to_purple)
pipe1_animation = ColorCycle(pipe_barnacle1, speed, light_green_to_med_blue)
pipe2_animation = ColorCycle(pipe_barnacle2, speed, light_green_to_med_blue)
rock_animation = ColorCycle(rock, speed, blue_green_to_dark_green)
moray_animation = ColorCycle(moray, speed, yellow_orange_to_green_yellow)
shelf_animation = ColorCycle(shelf, speed, cyan_to_blue)
branch1_animation = ColorCycle(branch1, speed, light_green_to_med_blue)
branch2_animation = ColorCycle(branch2, speed, light_green_to_med_blue)
barnacle_animation = ColorCycle(barnacle, speed, blue_green_to_dark_green)
antler_animation = ColorCycle(antler, speed, green_to_light_green)
big_brain_animation = ColorCycle(big_brain, speed, cyan_to_blue)
sm_brain_animation = ColorCycle(small_brain, speed, dark_purple_to_green)







animations = AnimationSequence(
    AnimationGroup(
        rock_animation,
        antler_animation,
        shelf_animation,
        sm_brain_animation,
        big_brain_animation,
        barnacle_animation,
        branch1_animation,
        branch2_animation,
        moray_animation,
        pipe1_animation,
        pipe2_animation,
        lips1_animation,
        lips2_animation,
        lips3_animation,
        crab_animation,
    ),
)

# main loop
try:
    while True:
        animations.animate()
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
