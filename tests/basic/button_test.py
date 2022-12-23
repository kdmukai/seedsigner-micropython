from seedsigner.hardware.buttons import HardwareButtons, HardwareButtonsConstants

buttons = HardwareButtons()

while True:
    # allow repeats for directional keys; single response only for center press or KEY1, 2, 3.
    key = buttons.wait_for(keys=HardwareButtonsConstants.ALL_KEYS, check_release=True, release_keys=HardwareButtonsConstants.KEYS__ANYCLICK)
    print(HardwareButtonsConstants.get_key_name(key))
