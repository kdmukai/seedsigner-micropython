"""
ampy -p /dev/tty.usbserial-1110 put seedsigner/resources/fonts/opensans_semibold_18.bin

cd src
mpremote connect /dev/tty.usbserial-1110 mount . run ../tests/basic/gui_button_test.py
"""
import lvgl as lv
from seedsigner.hardware.st7789 import ST7789
from seedsigner.gui.components import Button, FontAwesomeIconConstants, TopNav, GUIConstants, Fonts
from seedsigner.hardware.buttons import HardwareButtons, HardwareButtonsConstants


lv.init()

disp = ST7789(width=240, height=240)

# HardwareButtons HAVE to be instantiated AFTER the display!!
hardware_inputs = HardwareButtons()

scr = lv.scr_act()
scr.clean()

scr.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
scr.set_style_bg_color(lv.color_hex(0x000000), 0)


topnav = TopNav()
topnav.text = "Wienerschnitzel Gesundheit Fahrvergnügen!"
topnav.add_to_lv_obj(scr)

textarea = lv.textarea(scr)
textarea.set_width(240)
textarea.set_height(lv.SIZE_CONTENT)
textarea.set_y(GUIConstants.TOP_NAV_HEIGHT + GUIConstants.COMPONENT_PADDING)
# textarea.align_to(topnav, lv.ALIGN.BOTTOM_MID, 0, GUIConstants.COMPONENT_PADDING)
style = lv.style_t()
style.init()
style.set_pad_all(0)
style.set_pad_left(GUIConstants.EDGE_PADDING)
style.set_pad_right(GUIConstants.EDGE_PADDING)
style.set_border_width(0)
style.set_radius(0)
style.set_bg_color(lv.color_hex(0x000000))
style.set_text_color(lv.color_hex(GUIConstants.BODY_FONT_COLOR))
style.set_text_font(Fonts.FONT__OPEN_SANS__REGULAR__17__BPP8)
textarea.add_style(style, 0)
textarea.set_text("You are stealing: right to jail. You are playing music too loud: right to jail, right away. Driving too fast: jail. Slow: jail.")
textarea.update_layout()


# label_dsc = lv.draw_label_dsc_t()
# label_dsc.init()
# label_dsc.color = lv.color_hex(GUIConstants.BODY_FONT_COLOR)
# label_dsc.font =Fonts.FONT__OPEN_SANS__REGULAR__34     # 2x sample size!


# # Do the resize calcs on a background screen
# background = lv.obj()
# canvas = lv.canvas(background)
# cbuf = bytearray(480 * 480 * 4)
# canvas.set_buffer(cbuf, 480, 480, lv.img.CF.RGB565)
# canvas.draw_text(0, 0, 480, label_dsc, "You are stealing: right to jail. You are playing music too loud: right to jail, right away. Driving too fast: jail. Slow: jail.", lv.label.ALIGN.LEFT)


# # Render the final result to the foreground screen
# finalcanvas = lv.canvas(scr)
# finalbuf = bytearray(240 * 240 * 4)
# finalcanvas.set_buffer(finalbuf, 240, 240, lv.img.CF.RGB565)
# canvas.transform(canvas=finalcanvas, zoom=128, antialias=True, offset_x=0, offset_y=0)
# finalcanvas.align_to(textarea, lv.ALIGN.OUT_BOTTOM_MID, 0, GUIConstants.COMPONENT_PADDING)


# textarea2 = lv.textarea(scr)
# textarea2.set_width(240)
# textarea2.set_height(lv.SIZE_CONTENT)
# textarea2.align_to(textarea, lv.ALIGN.OUT_BOTTOM_MID, 0, GUIConstants.COMPONENT_PADDING)
# style = lv.style_t()
# style.init()
# style.set_pad_all(0)
# style.set_pad_left(GUIConstants.EDGE_PADDING)
# style.set_pad_right(GUIConstants.EDGE_PADDING)
# style.set_border_width(0)
# style.set_radius(0)
# style.set_bg_color(lv.color_hex(0x000000))
# style.set_text_color(lv.color_hex(GUIConstants.BODY_FONT_COLOR))
# style.set_text_font(Fonts.FONT__OPEN_SANS__REGULAR__17__BPP8)
# textarea2.add_style(style, 0)
# textarea2.set_text("You are stealing: right to jail. You are playing music too loud: right to jail, right away. Driving too fast: jail. Slow: jail.")
# textarea2.update_layout()


