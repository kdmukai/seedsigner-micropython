import time
from seedsigner.hardware.buttons import HardwareButtons, HardwareButtonsConstants

buttons = HardwareButtons()

# print("check for any input")
# while True:
#     if buttons.has_any_input():
#         print("Input!")
#         break

# print("check for up")
# while True:
#     if buttons.check_for_low(key=HardwareButtonsConstants.KEY_UP):
#         print("UP!")
#         break

# print("check for KEY2")
# while True:
#     if buttons.check_for_low(key=HardwareButtonsConstants.KEY2):
#         print("KEY2!")
#         break

# print("check for LEFT or RIGHT")
# while True:
#     if buttons.check_for_low(keys=[HardwareButtonsConstants.KEY_LEFT, HardwareButtonsConstants.KEY_RIGHT]):
#         print("LEFT or RIGHT!")
#         break
# time.sleep(1)

print("test wait_for on any input")

while True:
    # allow repeats for directional keys; single response only for center press or KEY1, 2, 3.
    key = buttons.wait_for(keys=HardwareButtonsConstants.ALL_KEYS, check_release=True, release_keys=HardwareButtonsConstants.KEYS__ANYCLICK)
    print(HardwareButtonsConstants.get_key_name(key))
