import board
import neopixel

pixel_pin = board.D18
pixel_width = 32
pixel_height = 8
num_pixels = pixel_width * pixel_height

pixels = neopixel.NeoPixel(
    pixel_pin,
    num_pixels,
    brightness=1.0, 
    auto_write=False,
    pixel_order=neopixel.RGB 
)


def fill_all(color):
    pixels.fill(color)
    pixels.show()


try:
    fill_all((255, 255, 255))

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()