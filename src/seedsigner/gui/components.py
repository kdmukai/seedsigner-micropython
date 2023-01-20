import lvgl as lv



# TODO: Remove all pixel hard coding
class GUIConstants:
    EDGE_PADDING = 8
    COMPONENT_PADDING = 8
    LIST_ITEM_PADDING = 4

    BACKGROUND_COLOR = 0x000000
    WARNING_COLOR = 0xffd60a
    DIRE_WARNING_COLOR = 0xff0000
    SUCCESS_COLOR = 0x00dd00
    BITCOIN_ORANGE = 0xff9416
    ACCENT_COLOR = 0xffcc00
    TESTNET_COLOR = 0x00f100
    REGTEST_COLOR = 0x00caf1

    ICON_FONT_NAME__FONT_AWESOME = "Font_Awesome_6_Free-Solid-900"
    ICON_FONT_NAME__SEEDSIGNER = "seedsigner-glyphs"
    ICON_FONT_SIZE = 22
    ICON_INLINE_FONT_SIZE = 24
    ICON_LARGE_BUTTON_SIZE = 36
    ICON_PRIMARY_SCREEN_SIZE = 50

    TOP_NAV_TITLE_FONT_NAME = "OpenSans-SemiBold"
    TOP_NAV_TITLE_FONT_SIZE = 20
    TOP_NAV_HEIGHT = 48
    TOP_NAV_BUTTON_SIZE = 32

    BODY_FONT_NAME = "OpenSans-Regular"
    BODY_FONT_SIZE = 17
    BODY_FONT_MAX_SIZE = TOP_NAV_TITLE_FONT_SIZE
    BODY_FONT_MIN_SIZE = 15
    BODY_FONT_COLOR = 0xf8f8f8
    BODY_LINE_SPACING = COMPONENT_PADDING

    FIXED_WIDTH_FONT_NAME = "Inconsolata-Regular"
    FIXED_WIDTH_EMPHASIS_FONT_NAME = "Inconsolata-SemiBold"

    LABEL_FONT_SIZE = BODY_FONT_MIN_SIZE
    LABEL_FONT_COLOR = 0x707070

    BUTTON_FONT_NAME = "OpenSans-SemiBold"
    BUTTON_FONT_SIZE = 18
    BUTTON_FONT_COLOR = 0xe8e8e8
    BUTTON_BACKGROUND_COLOR = 0x2c2c2c
    BUTTON_HEIGHT = 32
    BUTTON_SELECTED_FONT_COLOR = 0x000000
    
    NOTIFICATION_COLOR = 0x00f100



class BaseComponent:
    lv_parent: lv.obj = None

    # def __init__(self):
    #     from seedsigner.gui.renderer import Renderer
    #     self.renderer: Renderer = Renderer.get_instance()
    #     self.canvas_width = self.renderer.canvas_width
    #     self.canvas_height = self.renderer.canvas_height

    def add_to_lv_obj(self, lv_obj: lv.obj):
        raise Exception("Must implement in each child class")



class Fonts:
    import fs_driver

    # FS driver init
    fs_drv = lv.fs_drv_t()
    fs_driver.fs_register(fs_drv, 'S')

    FONT__OPEN_SANS__REGULAR__17 = lv.font_load("S:/opensans_regular_17.bin")
    FONT__OPEN_SANS__SEMIBOLD__18 = lv.font_load("S:/opensans_semibold_18.bin")
    FONT__OPEN_SANS__SEMIBOLD__20 = lv.font_load("S:/opensans_semibold_20.bin")



