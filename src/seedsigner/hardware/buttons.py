from micropython import const

from machine import Pin
import time

from seedsigner.models.singleton import Singleton


class HardwareButtons:
    # @classmethod
    # def get_instance(cls):
    #     # This is the only way to access the one and only instance
    #     if cls._instance is None:
    #         instance = cls.__new__(cls)
    #         cls._instance = instance

    def __init__(self, pin_mapping: dict = None):        
        if not pin_mapping:
            pin_mapping = {
                HardwareButtonsConstants.KEY_UP: 13,
                HardwareButtonsConstants.KEY_DOWN: 14,
                HardwareButtonsConstants.KEY_LEFT: 15,
                HardwareButtonsConstants.KEY_RIGHT: 16,
                HardwareButtonsConstants.KEY_PRESS: 17,
                HardwareButtonsConstants.KEY1: 3,
                HardwareButtonsConstants.KEY2: 34,
                HardwareButtonsConstants.KEY3: 33,
            }
        
        self.pins = {}
        for key, pin_num in pin_mapping.items():
            pin = Pin(pin_num, Pin.IN, Pin.PULL_UP)
            self.pins[key] = pin
            pin.irq(handler=HardwareButtons.rising_callback, trigger=Pin.IRQ_RISING)

        self.override_ind = False

        # Track state over time so we can apply input delays/ignores as needed
        self.cur_input = None           # Track which direction or button was last pressed
        self.cur_input_started = None   # Track when that input began
        self.last_input_time = time.ticks_ms()  # How long has it been since the last input?
        self.first_repeat_threshold = 225  # Long-press time required before returning continuous input
        self.next_repeat_threshold = 250  # Amount of time where we no longer consider input a continuous hold


    def wait_for(self, keys=[], check_release=True, release_keys=[]) -> int:
        """
            * keys: which inputs to wait on; ignores all other inputs
            * check_release & release_keys: if True, subsequent loops will not return continuous/repeat
                signals if a key in `release_keys` is held down.
            
            example:
                wait_for(keys=[HardwareButtonConstants.KEY_UP, HardwareButtonConstants.KEY1], check_release=True, release_keys=[HardwareButtonConstants.KEY1])

                * Holding KEY_UP will return continuous KEY_UP signals.
                * Holding KEY1 will only yield a single KEY1 signal.
        """
        # TODO: `check_release` is unnecessary in v0.5.x since we always want to allow continuous signals unless `release_keys` is specified.
        #   Assume True if `release_keys` is not empty; assume False if `release_keys` is empty
        # TODO: Refactor to keep control in the Controller and not here
        # from seedsigner.controller import Controller
        # controller = Controller.get_instance()

        # TODO: See note above; this is no longer the desired default in v0.5.x (default should be to allow continuous signals)
        if not release_keys:
            release_keys = keys

        self.override_ind = False

        while True:
            cur_time = time.ticks_ms()
            # if cur_time - self.last_input_time > controller.screensaver_activation_ms and not controller.screensaver.is_running:
            #     # Start the screensaver. Will block execution until input detected.
            #     controller.start_screensaver()

            #     # We're back. Update last_input_time to now.
            #     self.update_last_input_time()

            #     # Freeze any further processing for a moment to avoid having the wakeup
            #     #   input register in the resumed UI.
            #     time.sleep(self.next_repeat_threshold / 1000.0)

            #     # Resume from a fresh loop
            #     continue

            for key in keys:
                if not check_release or ((check_release and key in release_keys and HardwareButtonsConstants.release_lock) or check_release and key not in release_keys):
                    pin = self.pins[key]
                    # when check release is False or the release lock is released (True)
                    if pin.value() == 0 or self.override_ind:
                        HardwareButtonsConstants.release_lock = False
                        if self.override_ind:
                            self.override_ind = False
                            return HardwareButtonsConstants.OVERRIDE

                        if self.cur_input != key:
                            self.cur_input = key
                            self.cur_input_started = time.ticks_ms()  # in milliseconds
                            self.last_input_time = self.cur_input_started
                            # print(f"{key}: started {self.cur_input_started}")
                            return key

                        else:
                            # Still pressing the same input
                            if cur_time - self.last_input_time > self.next_repeat_threshold:
                                # Too much time has elapsed to consider this the same
                                #   continuous input. Treat as a new separate press.
                                self.cur_input_started = cur_time
                                self.last_input_time = cur_time
                                return key

                            elif cur_time - self.cur_input_started > self.first_repeat_threshold:
                                # We're good to relay this immediately as continuous
                                #   input.
                                self.last_input_time = cur_time
                                return key

                            else:
                                # We're not yet at the first repeat threshold; triggering
                                #   a key now would be too soon and yields a bad user
                                #   experience when only a single click was intended but
                                #   a second input is processed because of race condition
                                #   against human response time to release the button.
                                # So there has to be a delay before we allow the first
                                #   continuous repeat to register. So we'll ignore this
                                #   round's input and **won't update any of our
                                #   timekeeping vars**. But once we cross the threshold,
                                #   we let the repeats fly.
                                # print("ignoring repeat")
                                pass

            time.sleep(0.01) # wait 10 ms to give CPU chance to do other things


    def update_last_input_time(self):
        self.last_input_time = time.ticks_ms()


    def rising_callback(channel):
        HardwareButtonsConstants.release_lock = True


    def trigger_override(self, force_release = False) -> bool:
        if force_release:
            HardwareButtonsConstants.release_lock = True

        if not self.override_ind:
            self.override_ind = True
            return True
        return False


    def force_release(self) -> bool:
        HardwareButtonsConstants.release_lock = True
        return True


    def check_for_low(self, key: int = None, keys: list[int] = None) -> bool:
        # TODO: Rename this to `is_pressed` or something similar
        if key:
            keys = [key]

        for key in keys:
            if self.pins[key].value() == 0:
                return True
        return False


    def has_any_input(self) -> bool:
        for key, pin in self.pins.items():
            if pin.value() == 0:
                return True
        return False



# class used as short hand for static button/channel lookup values
# TODO: Implement `release_lock` functionality as a global somewhere. Mixes up design
#   patterns to have a static constants class plus a settable global value.
# TODO: Redundant definitions here necessary?
class HardwareButtonsConstants:
    KEY_UP = const(1)
    KEY_DOWN = const(2)
    KEY_LEFT = const(3)
    KEY_RIGHT = const(4)
    KEY_PRESS = const(5)
    KEY1 = const(6)
    KEY2 = const(7)
    KEY3 = const(8)
    OVERRIDE = const(1000)

    ALL_KEYS = [
        KEY_UP,
        KEY_DOWN,
        KEY_LEFT,
        KEY_RIGHT,
        KEY_PRESS,
        KEY1,
        KEY2,
        KEY3,
    ]

    KEYS__LEFT_RIGHT_UP_DOWN = [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN]
    KEYS__ANYCLICK = [KEY_PRESS, KEY1, KEY2, KEY3]

    release_lock = True # released when True, locked when False

    key_names = {
        KEY_UP: "UP",
        KEY_DOWN: "DOWN",
        KEY_LEFT: "LEFT",
        KEY_RIGHT: "RIGHT",
        KEY_PRESS: "PRESS",
        KEY1: "KEY1",
        KEY2: "KEY2",
        KEY3: "KEY3",
    }

    @classmethod
    def get_key_name(cls, key: int) -> str:
        return cls.key_names[key]