button_list_obj = lv.obj(scr)
button_list_obj.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
button_list_obj.set_width(240)
style = lv.style_t()
style.init()
style.set_pad_all(0)
style.set_pad_bottom(GUIConstants.EDGE_PADDING)
style.set_border_width(0)
style.set_radius(0)
style.set_bg_color(lv.color_hex(0x000000))
button_list_obj.add_style(style, 0)

btn1 = Button()
btn1.icon_name = FontAwesomeIconConstants.CAMERA
btn1.is_icon_inline = True
btn1.text = "Hello, world!"
btn1.is_text_centered = False
btn1.is_selected = True
btn1.align_to = (button_list_obj, lv.ALIGN.TOP_MID, 0, 0)
btn1.add_to_lv_obj(button_list_obj)

btn2 = Button()
btn2.icon_name = FontAwesomeIconConstants.KEYBOARD
btn2.is_icon_inline = True
btn2.text = "Riesling Trockenbeerenauslese"
btn2.is_text_centered = False
btn2.align_to = (btn1.lv_btn, lv.ALIGN.OUT_BOTTOM_MID, 0, GUIConstants.LIST_ITEM_PADDING)
btn2.add_to_lv_obj(button_list_obj)

btn3 = Button()
btn3.text = "Arbeiterunfallverischerungsgesetz"
btn3.is_text_centered = False
btn3.align_to = (btn2.lv_btn, lv.ALIGN.OUT_BOTTOM_MID, 0, GUIConstants.LIST_ITEM_PADDING)
btn3.add_to_lv_obj(button_list_obj)

btn4 = Button()
btn4.text = "Hello, scrolling!"
btn4.is_text_centered = False
btn4.align_to = (btn3.lv_btn, lv.ALIGN.OUT_BOTTOM_MID, 0, GUIConstants.LIST_ITEM_PADDING)
btn4.add_to_lv_obj(button_list_obj)

btn5 = Button()
btn5.text = "Hello, bottom!"
btn5.is_text_centered = False
btn5.align_to = (btn4.lv_btn, lv.ALIGN.OUT_BOTTOM_MID, 0, GUIConstants.LIST_ITEM_PADDING)
btn5.add_to_lv_obj(button_list_obj)

# Can only resize to content AFTER it's all been loaded
button_list_obj.set_height(lv.SIZE_CONTENT)
button_list_obj.align_to(textarea, lv.ALIGN.OUT_BOTTOM_MID, 0, GUIConstants.COMPONENT_PADDING)

buttons = [btn1, btn2, btn3, btn4, btn5]
cur_selected_button = 0

while True:
    # allow repeats for directional keys; single response only for center press or KEY1, 2, 3.
    key = hardware_inputs.wait_for(keys=HardwareButtonsConstants.ALL_KEYS, check_release=True, release_keys=HardwareButtonsConstants.KEYS__ANYCLICK)
    if key == HardwareButtonsConstants.KEY_DOWN:
        if cur_selected_button < len(buttons) - 1:
            buttons[cur_selected_button].set_is_selected(False)
            cur_selected_button += 1
            buttons[cur_selected_button].set_is_selected(True)

            # button reports its position relative to its parent container
            btn_y = buttons[cur_selected_button].lv_btn.get_y() + button_list_obj.get_y()
            scroll_pos = scr.get_scroll_top()
            if btn_y - scroll_pos > 240 - (int(2.25*GUIConstants.BUTTON_HEIGHT) + GUIConstants.LIST_ITEM_PADDING):
                scr.scroll_to_y(btn_y - 240 + int(2.25*GUIConstants.BUTTON_HEIGHT) + GUIConstants.LIST_ITEM_PADDING, lv.ANIM.ON)
    elif key == HardwareButtonsConstants.KEY_UP:
        if cur_selected_button > 0:
            buttons[cur_selected_button].set_is_selected(False)
            cur_selected_button -= 1
            buttons[cur_selected_button].set_is_selected(True)
        else:
            scroll_pos = scr.get_scroll_top()
            if scroll_pos > topnav.lv_obj.get_height():
                scr.scroll_to_y(topnav.lv_obj.get_height(), lv.ANIM.ON)
            else:
                scr.scroll_to_y(0, lv.ANIM.ON)

