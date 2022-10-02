from micropython import const
from typing import List

import machine
import time

from seedsigner.models.singleton import Singleton


class HardwareButtons(Singleton):
    KEY_UP_PIN = const(11)
    KEY_DOWN_PIN = const(10)
    KEY_LEFT_PIN = const(7)
    KEY_RIGHT_PIN = const(3)
    KEY_PRESS_PIN = const(1)

    KEY1_PIN = const(17)
    KEY2_PIN = const(18)
    KEY3_PIN = const(14)


    @classmethod
    def get_instance(cls):
        # This is the only way to access the one and only instance
        if cls._instance is None:
            instance = cls.__new__(cls)
            cls._instance = instance

            #init GPIO
            instance.key1 = machine.Pin(cls.KEY1_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
            instance.key2 = machine.Pin(cls.KEY2_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
            instance.key3 = machine.Pin(cls.KEY3_PIN, machine.Pin.IN, machine.Pin.PULL_UP)

            instance.joy_up = machine.Pin(cls.KEY_UP_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
            instance.joy_down = machine.Pin(cls.KEY_DOWN_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
            instance.joy_left = machine.Pin(cls.KEY_LEFT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
            instance.joy_right = machine.Pin(cls.KEY_RIGHT_PIN, machine.Pin.IN, machine.Pin.PULL_UP)
            instance.joy_press = machine.Pin(cls.KEY_PRESS_PIN, machine.Pin.IN, machine.Pin.PULL_UP)            

            cls._instance.override_ind = False

            # Track state over time so we can apply input delays/ignores as needed
            cls._instance.cur_input = None           # Track which direction or button was last pressed
            cls._instance.cur_input_started = None   # Track when that input began
            cls._instance.last_input_time = int(time.time() * 1000)  # How long has it been since the last input?
            cls._instance.first_repeat_threshold = 225  # Long-press time required before returning continuous input
            cls._instance.next_repeat_threshold = 250  # Amount of time where we no longer consider input a continuous hold

        return cls._instance


    def wait_for(self, keys=[], check_release=True, release_keys=[]) -> int:
        # TODO: Refactor to keep control in the Controller and not here
        from seedsigner.controller import Controller
        controller = Controller.get_instance()

        if not release_keys:
            release_keys = keys
        self.override_ind = False

        while True:
            cur_time = int(time.time() * 1000)
            if cur_time - self.last_input_time > controller.screensaver_activation_ms and not controller.screensaver.is_running:
                # Start the screensaver. Will block execution until input detected.
                controller.start_screensaver()

                # We're back. Update last_input_time to now.
                self.update_last_input_time()

                # Freeze any further processing for a moment to avoid having the wakeup
                #   input register in the resumed UI.
                time.sleep(self.next_repeat_threshold / 1000.0)

                # Resume from a fresh loop
                continue

            for key in keys:
                if not check_release or ((check_release and key in release_keys and HardwareButtonsConstants.release_lock) or check_release and key not in release_keys):
                    # when check release is False or the release lock is released (True)
                    if self.GPIO.input(key) == GPIO.LOW or self.override_ind:
                        HardwareButtonsConstants.release_lock = False
                        if self.override_ind:
                            self.override_ind = False
                            return HardwareButtonsConstants.OVERRIDE

                        if self.cur_input != key:
                            self.cur_input = key
                            self.cur_input_started = int(time.time() * 1000)  # in milliseconds
                            self.last_input_time = self.cur_input_started
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
                                pass

            time.sleep(0.01) # wait 10 ms to give CPU chance to do other things


    def update_last_input_time(self):
        self.last_input_time = int(time.time() * 1000)


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


    def check_for_low(self, key: int = None, keys: List[int] = None) -> bool:
        # TODO: Rename this to `is_pressed` or something similar
        if key:
            keys = [key]

        for key in keys:
            if key == HardwareButtons.KEY_UP_PIN:
                if self.joy_up.value() != 0:
                    return True

            elif key == HardwareButtons.KEY_DOWN_PIN:
                if self.joy_down.value() != 0:
                    return True

            elif key == HardwareButtons.KEY_LEFT_PIN:
                if self.joy_left.value() != 0:
                    return True

            elif key == HardwareButtons.KEY_RIGHT_PIN:
                if self.joy_right.value() != 0:
                    return True

            elif key == HardwareButtons.KEY_PRESS_PIN:
                if self.joy_press.value() != 0:
                    return True

            elif key == HardwareButtons.KEY1_PIN:
                if self.key1.value() != 0:
                    return True

            elif key == HardwareButtons.KEY2_PIN:
                if self.key2.value() != 0:
                    return True

            elif key == HardwareButtons.KEY3_PIN:
                if self.key3.value() != 0:
                    return True
        return False


    def has_any_input(self) -> bool:
        return (
            self.joy_up.value() != 0 and
            self.joy_down.value() != 0 and
            self.joy_left.value() != 0 and
            self.joy_right.value() != 0 and
            self.joy_press.value() != 0 and
            self.key1.value() != 0 and
            self.key2.value() != 0 and
            self.key3.value() != 0
        )




# class used as short hand for static button/channel lookup values
# TODO: Implement `release_lock` functionality as a global somewhere. Mixes up design
#   patterns to have a static constants class plus a settable global value.
# TODO: Redundant definitions here necessary?
class HardwareButtonsConstants:
    KEY_UP = const(HardwareButtons.KEY_UP_PIN)
    KEY_DOWN = const(HardwareButtons.KEY_DOWN_PIN)
    KEY_LEFT = const(HardwareButtons.KEY_LEFT_PIN)
    KEY_RIGHT = const(HardwareButtons.KEY_RIGHT_PIN)
    KEY_PRESS = const(HardwareButtons.KEY_PRESS_PIN)
    KEY1 = const(HardwareButtons.KEY1_PIN)
    KEY2 = const(HardwareButtons.KEY2_PIN)
    KEY3 = const(HardwareButtons.KEY3_PIN)
    OVERRIDE = 1000

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
