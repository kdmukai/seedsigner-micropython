# seedsigner-micropython


## ESP32-S2 Saola-1R wiring
ST7789 display (via Waveshare hat):
```
ST7789      RASPI GPIO      SAOLA
---------------------------------
3.3V        3V3
GND         GND
SCLK        11/SCLK         12
MOSI        10/MOSI         11
CS          8/CE0           10
DC          25               1
RST         27               2
BL          24              (not connected)
```

Waveshare hat joystick/button inputs:
```
BUTTON          RASPI GPIO      SAOLA
-------------------------------------
joystick up      6              13
joystick down   19              14
joystick left    5              15
joystick right  26              16
joystick press  13              17
key 1           21               3
key 2           20              34
key 3           16              33
```

OV2640 camera

_note: the camera module lists D2 through D9 but the camera driver expects d0 through d7. Map D2 as d0, D3 as d1, ..., D9 as d7._

```
OV2640      SAOLA
-----------------
3.3V
GND
SIOC         9 (SCA)
SIOD         8 (SDA)
VSYNC        7
HREF         6
PCLK         5
XCLK         4
D9          42
D8          41
D7          40
D6          39
D5          38
D4          37
D3          36
D2          35
RET         (not connected)
PWDN        (not connected)
```