class Button(BaseComponent):
    text: str = "Button Label"
    screen_x: int = 0
    screen_y: int = 0
    scroll_y: int = 0
    width: int = 240 - 2*GUIConstants.EDGE_PADDING
    height: int = 32
    icon_name: str = None   # Optional icon to accompany the text
    icon_size: int = GUIConstants.ICON_INLINE_FONT_SIZE
    icon_color: str = GUIConstants.BUTTON_FONT_COLOR
    selected_icon_color: str = "black"
    icon_y_offset: int = 0
    is_icon_inline: bool = True    # True = render next to text; False = render centered above text
    right_icon_name: str = None    # Optional icon rendered right-justified
    right_icon_size: int = GUIConstants.ICON_INLINE_FONT_SIZE
    right_icon_color: str = GUIConstants.BUTTON_FONT_COLOR
    text_y_offset: int = 0
    background_color: str = GUIConstants.BUTTON_BACKGROUND_COLOR
    selected_color: str = GUIConstants.ACCENT_COLOR
    font_name: str = GUIConstants.BUTTON_FONT_NAME
    font_size: int = GUIConstants.BUTTON_FONT_SIZE
    font_color: str = GUIConstants.BUTTON_FONT_COLOR
    selected_font_color: str = GUIConstants.BUTTON_SELECTED_FONT_COLOR
    outline_color: str = None
    selected_outline_color: str = None
    is_text_centered: bool = True
    is_selected: bool = False
    align: tuple = (lv.ALIGN.CENTER, 0, 0)
    align_to: tuple = None
    lv_btn = None


    def set_is_selected_style(self):
        """ Dynamically updates how the Button is rendered based on its is_selected state """
        style = lv.style_t()
        if self.is_selected:
            style.set_bg_color(lv.color_hex(GUIConstants.ACCENT_COLOR))
            style.set_text_color(lv.color_hex(GUIConstants.BUTTON_SELECTED_FONT_COLOR))
        else:
            style.set_bg_color(lv.color_hex(self.background_color))
            style.set_text_color(lv.color_hex(self.font_color))
        self.lv_btn.add_style(style, 0)


    def add_to_lv_obj(self, lv_obj: lv.obj):
        self.lv_parent = lv_obj
        self.lv_btn = lv.btn(self.lv_parent)
        self.lv_btn.set_size(self.width, self.height)
        self.lv_btn.add_flag(lv.obj.FLAG.SNAPPABLE)
        if self.align_to:
            self.lv_btn.align_to(*self.align_to)
        else:
            self.lv_btn.align(*self.align)

        style = lv.style_t()
        style.set_pad_all(0)
        style.set_text_font(Fonts.FONT__OPEN_SANS__SEMIBOLD__18)
        style.set_shadow_opa(0)
        self.lv_btn.add_style(style, 0)

        self.set_is_selected_style()

        label = lv.label(self.lv_btn)
        label.set_text(self.text)
        if self.is_text_centered:
            label.center()
        else:
            label.align(lv.ALIGN.LEFT_MID, GUIConstants.COMPONENT_PADDING, 2)
    

    def set_is_selected(self, is_selected: bool):
        self.is_selected = is_selected
        self.set_is_selected_style()



class TopNav(BaseComponent):
    text: str = "Screen Title"
    width: int = None
    height: int = GUIConstants.TOP_NAV_HEIGHT
    background_color: str = GUIConstants.BACKGROUND_COLOR
    icon_name: str = None
    icon_color: str = GUIConstants.BODY_FONT_COLOR
    font_name: str = GUIConstants.TOP_NAV_TITLE_FONT_NAME
    font_size: int = GUIConstants.TOP_NAV_TITLE_FONT_SIZE
    font_color: str = "#fcfcfc"
    show_back_button: bool = True
    show_power_button: bool = False
    is_selected: bool = False
    back_button: Button = None


    def add_to_lv_obj(self, lv_obj: lv.obj):
        self.lv_parent = lv_obj
        self.lv_obj = lv.obj(self.lv_parent)
        self.lv_obj.set_size(240, self.height)
        self.lv_obj.align(lv.ALIGN.TOP_LEFT, 0, 0)

        style = lv.style_t()
        style.init()
        style.set_pad_all(0)
        style.set_border_width(0)
        style.set_radius(0)
        style.set_bg_color(lv.color_hex(0x000000))
        self.lv_obj.add_style(style, 0)

        if self.show_back_button:
            self.back_button = Button()
            self.back_button.text = "<"
            self.back_button.width = GUIConstants.TOP_NAV_BUTTON_SIZE
            self.back_button.height = GUIConstants.TOP_NAV_BUTTON_SIZE
            self.back_button.align = (lv.ALIGN.LEFT_MID, GUIConstants.EDGE_PADDING, -4)
            self.back_button.add_to_lv_obj(self.lv_obj)

        label = lv.label(self.lv_obj)
        label.set_text(self.text)
        label.set_long_mode(lv.label.LONG.SCROLL_CIRCULAR)
        if self.back_button:
            label.set_width(240 - GUIConstants.TOP_NAV_BUTTON_SIZE - GUIConstants.EDGE_PADDING - GUIConstants.COMPONENT_PADDING)
            label.align_to(self.back_button.lv_btn, lv.ALIGN.OUT_RIGHT_MID, GUIConstants.COMPONENT_PADDING, -4)
        else:
            label.center()
        label_style = lv.style_t()
        label_style.set_text_font(Fonts.FONT__OPEN_SANS__SEMIBOLD__20)
        label_style.set_text_color(lv.color_hex(0xffffff))
        label.add_style(label_style, 0)


