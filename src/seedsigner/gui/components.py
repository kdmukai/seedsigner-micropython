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



class FontAwesomeIconConstants:
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

    FONT__OPEN_SANS__REGULAR__17__BPP8 = lv.font_load("S:/opensans_regular_17_bpp8.bin")
    FONT__OPEN_SANS__SEMIBOLD__18 = lv.font_load("S:/opensans_semibold_18.bin")
    FONT__OPEN_SANS__SEMIBOLD__20 = lv.font_load("S:/opensans_semibold_20.bin")
    FONT__OPEN_SANS__SEMIBOLD__26 = lv.font_load("S:/opensans_semibold_26.bin")
    FONT__FONT_AWESOME__24 = lv.font_load("S:/fontawesome_24.bin")
    FONT__FONT_AWESOME__SUBSET__36 = lv.font_load("S:/fontawesome_subset_36.bin")
    FONT__SEEDSIGNER_GLYPHS__24 = lv.font_load("S:/seedsigner_glyphs_24.bin")



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
            self.lv_label.set_long_mode(lv.label.LONG.SCROLL_CIRCULAR)
        else:
            style.set_bg_color(lv.color_hex(self.background_color))
            style.set_text_color(lv.color_hex(self.font_color))
            self.lv_label.set_long_mode(lv.label.LONG.CLIP)
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
        if self.font_size == GUIConstants.BUTTON_FONT_SIZE:
            style.set_text_font(Fonts.FONT__OPEN_SANS__SEMIBOLD__18)
        elif self.font_size == 20:
            style.set_text_font(Fonts.FONT__OPEN_SANS__SEMIBOLD__20)
        style.set_shadow_opa(0)
        self.lv_btn.add_style(style, 0)

        self.lv_icon_label = None
        if self.icon_name:
            self.lv_icon_label = lv.label(self.lv_btn)
            self.lv_icon_label.set_text(self.icon_name)
            style = lv.style_t()
            style.set_pad_all(0)
            if SeedSignerCustomIconConstants.MIN_VALUE <= self.icon_name and self.icon_name <= SeedSignerCustomIconConstants.MAX_VALUE:
                style.set_text_font(Fonts.FONT__SEEDSIGNER_GLYPHS__24)
            else:
                if self.icon_size == 24:
                    style.set_text_font(Fonts.FONT__FONT_AWESOME__24)
                elif self.icon_size == GUIConstants.ICON_LARGE_BUTTON_SIZE:
                    style.set_text_font(Fonts.FONT__FONT_AWESOME__SUBSET__36)

            style.set_shadow_opa(0)
            self.lv_icon_label.add_style(style, 0)
            if self.is_text_centered:
                if not self.is_icon_inline:
                    self.lv_icon_label.align_to(self.lv_btn, lv.ALIGN.TOP_MID, 0, GUIConstants.COMPONENT_PADDING)
                else:
                    self.lv_icon_label.center()
            else:
                self.lv_icon_label.align(lv.ALIGN.LEFT_MID, GUIConstants.COMPONENT_PADDING, 0)
            
            # Must update the obj to get correct x, width, etc data
            self.lv_icon_label.update_layout()

        self.lv_label = lv.label(self.lv_btn)
        self.lv_label.set_long_mode(lv.label.LONG.CLIP)
        self.lv_label.set_text(self.text)

        if self.is_text_centered:
            if self.lv_icon_label and not self.is_icon_inline:
                # Text has to be rendered centered below the icon
                self.lv_label.align_to(self.lv_icon_label, lv.ALIGN.OUT_BOTTOM_MID, 0, int(GUIConstants.COMPONENT_PADDING/2))
            else:
                self.lv_label.center()
        else:
            if self.lv_icon_label and self.is_icon_inline:
                self.lv_label.set_width(self.width - GUIConstants.COMPONENT_PADDING - self.lv_icon_label.get_x() - self.lv_icon_label.get_width() - GUIConstants.COMPONENT_PADDING)
                self.lv_label.align_to(self.lv_icon_label, lv.ALIGN.OUT_RIGHT_MID, GUIConstants.COMPONENT_PADDING, 2)
            else:
                self.lv_label.set_width(self.width - 2*GUIConstants.COMPONENT_PADDING)
                self.lv_label.align(lv.ALIGN.LEFT_MID, GUIConstants.COMPONENT_PADDING, 2)

        # # Must update the obj to get correct x, width, etc data
        # self.lv_btn.update_layout()

        self.set_is_selected_style()


    def set_is_selected(self, is_selected: bool):
        self.is_selected = is_selected
        self.set_is_selected_style()



class LargeIconButton(Button):
    width: int = 108
    height: int = 76
    icon_size: int = GUIConstants.ICON_LARGE_BUTTON_SIZE
    is_icon_inline: bool = False
    font_size: int = 20
    is_text_centered: bool = True


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
            self.back_button.text = ""
            self.back_button.icon_name = SeedSignerCustomIconConstants.LARGE_CHEVRON_LEFT
            self.back_button.width = GUIConstants.TOP_NAV_BUTTON_SIZE
            self.back_button.height = GUIConstants.TOP_NAV_BUTTON_SIZE
            self.back_button.align = (lv.ALIGN.LEFT_MID, GUIConstants.EDGE_PADDING, -4)
            self.back_button.add_to_lv_obj(self.lv_obj)

        if self.show_power_button:
            self.power_button = Button()
            self.power_button.text = ""
            self.power_button.icon_name = FontAwesomeIconConstants.POWER_OFF
            self.power_button.width = GUIConstants.TOP_NAV_BUTTON_SIZE
            self.power_button.height = GUIConstants.TOP_NAV_BUTTON_SIZE
            self.power_button.align = (lv.ALIGN.RIGHT_MID, -1 * GUIConstants.EDGE_PADDING, -4)
            self.power_button.add_to_lv_obj(self.lv_obj)

        label = lv.label(self.lv_obj)
        label.set_text(self.text)
        label.set_long_mode(lv.label.LONG.SCROLL_CIRCULAR)
        if self.back_button:
            label.set_width(240 - GUIConstants.EDGE_PADDING - GUIConstants.TOP_NAV_BUTTON_SIZE - GUIConstants.COMPONENT_PADDING)
            label.align_to(self.back_button.lv_btn, lv.ALIGN.OUT_RIGHT_MID, GUIConstants.COMPONENT_PADDING, -4)
        else:
            label.center()
        label_style = lv.style_t()
        if self.font_size == GUIConstants.TOP_NAV_TITLE_FONT_SIZE:
            style.set_text_font(Fonts.FONT__OPEN_SANS__SEMIBOLD__20)
        elif self.font_size == 26:
            style.set_text_font(Fonts.FONT__OPEN_SANS__SEMIBOLD__26)
        label_style.set_text_color(lv.color_hex(0xffffff))
        label_style.set_pad_right(GUIConstants.EDGE_PADDING)
        label.add_style(label_style, 0)


    def set_is_selected(self, is_selected: bool):
        self.is_selected = is_selected
        if self.show_back_button:
            self.back_button.set_is_selected(is_selected)
        if self.show_power_button:
            self.power_button.set_is_selected(is_selected)
