import board
import neopixel
from adafruit_led_animation.color import CYAN, BLUE, PURPLE, GREEN, YELLOW
from adafruit_led_animation.animation.colorcycle import ColorCycle
from adafruit_led_animation.helper import PixelSubset
from adafruit_led_animation.sequence import AnimationSequence
from adafruit_led_animation.group import AnimationGroup

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

# Objects on Pillar, end number is non-inclusive
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
# TODO: fix colors better

steps = 50
cyan_to_blue = color_cycle_array(CYAN, BLUE, steps)
blue_to_purple = color_cycle_array(BLUE, PURPLE, steps)
blue_green_to_dark_green = color_cycle_array(BLUE, GREEN, steps)
light_green_to_blue = color_cycle_array(GREEN, CYAN, steps)
yellow_to_green = color_cycle_array(YELLOW, GREEN, steps)

# Setup animations
# TODO: add delay to the cycle
speed = 0.2
rock_animation = ColorCycle(rock, speed, cyan_to_blue)
antler_animation = ColorCycle(antler, speed, light_green_to_blue)
shelf_animation = ColorCycle(shelf, speed, blue_to_purple)
sm_brain_animation = ColorCycle(small_brain, speed, blue_green_to_dark_green)
big_brain_animation = ColorCycle(big_brain, speed, blue_to_purple)
barnacle_animation = ColorCycle(barnacle, speed, blue_green_to_dark_green)
branch1_animation = ColorCycle(branch1, speed, light_green_to_blue)
branch2_animation = ColorCycle(branch2, speed, light_green_to_blue)
moray_animation = ColorCycle(moray, speed, yellow_to_green)
pipe1_animation = ColorCycle(pipe_barnacle1, speed, blue_green_to_dark_green)
pipe2_animation = ColorCycle(pipe_barnacle2, speed, blue_green_to_dark_green)
lips1_animation = ColorCycle(pointy_lips1, speed, blue_to_purple)
lips2_animation = ColorCycle(pointy_lips2, speed, blue_to_purple)
lips3_animation = ColorCycle(pointy_lips3, speed, blue_to_purple)
crab_animation = ColorCycle(crab_on_coral, speed, light_green_to_blue)

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
