import itertools
import board
import neopixel
from adafruit_led_animation.color import CYAN, BLUE, AQUA, GREEN
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup

# construct color cycles given start and end colors


def color_cycle_array(start, end, steps):
    list(map(lambda step: interpolate_color_between(
        start, end, step/steps), itertools.count(steps)))


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
    pixel_pin, pixel_num, brightness=1, auto_write=False)

# Objects on Pillar
rock = PixelSubset(pixels, 49, 49)
shelf = PixelSubset(pixels, 44, 46)
small_brain = PixelSubset(pixels, 41, 41)
big_brain = PixelSubset(pixels, 38, 39)
barnacle = PixelSubset(pixels, 36, 36)

# Color cycles
# TODO: fix colors better
cyan_to_blue = color_cycle_array(CYAN, AQUA)
blue_to_dark_blue = color_cycle_array(AQUA, BLUE)
blue_green_to_dark_green = color_cycle_array(BLUE, GREEN)
light_green_to_blue = color_cycle_array(GREEN, AQUA)

# Setup animations
# TODO: add delay to the cycle
rock_animation = ColorCycle(rock, 1, cyan_to_blue)
shelf_animation = ColorCycle(rock, 1, blue_to_dark_blue)
sm_brain_animation = ColorCycle(rock, 1, blue_green_to_dark_green)
big_brain_animation = ColorCycle(rock, 1, light_green_to_blue)
barnacle_animation = ColorCycle(rock, 1, cyan_to_blue)

animations = AnimationSequence(
    AnimationGroup(
        rock_animation,
        shelf_animation,
        sm_brain_animation,
        big_brain_animation,
        barnacle_animation,
    ),
)

# main loop
try:
    while True:
        animations.animate()
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
