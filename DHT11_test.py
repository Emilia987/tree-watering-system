import Adafruit_DHT
import time

# Define sensor type and pin number
sensor = Adafruit_DHT.DHT11
pin = 16

# Define number of readings
num_readings = 10

# Loop through readings
for i in range(num_readings):
    # Try to read the sensor
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    # Print results
    if humidity is not None and temperature is not None:
        print('Reading {0}: Temp={1:0.1f}*C  Humidity={2:0.1f}%'.format(i+1, temperature, humidity))
    else:
        print('Failed to get reading from DHT11 sensor.')

    # Wait a moment before next reading
    time.sleep(2)
