# from threading import Lock
import _thread
import lvgl as lv

from seedsigner.hardware.st7789 import ST7789



class Renderer:
    buttons = None
    canvas_width = 0
    canvas_height = 0
    lv_screen = None
    lock = _thread.allocate_lock()


    def __init__(self):
        self.canvas_width = 240
        self.canvas_height = 240

        # Initialize LVGL
        lv.init()

        # Instantiate the LVGL-aware screen
        self.lv_screen = ST7789(
            width=self.canvas_width, height=self.canvas_height,
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

