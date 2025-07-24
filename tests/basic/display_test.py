import lvgl as lv
import task_handler
from seedsigner.hardware.st7789 import ST7789


# see pin_defs.py and import the pin defs that match your build
from seedsigner.hardware.pin_defs import waveshare_esp32_s3_touch_lcd_2 as pins
#from .pin_defs import dev_board as pins
# from pin_defs import manual_wiring as pins
# raspi = dict(
#     st7789=dict(
#         mosi=10,
#         clk=11,
#         cs=8,  # SPI CS pin
#         dc=25,  # Data/Command pin
#         rst=27,  # Reset pin
#     ),
# )

# pins = raspi

lv.init()
disp = ST7789(pins["st7789"])
print("Display initialized")
scr = lv.screen_active()
scr.clean()

scr.set_style_bg_color(lv.color_hex(0x0000ff), 0)

label = lv.label(scr)
label.set_text("Hello, world?")
label.center()

label_style = lv.style_t()
label_style.set_text_color(lv.color_hex(0x00ff00))
label.add_style(label_style, 0)


th = task_handler.TaskHandler()


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