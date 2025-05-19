import RPi.GPIO as GPIO
import time

# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO signal to use (Physical pin 7 corresponds to BCM GPIO 4)
GPIO_LED = 4

# Set up the GPIO channel as output
GPIO.setup(GPIO_LED, GPIO.OUT)

try:
    # Loop to blink the LED on and off
    while True:
        # Turn LED on
        GPIO.output(GPIO_LED, True)
        print("LED ON")
        time.sleep(1)  # Sleep for 1 second

        # Turn LED off
        GPIO.output(GPIO_LED, False)
        print("LED OFF")
        time.sleep(1)  # Sleep for 1 second

except KeyboardInterrupt:
    # Clean up on Ctrl+C exit
    GPIO.cleanup()
