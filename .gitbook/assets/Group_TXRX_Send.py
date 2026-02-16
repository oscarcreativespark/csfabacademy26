import board
import busio
import digitalio
import analogio
import time

# Set up UART on TX=GD6, RX=D7 (we only use TX here)
uart = busio.UART(tx=board.TX, rx=board.RX, baudrate=9600)

# Set up a pot on analog pin A0
pot = analogio.AnalogIn(board.A0)

center = 65535/2 # The center of the pot
neutral_zone = 10000 # Area on pot where there is no input

while True:
    
    pot_value = pot.value
    deviation = pot_value - center

    print(pot_value)

    if abs(deviation) > neutral_zone: 
        
        if deviation > 0:
            uart.write(b'PRESSED\n')
            print("Sent: PRESSED")
    time.sleep(1)
