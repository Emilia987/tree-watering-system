import Adafruit_DHT
import time

# Define sensor type and pin number
sensor = Adafruit_DHT.DHT11
pin = 32

# Try to read the sensor
humidity, temperature = Adafruit_DHT.read(sensor, pin)

# Print results
if humidity is not None:
    print("Humidity: {0:0.1f}%".format(humidity))
else:
    print("Failed to get humidity reading from DHT11 sensor.")

if temperature is not None:
    print("Temperature: {0:0.1f}*C".format(temperature))
else:
    print("Failed to get temperature reading from DHT11 sensor.");

time.sleep(2);
