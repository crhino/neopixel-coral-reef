import board
import neopixel
from adafruit_led_animation.color import CYAN, BLUE, PURPLE, GREEN
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup

# construct color cycles given start and end colors


def color_cycle_array(start, end, steps):
    return list(map(lambda step: interpolate_color_between(
        start, end, step/steps), [i for i in range(steps)]))


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

# Objects on Pillar, not end number is non-inclusive
rock = PixelSubset(pixels, 49, 50)
shelf = PixelSubset(pixels, 45, 48)
antler = PixelSubset(pixels, 42, 45)
small_brain = PixelSubset(pixels, 41, 42)
big_brain = PixelSubset(pixels, 38, 40)
barnacle = PixelSubset(pixels, 35, 37)
branch1 = PixelSubset(pixels, 32, 33)
branch2 = PixelSubset(pixels, 34, 35)

# Color cycles
# TODO: fix colors better

steps = 50
cyan_to_blue = color_cycle_array(CYAN, BLUE, steps)
blue_to_purple = color_cycle_array(BLUE, PURPLE, steps)
blue_green_to_dark_green = color_cycle_array(BLUE, GREEN, steps)
light_green_to_blue = color_cycle_array(GREEN, CYAN, steps)

# Setup animations
# TODO: add delay to the cycle
rock_animation = ColorCycle(rock, 1, cyan_to_blue)
antler_animation = ColorCycle(antler, 1, light_green_to_blue)
shelf_animation = ColorCycle(shelf, 1, blue_to_purple)
sm_brain_animation = ColorCycle(small_brain, 1, blue_green_to_dark_green)
big_brain_animation = ColorCycle(big_brain, 1, light_green_to_blue)
barnacle_animation = ColorCycle(barnacle, 1, blue_green_to_dark_green)
branch1_animation = ColorCycle(branch1, 1, blue_to_purple)
branch2_animation = ColorCycle(branch2, 1, blue_to_purple)

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
    ),
)

# main loop
try:
    while True:
        animations.animate()
except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
