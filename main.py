import Adafruit_DHT
import time
import usb.core
import logging

# Set up logging
logging.basicConfig(filename='watering.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def read_dht11():
    # Set sensor type : DHT11
    sensor = Adafruit_DHT.DHT11

    # Set GPIO sensor is connected to
    gpio = 4

    # Read temperature and humidity from sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)

    # Check if the sensor data is valid
    if humidity is not None and temperature is not None:
        # Return sensor data as a dictionary
        return {'temperature': temperature, 'humidity': humidity}
    else:
        logging.error('Failed to read DHT11 sensor')
        return None

def control_pump(sensor_data):
    # Set threshold values for turning the pump on and off
    humidity_threshold = 50
    temperature_threshold = 25

    # Check if the sensor data is valid
    if sensor_data is not None:
        # Check if humidity and temperature are below threshold values
        if sensor_data['humidity'] < humidity_threshold and sensor_data['temperature'] > temperature_threshold:
            # Turn on the USB port connected to the pump
            dev = usb.core.find(idVendor=0x0000, idProduct=0x0000)
            if dev is not None:
                dev.set_configuration()
                time.sleep(10)  # Wait for 10 seconds to water the plant
                # Turn off the USB port connected to the pump
                dev.reset()
            else:
                logging.error('Failed to find USB device for pump')
        else:
            logging.info('Sensor data is within threshold values')
    else:
        logging.error('Sensor data is None')


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # Read sensor data
    sensor_data = read_dht11()

    # Control pump based on sensor data
    control_pump(sensor_data)

    # Return sensor data as JSON response
    if sensor_data is not None:
        return jsonify(sensor_data)
    else:
        return 'Failed to read sensor data'
