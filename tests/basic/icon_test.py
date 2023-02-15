import lvgl as lv
from seedsigner.hardware.st7789 import ST7789
import fs_driver



ANGLE_DOWN = "\uf107"
ANGLE_LEFT = "\uf104"
ANGLE_RIGHT = "\uf105"
ANGLE_UP = "\uf106"
CAMERA = "\uf030"
CARET_DOWN = "\uf0d7"
CARET_LEFT = "\uf0d9"
CARET_RIGHT = "\uf0da"
CARET_UP = "\uf0d8"
SOLID_CIRCLE_CHECK = "\uf058"
CIRCLE = "\uf111"
CIRCLE_CHEVRON_RIGHT = "\uf138"
DICE = "\uf522"
DICE_ONE = "\uf525"
DICE_TWO = "\uf528"
DICE_THREE = "\uf527"
DICE_FOUR = "\uf524"
DICE_FIVE = "\uf523"
DICE_SIX = "\uf526"
GEAR = "\uf013"
KEY = "\uf084"
KEYBOARD = "\uf11c"
LOCK = "\uf023"
MAP = "\uf279"
PAPER_PLANE = "\uf1d8"
PEN = "\uf304"
PLUS = "+"
POWER_OFF = "\uf011"
ROTATE_RIGHT = "\uf2f9"
SCREWDRIVER_WRENCH = "\uf7d9"
SQUARE = "\uf0c8"
SQUARE_CARET_DOWN = "\uf150"
SQUARE_CARET_LEFT = "\uf191"
SQUARE_CARET_RIGHT = "\uf152"
SQUARE_CARET_UP = "\uf151"
SQUARE_CHECK = "\uf14a"
TRIANGLE_EXCLAMATION = "\uf071"
UNLOCK = "\uf09c"
QRCODE = "\uf029"
X = "\u0058"
SDCARD = "\uf7c2"

icons = ['\uf107',
 '\uf104',
 '\uf105',
 '\uf106',
 '\uf030',
 '\uf0d7',
 '\uf0d9',
 '\uf0da',
 '\uf0d8',
 '\uf058',
 '\uf111',
 '\uf138',
 '\uf522',
 '\uf525',
 '\uf528',
 '\uf527',
 '\uf524',
 '\uf523',
 '\uf526',
 '\uf013',
 '\uf084',
 '\uf11c',
 '\uf023',
 '\uf279',
 '\uf1d8',
 '\uf304',
 '+',
 '\uf011',
 '\uf2f9',
 '\uf7d9',
 '\uf0c8',
 '\uf150',
 '\uf191',
 '\uf152',
 '\uf151',
 '\uf14a',
 '\uf071',
 '\uf09c',
 '\uf029',
 'X',
 '\uf7c2']

class SeedSignerCustomIconConstants:
    LARGE_CHEVRON_LEFT = "\ue900"
    SMALL_CHEVRON_RIGHT = "\ue901"
    PAGE_UP = "\ue903"
    PAGE_DOWN = "\ue902"
    PLUS = "\ue904"
    CIRCLE_CHECK = "\ue907"
    CIRCLE_EXCLAMATION = "\ue908"
    CIRCLE_X = "\ue909"
    FINGERPRINT = "\ue90a"
    PATH = "\ue90b"
    BITCOIN_LOGO_STRAIGHT = "\ue90c"
    BITCOIN_LOGO_TILTED = "\ue90d"

    MIN_VALUE = LARGE_CHEVRON_LEFT
    MAX_VALUE = BITCOIN_LOGO_TILTED

    ALL_GLYPHS = [
        LARGE_CHEVRON_LEFT,
        SMALL_CHEVRON_RIGHT,
        PAGE_UP,
        PAGE_DOWN,
        PLUS,
        CIRCLE_CHECK,
        CIRCLE_EXCLAMATION, 
        CIRCLE_X,
        FINGERPRINT,
        PATH,
        BITCOIN_LOGO_STRAIGHT,
        BITCOIN_LOGO_TILTED,
    ]



lv.init()
disp = ST7789(width=240, height=240)

# FS driver init
fs_drv = lv.fs_drv_t()
fs_driver.fs_register(fs_drv, 'S')

# FONT__OPEN_SANS__REGULAR__17 = lv.font_load("S:/opensans_regular_17.bin")
# FONT__OPEN_SANS__SEMIBOLD__18 = lv.font_load("S:/opensans_semibold_18.bin")
# FONT__OPEN_SANS__SEMIBOLD__20 = lv.font_load("S:/opensans_semibold_20.bin")
FONT__FONT_AWESOME__22 = lv.font_load("S:/fontawesome_22.bin")
FONT__FONT_AWESOME__24 = lv.font_load("S:/fontawesome_24.bin")
FONT__SEEDSIGNER_GLYPHS__22 = lv.font_load("S:/seedsigner_glyphs_22.bin")
FONT__SEEDSIGNER_GLYPHS__24 = lv.font_load("S:/seedsigner_glyphs_24.bin")

scr = lv.scr_act()
scr.clean()

scr.set_style_bg_color(lv.color_hex(0x000099), 0)


# text = ""
# for i, icon in enumerate(SeedSignerCustomIconConstants.ALL_GLYPHS):
#     text += icon + " "
#     if i > 0 and i % 4 == 0:
#         text += "\n"

# label = lv.label(scr)
# label.set_text(text)
# label.center()

# label_style = lv.style_t()
# label_style.set_text_font(FONT__SEEDSIGNER_GLYPHS__24)
# label_style.set_text_color(lv.color_hex(0xffcc00))
# label.add_style(label_style, 0)



# text = ""
# for i, icon in enumerate(icons):
#     text += icon + " "
#     if i > 0 and i % 8 == 0:
#         text += "\n"

# label = lv.label(scr)
# label.set_text(text)
# label.center()

# label_style = lv.style_t()
# label_style.set_text_font(FONT__FONT_AWESOME__22)
# label_style.set_text_color(lv.color_hex(0xffcc00))
# label.add_style(label_style, 0)



text = ""
for i, icon in enumerate(icons):
    text += icon + " "
    if i > 0 and i % 6 == 0:
        text += "\n"

label = lv.label(scr)
label.set_text(text)
label.center()

label_style = lv.style_t()
label_style.set_text_font(FONT__FONT_AWESOME__24)
label_style.set_text_color(lv.color_hex(0x88ff00))
label.add_style(label_style, 0)
