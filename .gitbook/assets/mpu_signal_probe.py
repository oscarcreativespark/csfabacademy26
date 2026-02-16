from machine import Pin, I2C, SoftI2C
import time
import math
import gc

# Free up memory
gc.collect()

# MPU6050 registers
MPU_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
GYRO_XOUT_H = 0x43
TEMP_OUT_H = 0x41
WHO_AM_I = 0x75

# Set DEBUG mode
DEBUG = True

def debug_print(message):
    """Print debug messages if DEBUG is enabled"""
    if DEBUG:
        print(f"DEBUG: {message}")

def init_mpu6050(i2c):
    """Initialize the MPU6050 sensor"""
    print("\nInitializing MPU6050...")
    
    try:
        # Check the device ID
        debug_print("Reading WHO_AM_I register")
        who_am_i = i2c.readfrom_mem(MPU_ADDR, WHO_AM_I, 1)[0]
        print(f"MPU6050 WHO_AM_I register: 0x{who_am_i:02X} (should be 0x68)")
        
        if who_am_i != 0x68:
            print("WARNING: Unexpected device ID!")
            return False
        
        # Reset the device
        print("Resetting device...")
        debug_print("Writing 0x80 to PWR_MGMT_1")
        i2c.writeto_mem(MPU_ADDR, PWR_MGMT_1, bytes([0x80]))
        time.sleep(0.1)
        
        # Wake up the device
        print("Waking up device...")
        debug_print("Writing 0x00 to PWR_MGMT_1")
        i2c.writeto_mem(MPU_ADDR, PWR_MGMT_1, bytes([0x00]))
        time.sleep(0.1)
        
        print("MPU6050 initialization complete!")
        return True
    except Exception as e:
        print(f"Error initializing MPU6050: {e}")
        return False

def read_sensor_data(i2c):
    """Read all sensor data in a single transaction"""
    print("\nReading all sensor data...")
    
    try:
        debug_print("Reading 14 bytes from ACCEL_XOUT_H")
        # Read 14 bytes of data starting from ACCEL_XOUT_H
        data = i2c.readfrom_mem(MPU_ADDR, ACCEL_XOUT_H, 14)
        
        # Parse accelerometer values
        accel_x = (data[0] << 8) | data[1]
        accel_y = (data[2] << 8) | data[3]
        accel_z = (data[4] << 8) | data[5]
        
        # Parse temperature
        temp = (data[6] << 8) | data[7]
        
        # Parse gyroscope values
        gyro_x = (data[8] << 8) | data[9]
        gyro_y = (data[10] << 8) | data[11]
        gyro_z = (data[12] << 8) | data[13]
        
        # Convert to signed values
        if accel_x > 32767: accel_x -= 65536
        if accel_y > 32767: accel_y -= 65536
        if accel_z > 32767: accel_z -= 65536
        if temp > 32767: temp -= 65536
        if gyro_x > 32767: gyro_x -= 65536
        if gyro_y > 32767: gyro_y -= 65536
        if gyro_z > 32767: gyro_z -= 65536
        
        # Print physical measurements
        print("\n=== SENSOR READINGS ===")
        print(f"Accelerometer: X={accel_x/16384:.3f}g, Y={accel_y/16384:.3f}g, Z={accel_z/16384:.3f}g")
        print(f"Gyroscope: X={gyro_x/131:.2f}°/s, Y={gyro_y/131:.2f}°/s, Z={gyro_z/131:.2f}°/s")
        print(f"Temperature: {temp/340 + 36.53:.2f}°C")
        
        # Calculate orientation
        accel_magnitude = (accel_x**2 + accel_y**2 + accel_z**2)**0.5
        roll = math.atan2(accel_y, accel_z) * 180 / math.pi
        pitch = math.atan2(-accel_x, (accel_y**2 + accel_z**2)**0.5) * 180 / math.pi
        
        print("\n=== ORIENTATION ===")
        print(f"Roll: {roll:.1f}°")
        print(f"Pitch: {pitch:.1f}°")
        print(f"Acceleration magnitude: {accel_magnitude/16384:.3f}g")
        
        return True
    except Exception as e:
        print(f"Error reading sensor data: {e}")
        return False

def read_sensor_single_registers(i2c):
    """Read sensor data one register at a time to avoid timeouts"""
    print("\nReading sensor data one register at a time...")
    
    try:
        # Read accelerometer X
        debug_print("Reading accelerometer X registers")
        accel_x_h = i2c.readfrom_mem(MPU_ADDR, ACCEL_XOUT_H, 1)[0]
        accel_x_l = i2c.readfrom_mem(MPU_ADDR, ACCEL_XOUT_H + 1, 1)[0]
        accel_x = (accel_x_h << 8) | accel_x_l
        print(f"Accelerometer X: {accel_x}")
        
        # Read accelerometer Y
        debug_print("Reading accelerometer Y registers")
        accel_y_h = i2c.readfrom_mem(MPU_ADDR, ACCEL_XOUT_H + 2, 1)[0]
        accel_y_l = i2c.readfrom_mem(MPU_ADDR, ACCEL_XOUT_H + 3, 1)[0]
        accel_y = (accel_y_h << 8) | accel_y_l
        print(f"Accelerometer Y: {accel_y}")
        
        # Read accelerometer Z
        debug_print("Reading accelerometer Z registers")
        accel_z_h = i2c.readfrom_mem(MPU_ADDR, ACCEL_XOUT_H + 4, 1)[0]
        accel_z_l = i2c.readfrom_mem(MPU_ADDR, ACCEL_XOUT_H + 5, 1)[0]
        accel_z = (accel_z_h << 8) | accel_z_l
        print(f"Accelerometer Z: {accel_z}")
        
        # Convert to signed values
        if accel_x > 32767: accel_x -= 65536
        if accel_y > 32767: accel_y -= 65536
        if accel_z > 32767: accel_z -= 65536
        
        # Print physical measurements
        print("\n=== SENSOR READINGS ===")
        print(f"Accelerometer: X={accel_x/16384:.3f}g, Y={accel_y/16384:.3f}g, Z={accel_z/16384:.3f}g")
        
        # Calculate orientation (simplified, using just accelerometer)
        accel_magnitude = (accel_x**2 + accel_y**2 + accel_z**2)**0.5
        roll = math.atan2(accel_y, accel_z) * 180 / math.pi
        pitch = math.atan2(-accel_x, (accel_y**2 + accel_z**2)**0.5) * 180 / math.pi
        
        print("\n=== ORIENTATION ===")
        print(f"Roll: {roll:.1f}°")
        print(f"Pitch: {pitch:.1f}°")
        print(f"Acceleration magnitude: {accel_magnitude/16384:.3f}g")
        
        return True
    except Exception as e:
        print(f"Error reading sensor data: {e}")
        return False

