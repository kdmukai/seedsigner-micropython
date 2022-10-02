from threading import Lock

import lvgl as lv
import ili9XXX
from ili9XXX import st7789

from seedsigner.models import ConfigurableSingleton



class Renderer(ConfigurableSingleton):
    buttons = None
    canvas_width = 0
    canvas_height = 0
    lv_screen = None
    lock = Lock()


    @classmethod
    def configure_instance(cls):
        # Instantiate the one and only Renderer instance
        renderer = cls.__new__(cls)
        cls._instance = renderer

        renderer.canvas_width = 240
        renderer.canvas_height = 240

        renderer.lv_screen = st7789(
            # Saola-1R
            mosi=11, clk=12, cs=10, dc=1, rst=2,
            width=renderer.canvas_width, height=renderer.canvas_height,
            rot=ili9XXX.LANDSCAPE,
        )


    def show_image(self, image=None, alpha_overlay=None):
        pass


    def show_image_pan(self, image, start_x, start_y, end_x, end_y, rate, alpha_overlay=None):
        pass


    # TODO: Remove all references
    def show_image_with_text(self, image, text, font=None, text_color="GREY", text_background=None):
        pass


    # TODO: Should probably move this to screens.py
    def draw_modal(self, lines = [], title = "", bottom = "") -> None:
        pass


    # TODO: Should probably move this to templates.py
    def draw_prompt_yes_no(self, lines = [], title = "", bottom = "") -> None:
        pass


    # TODO: Should probably move this to templates.py
    def draw_prompt_custom(self, a_txt, b_txt, c_txt, lines = [], title = "", bottom = "") -> None:
        pass


    def display_blank_screen(self):
        self.lv_screen.clean()

