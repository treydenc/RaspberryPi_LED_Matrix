import board
import time
import neopixel
from adafruit_pixel_framebuf import PixelFramebuffer

pixel_pin = board.D18
pixel_width = 16
pixel_height = 48
num_pixels = pixel_width * pixel_height

# Initialize the NeoPixel object
pixels = neopixel.NeoPixel(
    pixel_pin,
    num_pixels,
    brightness=0.2,
    auto_write=False,
)

# The text you want to display
text = "Raspberry Pi Girls"

# Set up the frame buffer
pixel_framebuf = PixelFramebuffer(
     pixels,
     pixel_width,
     pixel_height,
     reverse_x=True,
     orientation=1,
     rotation=1
)

while True:
    for i in range(6 * len(text) + pixel_width - 1):
        pixel_framebuf.fill(0x000000)  # Clear the frame buffer with black
        pixel_framebuf.text(text, pixel_width - i, 4, 0xb400ff)  # Display the text with a color
        pixel_framebuf.display()  # Update the LED matrix with the buffer content
        time.sleep(0.05)  # Small delay to control the speed of the scrolling text
