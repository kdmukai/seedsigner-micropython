import lvgl as lv
import machine
import lcd_bus
import st7789



class ST7789(st7789.ST7789):
    def __init__(self, pins: dict):
        spi_bus = machine.SPI.Bus(
            host=pins["host"],  # SPI channel 0 vs 1
            mosi=pins["mosi"],
            miso=pins["miso"],
            sck=pins["clk"]
        )
        display_bus = lcd_bus.SPIBus(
            spi_bus=spi_bus,
            freq=40_000_000,  # 40MHz
            dc=pins["dc"],
            cs=pins["cs"],
        )

        super().__init__(
            data_bus=display_bus,
            display_width=pins["width"],
            display_height=pins["height"],
            backlight_pin=pins["backlight"],
            color_space=lv.COLOR_FORMAT.RGB565,
            color_byte_order=st7789.BYTE_ORDER_BGR,
            rgb565_byte_swap=True,
        )

        self.set_rotation(3)

        self.set_power(True)
        self.init()
        self.set_backlight(100)
