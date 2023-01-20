import time

from seedsigner.hardware.qr_module import QRHost


scanner = QRHost()
print("Instantiated QRHost")

scanner.configure()
print("finished configure()")

while True:
    if scanner.uart.any() > 0:
        data = scanner.uart.read()
        if data:
            try:
                print(data.decode())
            except:
                print(data)
    time.sleep(0.1)
