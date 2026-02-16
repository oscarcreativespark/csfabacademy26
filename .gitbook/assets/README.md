# Simple Dashboard for Pico W

This is a simple web dashboard for the Raspberry Pi Pico W that displays button state and allows LED control.

## Features

- Real-time button state monitoring
- LED control (on/off)
- Timestamp of last button press
- Responsive web interface

## Hardware Setup

- Connect a button to GP22 (already done in your setup)
- The onboard LED is used for output

## How to Use

1. Upload `simple_dashboard.py` to your Pico W using Thonny IDE
2. Make sure the Microdot library files (`microdot.py` and `microdot_asyncio.py`) are also on your Pico W
3. Run the script on the Pico W
4. Connect to the WiFi network with:
   - SSID: `fab`
   - Password: `classroom5`
5. Open a web browser and navigate to `http://192.168.4.1`
6. The dashboard will show the button state and allow LED control

## Extending the Dashboard

This simple dashboard can be extended with:

1. Additional sensors (temperature, light, etc.)
2. More controls (PWM for LED brightness, multiple outputs)
3. Data logging and visualization
4. More advanced UI elements

## Code Overview

The dashboard combines:
- A MicroPython web server using Microdot
- Asynchronous handling of button state
- Simple HTML/CSS/JavaScript front-end
- JSON API for status updates 