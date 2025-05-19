import time
import Adafruit_DHT
import BlynkLib

# Replace with your Blynk Auth Token
BLYNK_AUTH_TOKEN = '_XnsCg95jOshh7O2jiBuMq7oWbVA6iCr'

# Set the sensor type and the GPIO pin
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin number where the sensor's data pin is connected

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

# Function to read DHT11 data and send it to Blynk
def read_and_send_data():
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        print(f'Temperature: {temperature}°C, Humidity: {humidity}%')
        blynk.virtual_write(1, temperature)  # Send temperature to virtual pin V1
        blynk.virtual_write(0, humidity)     # Send humidity to virtual pin V0
    else:
        print('Failed to retrieve data from sensor')

# Main loop
while True:
    read_and_send_data()  # Read and send data to Blynk
    blynk.run()           # Keep Blynk connection alive
    time.sleep(2)         # Wait before next reading
