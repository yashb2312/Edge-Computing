import adafruit_dht
import board
import time
import paho.mqtt.client as mqtt

# MQTT Broker Details
MQTT_BROKER = "192.168.1.100"  # Replace with your broker IP (Raspberry Pi or external broker)
MQTT_PORT = 1883
MQTT_TOPIC = "sensor/dht11"

# Set up the DHT11 sensor (Using GPIO pin 4)
dht_device = adafruit_dht.DHT11(board.D4)

# MQTT Client Setup
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

try:
    while True:
        try:
            # Read temperature and humidity
            temperature_c = dht_device.temperature
            humidity = dht_device.humidity

            if temperature_c is not None and humidity is not None:
                # Create a payload (JSON format)
                payload = f'{{"temperature": {temperature_c}, "humidity": {humidity}}}'

                # Publish data to MQTT topic
                client.publish(MQTT_TOPIC, payload)

                # Print confirmation
                print(f"Published: {payload}")
            else:
                print("Sensor reading failed, skipping publish...")

        except RuntimeError as error:
            print(f"Error reading from DHT11: {error.args[0]}")

        time.sleep(2)  # Wait for 2 seconds before the next reading

except KeyboardInterrupt:
    print("Exiting...")

finally:
    dht_device.exit()
    client.disconnect()
