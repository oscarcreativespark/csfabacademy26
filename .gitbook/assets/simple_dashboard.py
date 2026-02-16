from machine import Pin
import network
import uasyncio as asyncio
import time
from microdot_asyncio import Microdot, Request, Response

# --- Hardware Setup ---
led = Pin('LED', Pin.OUT)
button = Pin(22, Pin.IN, Pin.PULL_UP)  # Button is connected to GP22, not GP21
button_state = "Released"  # Initialize button state
last_press_time = 0  # Track when button was last pressed

# --- Network Setup ---
wifi = network.WLAN(network.AP_IF)
wifi.config(ssid='fab', key='classroom5')
wifi.active(True)
while not wifi.active():
    pass
print("AP started at", wifi.ifconfig())
print("ssid: fab, key: classroom5")

# --- Web Server Setup ---
server = Microdot()

# --- Dashboard HTML ---
def dashboard_html():
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pico W Dashboard</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                margin: 0; 
                padding: 20px; 
                background: #f5f5f5; 
            }
            .dashboard { 
                max-width: 600px; 
                margin: 0 auto; 
                background: white; 
                padding: 20px; 
                border-radius: 10px; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.1); 
            }
            .card { 
                background: #f9f9f9; 
                border-radius: 5px; 
                padding: 15px; 
                margin-bottom: 15px; 
            }
            .control-panel { 
                display: flex; 
                gap: 10px; 
                flex-wrap: wrap; 
                margin-top: 10px;
            }
            .button { 
                background: #2c3e50; 
                color: white; 
                border: none; 
                padding: 10px 15px; 
                border-radius: 5px; 
                cursor: pointer; 
            }
            .button:hover { 
                background: #34495e; 
            }
            .status-indicator {
                padding: 10px;
                border-radius: 5px;
                margin-top: 10px;
                text-align: center;
                font-weight: bold;
            }
            .released {
                background-color: #e74c3c;
                color: white;
            }
            .pressed {
                background-color: #2ecc71;
                color: white;
            }
        </style>
    </head>
    <body>
        <div class="dashboard">
            <h1>Pico W Dashboard</h1>
            
            <div class="card">
                <h2>LED Control</h2>
                <div class="control-panel">
                    <button class="button" onclick="toggleLED('on')">LED ON</button>
                    <button class="button" onclick="toggleLED('off')">LED OFF</button>
                </div>
                <div id="led-message"></div>
            </div>
            
            <div class="card">
                <h2>Button Status</h2>
                <div id="button-status" class="status-indicator released">
                    Checking...
                </div>
                <p>Last pressed: <span id="last-pressed">Never</span></p>
            </div>
        </div>

        <script>
            // Control the LED
            function toggleLED(state) {
                fetch(state)
                    .then(response => response.text())
                    .then(data => {
                        document.getElementById('led-message').innerHTML = data;
                    });
            }
            
            // Update button status periodically
            function updateButtonStatus() {
                fetch('button-status')
                    .then(response => response.json())
                    .then(data => {
                        const statusElement = document.getElementById('button-status');
                        statusElement.textContent = data.state;
                        statusElement.className = 'status-indicator ' + 
                            (data.state === 'Pressed' ? 'pressed' : 'released');
                        
                        if (data.last_press_time > 0) {
                            document.getElementById('last-pressed').innerText = 
                                new Date(data.last_press_time * 1000).toLocaleTimeString();
                        }
                    });
            }
            
            // Update status every 200ms
            setInterval(updateButtonStatus, 200);
            
            // Initial status update
            updateButtonStatus();
        </script>
    </body>
    </html>
    '''
    return html

# --- Route Handlers ---
@server.get('/')
async def get_root(request):
    return dashboard_html(), 200, {'Content-Type': 'text/html'}

@server.get('/on')
async def get_on(request):
    led.value(1)
    return "LED is ON", 200, {'Content-Type': 'text/html'}

@server.get('/off')
async def get_off(request):
    led.value(0)
    return "LED is OFF", 200, {'Content-Type': 'text/html'}

@server.get('/button-status')
async def get_button_status(request):
    global button_state, last_press_time
    return {
        "state": button_state,
        "last_press_time": last_press_time
    }, 200, {'Content-Type': 'application/json'}

# --- Button Monitoring Task ---
async def monitor_button():
    global button_state, last_press_time
    while True:
        # Button is pulled up, so value() == 0 means pressed
        if button.value() == 0 and button_state != "Pressed":
            button_state = "Pressed"
            last_press_time = time.time()
            print("Button pressed")
        elif button.value() == 1 and button_state != "Released":
            button_state = "Released"
            print("Button released")
        await asyncio.sleep(0.05)  # Check every 50ms

# --- Main Application ---
async def main():
    button_task = asyncio.create_task(monitor_button())
    server_task = asyncio.create_task(server.start_server(port=80, debug=True))
    await asyncio.gather(button_task, server_task)

# --- Run Application ---
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Server stopped by user") 