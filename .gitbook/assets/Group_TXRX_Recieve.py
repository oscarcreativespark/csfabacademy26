import board
import busio
import digitalio
import time

Set up UART on TX=GP4, RX=GP5 (we only use RX here)
uart = busio.UART(tx=board.TX, rx=board.RX, baudrate=9600)

Set up onboard LED (or use another GPIO pin)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

buffer = b''

while True:
    data = uart.read(32)  # Read up to 32 bytes at once
    led.value = not led.value  # toggle LED

if data:
    buffer += data
    if b'\n' in buffer:
        line, _, buffer = buffer.partition(b'\n')
        message = line.strip().decode("utf-8")
        print("Received:", message)
        if message == "PRESSED":
            led.value = not led.value  # toggle LED