import lvgl as lv
from seedsigner.hardware.st7789 import ST7789


lv.init()
disp = ST7789(width=240, height=240)
scr = lv.scr_act()
scr.clean()

scr.set_style_bg_color(lv.color_hex(0x000000), 0)

label = lv.label(scr)
label.set_text("Hello, world!")
label.center()

label_style = lv.style_t()
label_style.set_text_color(lv.color_hex(0xffffff))
label.add_style(label_style, 0)
