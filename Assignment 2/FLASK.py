from flask import Flask, render_template, jsonify
import adafruit_dht
import board

app = Flask(__name__)
DHT_SENSOR_PIN = board.D4  # GPIO4

def read_dht_sensor():
    dht_sensor = adafruit_dht.DHT11(DHT_SENSOR_PIN)
    try:
        temperature = dht_sensor.temperature
        humidity = dht_sensor.humidity
        return temperature, humidity
    except RuntimeError:
        return None, None
    finally:
        dht_sensor.exit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sensor-data')
def sensor_data():
    temperature, humidity = read_dht_sensor()
    if temperature is not None and humidity is not None:
        data = {
            "temperature": f"{temperature:.1f} °C",
            "humidity": f"{humidity:.1f} %"
        }
    else:
        data = {"error": "Unable to read sensor data."}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
