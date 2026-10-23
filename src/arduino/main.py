import serial
import time

# Replace COM5 with your Arduino's serial port
with serial.Serial("COM5", 9600, timeout=1) as arduino:
    time.sleep(2)  # Wait for Arduino to restart

    for i in range(10):
        arduino.write(b'1')
        #print("Sent ON command")
        time.sleep(0.2)

        arduino.write(b'0')
        #print("Sent OFF command")
        time.sleep(0.2)
