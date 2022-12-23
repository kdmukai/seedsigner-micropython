import lvgl as lv
import ili9XXX
from ili9XXX import st7789

# see pin_defs.py and import the pin defs that match your build
from .pin_defs import dev_board as pins
# from pin_defs import manual_wiring as pins



class ST7789(st7789):
    """class for ST7789  240*240 1.3inch OLED displays."""

    def __init__(self, width: int, height: int):
        super().__init__(
            **pins["st7789"],
            width=width, height=height,
            rot=ili9XXX.LANDSCAPE,
        )