def analyze_bus_timing(i2c, freq):
    """Analyze I2C bus timing characteristics"""
    print("\nAnalyzing I2C bus timing...")
    
    samples = []
    for i in range(5):
        try:
            debug_print(f"Timing test {i+1}/5")
            sample_start = time.ticks_us()
            i2c.readfrom_mem(MPU_ADDR, WHO_AM_I, 1)
            duration = time.ticks_diff(time.ticks_us(), sample_start)
            samples.append(duration)
            time.sleep_ms(10)
            print(f"Test {i+1}: {duration} µs")
        except Exception as e:
            print(f"Error during timing test {i+1}: {e}")
    
    if samples:
        avg_duration = sum(samples) / len(samples)
        max_duration = max(samples)
        min_duration = min(samples)
        
        print(f"Average transaction duration: {avg_duration:.2f} µs")
        print(f"Maximum duration: {max_duration} µs")
        print(f"Minimum duration: {min_duration} µs")
        print(f"Clock period: {1000000/freq:.2f} µs (Frequency: {freq} Hz)")
    else:
        print("No timing samples collected due to errors.")

def try_both_i2c_implementations():
    """Try both hardware I2C and SoftI2C implementations"""
    print("\nTrying both I2C implementations...")
    
    # Try Hardware I2C
    hw_freq = 100000  # Store the frequency we're setting
    print("\n1. Testing Hardware I2C:")
    try:
        hw_i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=hw_freq, timeout=5000)  # Increased timeout from 1000 to 5000
        devices = hw_i2c.scan()
        if devices:
            print(f"  Devices found: {[hex(d) for d in devices]}")
            if MPU_ADDR in devices:
                print(f"  MPU6050 found at address {hex(MPU_ADDR)}")
                return hw_i2c, "Hardware I2C", hw_freq
            else:
                print("  MPU6050 not found")
        else:
            print("  No devices found")
    except Exception as e:
        print(f"  Hardware I2C error: {e}")
    
    # Try slower hardware I2C
    hw_freq_slow = 50000  # Try a slower frequency
    print("\n2. Testing Slower Hardware I2C:")
    try:
        hw_i2c_slow = I2C(1, scl=Pin(7), sda=Pin(6), freq=hw_freq_slow, timeout=5000)
        devices = hw_i2c_slow.scan()
        if devices:
            print(f"  Devices found: {[hex(d) for d in devices]}")
            if MPU_ADDR in devices:
                print(f"  MPU6050 found at address {hex(MPU_ADDR)}")
                return hw_i2c_slow, "Hardware I2C (Slow)", hw_freq_slow
            else:
                print("  MPU6050 not found")
        else:
            print("  No devices found")
    except Exception as e:
        print(f"  Slower Hardware I2C error: {e}")
    
    # Try Software I2C
    soft_freq = 50000  # Lower frequency for SoftI2C for better reliability
    print("\n3. Testing Software I2C:")
    try:
        soft_i2c = SoftI2C(scl=Pin(7), sda=Pin(6), freq=soft_freq)
        devices = soft_i2c.scan()
        if devices:
            print(f"  Devices found: {[hex(d) for d in devices]}")
            if MPU_ADDR in devices:
                print(f"  MPU6050 found at address {hex(MPU_ADDR)}")
                return soft_i2c, "Software I2C", soft_freq
            else:
                print("  MPU6050 not found")
        else:
            print("  No devices found")
    except Exception as e:
        print(f"  Software I2C error: {e}")
    
    return None, "No working I2C implementation found", 0

def main():
    print("MPU6050 Signal Probe and Analysis")
    print("================================")
    
    try:
        # Try to find the best I2C implementation
        i2c, i2c_type, i2c_freq = try_both_i2c_implementations()
        
        if not i2c:
            print("\nCould not initialize I2C. Please check your connections.")
            return
                
        print(f"\nUsing {i2c_type} with frequency {i2c_freq} Hz")
        
        # Initialize the device
        if not init_mpu6050(i2c):
            print("Failed to initialize MPU6050")
            return
        
        while True:
            print("\nOptions:")
            print("1. Read all sensor data (bulk read)")
            print("2. Read sensor data (one register at a time)")
            print("3. Analyze bus timing")
            print("4. Exit")
            
            choice = input("Select an option (1-4): ")
            
            if choice == '1':
                read_sensor_data(i2c)
            elif choice == '2':
                read_sensor_single_registers(i2c)
            elif choice == '3':
                analyze_bus_timing(i2c, i2c_freq)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
                
    except KeyboardInterrupt:
        print("\nProgram stopped by user")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main() 