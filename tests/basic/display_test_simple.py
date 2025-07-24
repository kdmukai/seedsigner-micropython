# Copyright (c) 2024 - 2025 Kevin G. Schlosser

from micropython import const


import lcd_bus  # NOQA
# this next section is the setup for the SPIBus.
# How this works is like this.
# I recommend using the hardware pins for SPI. This is going to
# get you the best speeds possible. This is due to the design of the MCU.

# Pi Zero
# import import st7789
# display_cls = st7789.ST7789
# _WIDTH = 240
# _HEIGHT = 320
# pins = dict(
#     dc=25,  # Data/Command pin, this is used to tell the display
#     mosi=10,  # Master Out Slave In pin, this is used to send data to the display
#     miso=9,  # Master In Slave Out pin, this is used to receive
#     sck=11,  # Serial Clock pin, this is used to clock the data to the display
#     cs=8,  # Chip Select pin, this is used to select the display
#     reset=27,  # Reset pin, this is used to reset the display
#     power=-1,  # Power pin, this is used to power on the display
#     backlight=24,  # Backlight pin, this is used to turn on and
    # reset_state=st7789.STATE_HIGH,
    # power_on_state=st7789.STATE_HIGH,
    # backlight_on_state=st7789.STATE_HIGH,
# )

# Waveshare ESP32-S3 Touch LCD 3.5B
# import axs15231b
# display_cls = axs15231b.AXS15231B
# _WIDTH = 320
# _HEIGHT = 480
# config = dict(
#     dc=3,  # Data/Command pin, this is used to tell the display
#     mosi=1,  # Master Out Slave In pin, this is used to send data to the display
#     miso=2,  # Master In Slave Out pin, this is used to receive
#     sck=5,  # Serial Clock pin, this is used to clock the data to the display
#     cs=12,  # Chip Select pin, this is used to select the display
#     reset=-1,  # Note: Expansion pin
#     power=-1,  # Power pin, this is used to power on the display
#     backlight=6,  # Backlight pin, this is used to turn on and
#     reset_state=axs15231b.STATE_HIGH,
#     power_on_state=axs15231b.STATE_HIGH,
#     backlight_on_state=axs15231b.STATE_HIGH,
#     color_byte_order=axs15231b.BYTE_ORDER_RGB,
#     rgb565_byte_swap=True,
# )


# Waveshare ESP32-S3 Touch LCD 2
import st7789
display_cls = st7789.ST7789
_WIDTH = 240
_HEIGHT = 320
from seedsigner.hardware.pin_defs import waveshare_esp32_s3_touch_lcd_2
config = waveshare_esp32_s3_touch_lcd_2['st7789'].copy()
config.update(dict(
    reset_state=st7789.STATE_LOW,
    power_on_state=st7789.STATE_LOW,
    backlight_on_state=st7789.STATE_PWM,
    color_byte_order=st7789.BYTE_ORDER_BGR,
    rgb565_byte_swap=True,
))


# this is a required setting. You MUST supply a value here.
_DC_PIN = config['dc']

# if you leave the `host` at its default or set it to -1 then this must be
# supplied. This is the pin that sends data to the display.
_MOSI_PIN = config['mosi']

# There is an option that can be used to save making a pin connection.
# in most cses the display is only going to have to receive data to it.
# So the SPI bus only has to transmit. If you set the `tx_only` parameter to
# True this pin will be changed to -1. If you have the `host` left at its
# default or it is set to -1 that means you want the host assignment picked
# automatically. If that is the case then you will need to set this to the
# pin that it is assigned to for the host you are going to want to use.
# If the host is set to -1 or it is left at its default even if even if you have
# `tx_only` to True you will need to set this. Don't worry you will not have
# to make a connection from the display to this pin if you are using `tx_only`.
_MISO_PIN = config['miso']

# if you leave the `host` at its default or set it to -1 then this must be
# supplied.
_SCLK_PIN = config['clk']

# This is the pin that selects the display so it can receive data. This pin
# is optional and can be set to -1. If this pin is set to -1 the display MUST
# be the only device attached to the bus other than the MCU. The CS pin on the
# display side will need to be pulled either high or low depending on the
# specification for the display
_CS_PIN = config['cs']

# _FREQ = const(80000000)
_FREQ = 40_000_000

# these pins get set Automatically if you are using hardware SPI pins and you
# have qud_spi set to True. You can set them manually if you are using
# something other than the hardware pins.
# _WP_PIN = const(-1)
# _HD_PIN = const(-1)
_WP_PIN = -1
_HD_PIN = -1

import machine
spi_bus = machine.SPI.Bus(
    host=1,
    mosi=config['mosi'],
    miso=config['miso'],
    sck=config['clk']
)
print("created SPI bus")

display_bus = lcd_bus.SPIBus(
    spi_bus=spi_bus,
    freq=_FREQ,
    dc=config['dc'],
    cs=config['cs'],
)
print("created display bus")

# reset pin, this pin is used to reset the display.
# If there is no reset pin for your display set this to -1.
_RESET_PIN = config['rst']

# power pin, this pin is used to power on the display.
# If there is no power pin for your display set this to -1.
_POWER_PIN = config['power']

# backlight pin, this pin is used to turn on and off the
# backlight to the display.
# If there is no backlight pin for your display set this to -1.
_BACKLIGHT_PIN = config['backlight']


# some displays have a bezel that covers a small portion of the viewable area
# of the display. This is to offset the display data so it is not covered by
# the bezel. Keep in mind that you will have to adjust the width and height in
# order to compensate for the right and bottom edges of the display.
_OFFSET_X = 0
_OFFSET_Y = 0


import lvgl as lv  # NOQA


display = display_cls(
    data_bus=display_bus,
    display_width=_WIDTH,
    display_height=_HEIGHT,
    backlight_pin=_BACKLIGHT_PIN,
    color_space=lv.COLOR_FORMAT.RGB565,
    color_byte_order=config['color_byte_order'],
    rgb565_byte_swap=config['rgb565_byte_swap'],
)
print("instantiated the display")

display.set_rotation(3)

import task_handler  # NOQA

# Remember you are going to need to power the display
# on if you have a power pin connected. If you set this to True and you have
# the power pin set to -1 do not worry it will simply return doing nothing.
# it is ideal to have this in place no matter what so if you change the display
# to one that does have the power pin the only thing you are going
# to need to change is the pin number
display.set_power(True)
print("set power")

# The old drivers used to inot the display automatically. I have decided against
# doing that to save memory. So the init must be done at some point before
# you create any LVGL objects.
display.init()
print("init")


display.set_backlight(100)
print("set backlight")

th = task_handler.TaskHandler()

scrn = lv.screen_active()
scrn.set_style_bg_color(lv.color_hex(0x000000), 0)
print("set screen background color")

# slider = lv.slider(scrn)
# slider.set_size(200, 50)
# slider.center()

label = lv.label(scrn)
label.set_text('Hello, world!')
label.align(lv.ALIGN.CENTER, 0, 50)
print("created label")


import time
time_passed = 1000000

print("starting main loop")
while True:
    start_time = time.time_ns()
    time.sleep_ms(1000)
    lv.tick_inc(int(time_passed // 1000000))
    time_passed -= int(time_passed // 1000000) * 1000000
    lv.task_handler()
    end_time = time.time_ns()
    time_passed += time.ticks_diff(end_time, start_time)
    print(f"{time_passed=}")
