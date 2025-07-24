"""
ampy -p /dev/tty.usbserial-1110 put seedsigner/resources/fonts/opensans_semibold_18.bin

cd src
mpremote connect /dev/tty.usbserial-1110 mount . run ../tests/basic/home_screen_test.py
"""
import lvgl as lv

# MUST init before gui.components tries to use the fs_driver to load fonts
lv.init()

from seedsigner.hardware.st7789 import ST7789
from seedsigner.gui.components import Button, FontAwesomeIconConstants, LargeIconButton, TopNav, GUIConstants, Fonts
from seedsigner.gui.components import TopNav
from seedsigner.hardware.buttons import HardwareButtons, HardwareButtonsConstants

from seedsigner.hardware.pin_defs import waveshare_esp32_s3_touch_lcd_2 as pins


lv.init()

disp = ST7789(pins["st7789"])

# HardwareButtons HAVE to be instantiated AFTER the display!!
# hardware_inputs = HardwareButtons()

scr = lv.screen_active()
scr.clean()

scr.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scr.set_style_bg_color(lv.color_hex(0x000000), 0)



topnav = TopNav()
topnav.show_back_button = False
topnav.show_power_button = True
topnav.text = "Home"
topnav.font_size = 26
topnav.add_to_lv_obj(scr)

btn1 = LargeIconButton()
btn1.icon_name = FontAwesomeIconConstants.QRCODE
btn1.text = "Scan"
btn1.is_selected = True
btn1.align_to = (topnav.lv_obj, lv.ALIGN.OUT_BOTTOM_LEFT, GUIConstants.EDGE_PADDING, 0)
btn1.add_to_lv_obj(scr)

btn2 = LargeIconButton()
btn2.icon_name = FontAwesomeIconConstants.KEY
btn2.text = "Seeds"
btn2.align_to = (btn1.lv_btn, lv.ALIGN.OUT_RIGHT_TOP, GUIConstants.COMPONENT_PADDING, 0)
btn2.add_to_lv_obj(scr)

btn3 = LargeIconButton()
btn3.icon_name = FontAwesomeIconConstants.SCREWDRIVER_WRENCH
btn3.text = "Tools"
btn3.align_to = (btn1.lv_btn, lv.ALIGN.OUT_BOTTOM_LEFT, 0, GUIConstants.COMPONENT_PADDING)
btn3.add_to_lv_obj(scr)

btn4 = LargeIconButton()
btn4.icon_name = FontAwesomeIconConstants.GEAR
btn4.text = "Settings"
btn4.align_to = (btn2.lv_btn, lv.ALIGN.OUT_BOTTOM_LEFT, 0, GUIConstants.COMPONENT_PADDING)
btn4.add_to_lv_obj(scr)


# # Can only resize to content AFTER it's all been loaded
# button_list_obj.set_height(lv.SIZE_CONTENT)
# button_list_obj.align_to(textarea, lv.ALIGN.OUT_BOTTOM_MID, 0, GUIConstants.COMPONENT_PADDING)

buttons = [btn1, btn2, btn3, btn4]
cur_selected_button = 0

import task_handler  # NOQA
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


# while True:
#     # allow repeats for directional keys; single response only for center press or KEY1, 2, 3.
#     key = hardware_inputs.wait_for(keys=HardwareButtonsConstants.ALL_KEYS, check_release=True, release_keys=HardwareButtonsConstants.KEYS__ANYCLICK)
#     if key == HardwareButtonsConstants.KEY_DOWN:
#         if topnav.is_selected:
#             topnav.set_is_selected(False)
#             buttons[cur_selected_button].set_is_selected(True)

#         elif cur_selected_button <= 1:
#             buttons[cur_selected_button].set_is_selected(False)
#             cur_selected_button += 2
#             buttons[cur_selected_button].set_is_selected(True)

#     elif key == HardwareButtonsConstants.KEY_UP:
#         if cur_selected_button <= 1 and not topnav.is_selected:
#             topnav.set_is_selected(True)
#             buttons[cur_selected_button].set_is_selected(False)

#         elif cur_selected_button >= 2:
#             buttons[cur_selected_button].set_is_selected(False)
#             cur_selected_button -= 2
#             buttons[cur_selected_button].set_is_selected(True)

#     elif key == HardwareButtonsConstants.KEY_RIGHT:
#         if topnav.is_selected:
#             continue

#         if cur_selected_button in [0, 2]:
#             buttons[cur_selected_button].set_is_selected(False)
#             cur_selected_button += 1
#             buttons[cur_selected_button].set_is_selected(True)

#     elif key == HardwareButtonsConstants.KEY_LEFT:
#         if topnav.is_selected:
#             continue

#         if cur_selected_button in [1, 3]:
#             buttons[cur_selected_button].set_is_selected(False)
#             cur_selected_button -= 1
#             buttons[cur_selected_button].set_is_selected(True)
